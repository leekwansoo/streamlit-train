# streamlit_app.py

import streamlit as st
import pymongo
import pandas as pd 
import csv
from trace_train import trace_train
# Initialize connection.
# Uses st.cache_resource to only run once.

@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

#client = init_connection()
from database import coll, client
cursor = coll.find()

    
@st.cache_data(ttl=600)
def get_data():
    cursor = coll.find()
    items = []
    for doc in cursor:
        item = doc
        items.append(doc)
    return items

trains = get_data()

# Print results.
#for item in trains:
    #st.write(item)
    #st.write(f"{item['date']} :   pushup :{item['pushup']}, squat :{item['squat']} ")

#st.write(trains)   

# store items into a csv file 
to_csv = trains
keys = to_csv[0].keys()
field_names =["_id", "date", "user", "pushup", "stomach","squat", "arm", "uplift", "upheel", "kick_on_chair","spreading_thigh"]
with open('trains.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=field_names)
    dict_writer.writeheader()
    dict_writer.writerows(to_csv)
    
data = pd.read_csv('trains.csv')
st.dataframe(data)
# draw the trace

st.sidebar.button("Daily Record", on_click=trace_train)

# Download data in CSV format
def convert_df(data):
    return data.to_csv(index=False).encode('utf-8')

data = convert_df(data)

st.download_button(
    "Press to Download",
    data,
    "trains.csv",
    "text/csv",
    key='download-csv'
)



 

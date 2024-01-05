import streamlit as st
import pandas as pd
import numpy as np
import time

# column_names = ["date","user","pushup","stomach","squat","arm","uplift","upheel"]
def data_entry():
      # Getting user input
    with st.form(key='columns_in_form'):
        c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)
        with c1:
            date = st.date_input('today')
        with c2:
            user = st.text_input('user')
        with c3:
            pushup = st.number_input('pushup', value = 0)
        with c4:
            stomach = st.number_input('stomach', value = 0)
        with c5:
            squat = st.number_input('squat', value = 0)
        with c6:
            arm = st.number_input('arm', value = 0)
        with c7:
            uplift = st.number_input('uplift', value = 0)
        with c8:
            upheel = st.number_input('upheel', value = 0)

        submitButton = st.form_submit_button(label = 'Submit Data')

    # Create dataframe for new_record with user input

    new_record = pd.DataFrame({
        'date': date,
        'user': user,
        'pushup':pushup,
        'stomach': stomach,
        'squat': squat,
        'arm':arm, 
        'uplift': uplift,
        'upheel':upheel,   
    }, index=[0])  #ValueError("If using all scalar values, you must pass an index")

    st.dataframe(new_record)

data_entry()

    # Display the updated dataframe
    #st.table(df.set_index('Title'))

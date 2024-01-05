import streamlit as st
import streamlit.components.v1 as stc

# File Processing Pkgs
import pandas as pd
import docx2txt
from PIL import Image 
from PyPDF2 import PdfFileReader
import pdfplumber
from trace_train import trace_train
from data_entry import data_entry
from pages.get_train import get_train

@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 

  
st.sidebar.title("Activities for Home Train")

menu = ["Upload Image","Train Record", "Data Entry" , "DocumentFiles","About"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Upload Image":
    st.sidebar.subheader("Upload Image")
    image_file = st.sidebar.file_uploader("Upload Image",type=['png','jpeg','jpg'])
    if image_file is not None:
    
        # To See Details
        # st.write(type(image_file))
        # st.write(dir(image_file))
        file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
        st.write(file_details)

        img = load_image(image_file)
        st.image(img,width=250,height=250)


elif choice == "Train Record":
    st.sidebar.button("Get Train Record", on_click = get_train)
    
elif choice == "Data Entry":
    st.sidebar.button("Upload Train Record", on_click = data_entry)
       
elif choice == "DocumentFiles":
    st.sidebar.subheader("Upload Documents")
    docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])
    if st.button("Process"):
        if docx_file is not None:
            file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
            st.write(file_details)
            # Check File Type
            if docx_file.type == "text/plain":
                # raw_text = docx_file.read() # read as bytes
                # st.write(raw_text)
                # st.text(raw_text) # fails
                st.text(str(docx_file.read(),"utf-8")) # empty
                raw_text = str(docx_file.read(),"utf-8") # works with st.text and st.write,used for further processing
                # st.text(raw_text) # Works
                st.write(raw_text) # works
            elif docx_file.type == "application/pdf":
                # raw_text = read_pdf(docx_file)
                # st.write(raw_text)
                try:
                    with pdfplumber.open(docx_file) as pdf:
                        page = pdf.pages[0]
                        st.write(page.extract_text())
                except:
                    st.write("None")
                    
                
            elif docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            # Use the right file processor ( Docx,Docx2Text,etc)
                raw_text = docx2txt.process(docx_file) # Parse in the uploadFile Class 
                st.write(raw_text)

else:
    st.sidebar.subheader("About")
    st.sidebar.info("Home Training Tracker")
    st.sidebar.info("Designed BY JD Green")

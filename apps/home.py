from msilib.schema import Directory
from operator import imod
from tkinter import Image
import cv2
import numpy as np
import face_recognition
import os
import streamlit as st
import streamlit.components.v1 as components 
from PIL import Image 

def app():
    st.markdown("""
    <style>
    .big-font {
        font-size:130px !important;
        text-align:center;
    }
    .small-font{
        font-size:40px;
        font-style:Times New Roman;
        text-align:center;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3,2,3])

    with col1:
        st.write("")

    with col2:
        st.image("images\heading.jpeg") #center-align the image

    with col3:
        st.write("")

    col1, col2, col3 = st.columns([0.5,7,0.5])
    with col1:
        st.write(" ")

    with col2:
        st.markdown('<p class="big-font">Find ME</p>', unsafe_allow_html=True)
        st.markdown('<p class="small-font">Find your lost one</p>', unsafe_allow_html=True)

    with col3:
        st.write(" ") 

    st.write(" ") 
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    @st.cache
    def load_image(image_file):
        img=Image.open(image_file)
        return img 

    st.markdown("""
    <style>
    .font{
        font-size:50px;
        font-style:Times New Roman;
        text-align:center;
    }
    .form{
        font-size:30px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="font"> Upload details</p>', unsafe_allow_html=True) #heading

    st.text("") #insert line break
    st.text("")
    col1, col2, col3 = st.columns([7,1,5])
    with col1:
        st.image("images\left.png") 
    
    with col2:
        st.text("")
         
    with col3:
        st.image("images\leaf.png")

    st.text("")
    st.text("")

    st.markdown('<p class="form"> Upload details of the Missing Person </p>', unsafe_allow_html=True) #sub-heading

    name, age = st.columns([5,2]) #create a form from scratch
    with name:
        firstName= st.text_input('Name', value="", key=None, type="default", help='Type complete name') 
    
    with age:
        st.number_input('Age', help='Age of the missing person', value= 1, step=1)

    st.text("")

    gender, complexion,height = st.columns([3,3,3])
    with gender:
        option = st.selectbox('Gender', ('Male', 'Female', 'Other'), help='Specify gender of the missing person')

    with complexion:
        st.text_input('Complexion', value="", key=None, type="default", help='Specify skin color of the missing person') 
         
    with height:
        st.text_input('Height (in inches)', value="", key=None, type="default", help='Specify height of missing person in inches')   

    st.text("")

    place,date,time = st.columns([3,3,3])
    with place:
        st.text_input('Missing from (Place)', value="", key=None, type="default", help='The person was last seen at which place') 
    
    with date:
        st.date_input('Missing from (Date)', value=None, min_value=None, max_value=None, key=None, help='The person was last seen on which date')

    with time:
        st.time_input('Missing since (Time)', value=None, key=None, help='The person was last seen on what time')  
    
    st.text("")

    filepath = st.file_uploader("Upload missing person's image",type=['png','jpeg','jpg'])
    st.text("")
    st.text("")
    if filepath is not None: #create a sub folder to take image input inside already existing folder. Name of the sub folder = name of missing person
        file_details = {"FileName":firstName,"FileType":filepath.type}
        img = load_image(filepath)
        st.image(img,width=250)
        subfolder_name = firstName
        os.makedirs(os.path.join('test_images', subfolder_name))

        path = os.path.join('test_images',subfolder_name, firstName)
        with open(path, "wb") as f: 
            f.write(filepath.getbuffer())         
        st.success("Saved File")

    st.text("")
    st.text("")

    st.markdown('<p class="form"> Upload your details</p>', unsafe_allow_html=True) #sub-heading

    st.text_input('Name', value="", key=None, type="default", help='Type your complete name')
    st.text("") 

    number, relation = st.columns([3,3])
    with number:
        st.text_input('Contact Number', value="", key=None, type="default", help='Specify your contact number') 

    with relation:
        st.text_input('Your relation with the person', value="", key=None, type="default", help='What is your relation with the missing person') 

    st.write("")
    st.write("")

    result = st.button("Submit")
    if result:
        st.write("Form submitted successfully. Please wait.") 
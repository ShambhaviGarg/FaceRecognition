import streamlit as st
from multiapp import MultiApp
from apps import home, form,findMe, about, contact # importing all app modules 
from PIL import Image

#PROGRAM TO COMBINE ALL THE PAGES OF THE APP

icon  = Image.open("images\heading.jpeg")
st.set_page_config(page_title='Find ME', page_icon = icon) #to set title and icon of webpage

hide_menu_style = """
    <style> 
    #MainMenu {visibility: hidden;}
    footer{visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)  #hide the watermarks provided by default by streamlit

app = MultiApp()

from streamlit_option_menu import option_menu
with st.sidebar:
    selected =option_menu(
        menu_title=None,
        options=["Home", "Fill the form", "Find Me", "About Us", "Contact"],
        icons=["house","book","envelope"],
        menu_icon="cast",
        default_index=0,
)

if selected == "Home":
    app.add_app("Home", home.app)
    app.run()
    
# if selected == "Fill the form":
#     app.add_app("Fill the form", form.app)
#     app.run()
    
if selected == "Find Me":
    app.add_app("Finding the missing", findMe.app)
    app.run()

if selected == "About Us":
    app.add_app("About US", about.app)
    app.run()

if selected == "Contact":
    app.add_app("Contact information", contact.app)
    app.run()



 

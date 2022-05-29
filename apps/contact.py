import streamlit as st

def app():
    st.title("Contact US")
    st.write("")
    st.write("") 
    col1, col2 = st.columns([3,4])

    with col1:
        st.image("images\Screenshot (197).png")

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        url = "https://mail.google.com/mail/u/0/#inbox?compose=new"
        st.write("EMail id: [shambhavigarg22@gmail.com](%s)" % url)
        st.write("Contact Number: 9999999999")


    

        






   

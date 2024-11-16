import streamlit as st
import requests


def information(email):
    print(f'The text_input_value is : {email}')
    requests.get('http://127.0.0.1:5000/get_user_by_email', params={"email": email})


if __name__ == '__main__':
    st.header("Information system")
    title = st.text_input(label="Email", placeholder="example@gmail.com")
    st.button("Submit", on_click=lambda: information(title))
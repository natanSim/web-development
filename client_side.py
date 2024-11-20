import streamlit as st
import requests


def user_data(user_email, user_name, user_last_name, user_age, id_of_user):
    print(f'The email is : {email}\n'
          f'the name is: {user_name}\n'
          f'the last_name is: {user_last_name}\n'
          f'the age is: {user_age}\n'
          f'the user_id is: {id_of_user}\n')
    requests.get('http://127.0.0.1:5000/get_user_by_information', params={"email": user_email, "name": user_last_name,
                                                                          "last_name": last_name, "age": user_age,
                                                                          "user_id": id_of_user})


if __name__ == '__main__':
    st.header("Information system")
    email = st.text_input(label="Email", placeholder="example@gmail.com")
    name = st.text_input(label="Name", placeholder="Israel")
    last_name = st.text_input(label="Last name", placeholder="Israeli")
    age = st.text_input(label="Age", placeholder="18")
    user_id = st.text_input(label="Id", placeholder="Numbers from 1 to 9", help='id: 123456789')
    st.button("Submit", on_click=lambda: user_data(email, name, last_name, age, user_id))

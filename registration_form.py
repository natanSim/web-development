import streamlit as st
import requests
from streamlit.elements import form


def registration_form(user_email, user_name, user_last_name, user_age, id_of_user):
    print(f'The email is : {email}\n'
          f'the name is: {user_name}\n'
          f'the last_name is: {user_last_name}\n'
          f'the age is: {user_age}\n'
          f'the user_id is: {id_of_user}\n')
    requests.get('http://127.0.0.1:5000/registration_form', params={"email": user_email, "name": user_name,
                                                                    "last_name": user_last_name, "age": user_age,
                                                                    "user_id": id_of_user})


if __name__ == '__main__':
    st.title("Registration form")

    with st.form(key='Registration form', clear_on_submit=True):
        email = st.text_input(label="Email", placeholder="example@gmail.com")
        name = st.text_input(label="Name", placeholder="Israel")
        last_name = st.text_input(label="Last name", placeholder="Israeli")
        age = st.text_input(label="Age", placeholder="18")
        user_id = st.text_input(label="Id", placeholder="Numbers from 1 to 9", help='id: 123456789')
        submit = st.form_submit_button("Submit")

        if submit:
            registration_form(email, name, last_name, age, user_id)
            st.write('The form was successfully received')
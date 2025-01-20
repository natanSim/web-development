import datetime
import streamlit as st
import requests


def is_length_more_thane_zero(value):
    if len(value) > 0:
        print('correct')
        return True

    print('incorrect')
    st.error('This is an error(You need write somthing)', icon="🚨")

    return False


def is_type_string(value):
    if value.isalpha():
        print('correct')
        return True

    print('incorrect')
    st.error('This is an error(Name and Last Name should contain only letters)', icon="🚨")

    return False


def is_type_int(value):
    if value.isdigit() and len(value) > 0:
        print("correct")
        return True

    print('incorrect')
    st.error('This is an error(Phone number and ID should contain only numbers)', icon="🚨")

    return False


def is_registration_fields_valid(user_first_name, user_last_name, user_date, user_text):
    user_first_name_valid_flag = is_type_string(user_first_name)
    user_last_name_valid_flag = is_type_string(user_last_name)
    user_text_valid_flag = is_length_more_thane_zero(user_text)

    if all([user_first_name_valid_flag,
            user_last_name_valid_flag, user_text_valid_flag]):

        print(
              f'First Name: {user_first_name}\n'
              f'Last Name: {user_last_name}\n'
              f'Date: {user_date}\n'
              f'Text: {user_text}\n')

        return True

    return False


def send_to_server(user_first_name, user_last_name, date, user_text):
    try:
        requests.get('http://127.0.0.1:5000/writeText', params={
                                                                        "first_name": user_first_name,
                                                                        "last_name": user_last_name,
                                                                        "date": date,
                                                                        "user_text": user_text})
        print("Mission Accomplished")
        return True

    except ConnectionError as error:
        print(f'Server error. message - {error}')
        return "Mission Unaccomplished"


def main():
    st.title("Text task")
    name = st.text_input(label="Name", placeholder="Israel")
    last_name = st.text_input(label="Last name", placeholder="Israeli")
    date = st.date_input(label="Date of today")
    text = st.text_area('Write here your text task')

    st.write(f"You wrote {len(text.split())} words")

    clear_on_submit = ''
    with st.form(key='Text task', clear_on_submit=True):

        submit = st.form_submit_button("Submit")

        if submit:
            values = [name, last_name, date, text]

            if is_registration_fields_valid(*values):
                if send_to_server(*values) is True:
                    st.write('The form was successfully received')
            else:
                st.write('Form submission failed')


if __name__ == '__main__':
    main()


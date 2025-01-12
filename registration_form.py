import streamlit as st
import requests
from streamlit.elements import form


def find_email_name(user_email):
    email_name = ''

    for i in range(len(user_email)):
        print(i, user_email[i])
        if user_email[i] == '@':
            break

        email_name = email_name + user_email[i]

    return email_name


def is_contains_letters(user_email):
    email_name = find_email_name(user_email)

    if email_name.isalpha():
        return True
    else:

        return False


def is_email_valid(user_email):
    # print(f'user_email= {user_email}')

    if '@gmail.com' in user_email and len(find_email_name(user_email)) > 1 and is_contains_letters(user_email):
        print("correct")
        return True

    print('incorrect')
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
    st.error('This is an error(Age and ID should contain only numbers)', icon="🚨")

    return False


def registration_form(user_email, user_name, user_last_name, user_age, id_of_user):
    mail = is_email_valid(user_email)
    name_user = is_type_string(user_name)
    last_name_user = is_type_string(user_last_name)
    age_user = is_type_int(user_age)
    id_user = is_type_int(id_of_user)

    if mail and name_user and last_name_user and age_user and id_user:
        print(f'The email is : {email}\n'
              f'the name is: {user_name}\n'
              f'the last_name is: {user_last_name}\n'
              f'the age is: {user_age}\n'
              f'the user_id is: {id_of_user}\n')
        requests.get('http://127.0.0.1:5000/registration_form', params={"email": user_email, "name": user_name,
                                                                        "last_name": user_last_name, "age": user_age,
                                                                        "user_id": id_of_user})
        return True
    else:
        return False


    # return mail, name_user, last_name_user, age_user, id_user


if __name__ == '__main__':
    st.title("Registration form")
    clear_on_submit = ''
    with st.form(key='Registration form', clear_on_submit=True):
        email = st.text_input(label="Email", placeholder="example@gmail.com")
        name = st.text_input(label="Name", placeholder="Israel")
        last_name = st.text_input(label="Last name", placeholder="Israeli")
        age = st.text_input(label="Age", placeholder="18")
        user_id = st.text_input(label="Id", placeholder="Numbers from 1 to 9", help='id: 123456789', max_chars=9)
        submit = st.form_submit_button("Submit")

        if submit:
            if registration_form(email, name, last_name, age, user_id):
                st.write('The form was successfully received')

            else:
                st.write('Form submission failed')



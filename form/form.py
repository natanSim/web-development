import datetime
import streamlit as st
import requests



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
    st.error('This is an error(Write the valid mail)', icon="🚨")
    return False


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


def registration_form(user_email, user_name, user_last_name, user_date, id_of_user,
                      user_phone, about_user, job_question, file):
    mail = is_email_valid(user_email)
    name_user = is_type_string(user_name)
    last_name_user = is_type_string(user_last_name)
    id_user = is_type_int(id_of_user)
    phone = is_type_int(user_phone)
    about = is_length_more_thane_zero(about_user)
    question_job = is_length_more_thane_zero(job_question)

    if mail and name_user and last_name_user and user_date and id_user and phone and about and question_job:
        print(f'The email is : {email}\n'
              f'the name is: {user_name}\n'
              f'the last_name is: {user_last_name}\n'
              f'the date is: {user_date}\n'
              f'the user_id is: {id_of_user}\n'
              f'the phone is: {phone}\n'
              f'the about is: {about}\n'
              f'the question_job is: {question_job}\n'
              f'the file is: {file}\n')

        requests.get('http://127.0.0.1:5000/registrationForm', params={"email": user_email, "name": user_name,
                                                                        "last_name": user_last_name, "user_date": user_date,
                                                                        "user_id": id_of_user, 'phone_number': phone,
                                                                       "user_about": about,'question_job': question_job,
                                                                       'file': file})
        return True
    else:
        return False


if __name__ == '__main__':
    st.title("Job interview form")
    clear_on_submit = ''
    with st.form(key='Registration form', clear_on_submit=True):
        email = st.text_input(label="Email", placeholder="example@gmail.com")
        name = st.text_input(label="Name", placeholder="Israel")
        last_name = st.text_input(label="Last name", placeholder="Israeli")
        date = st.date_input(label="Date of birth", min_value=datetime.date(1919, 7, 6))
        user_id = st.text_input(label="Id", placeholder="Numbers from 1 to 9", help='id: 123456789', max_chars=9)
        phone_number = st.text_input(label="Phone number", placeholder="Numbers from 1 to 10", help='phone number: 051-11-111-11', max_chars=10)
        user_about = st.text_area('Tel us about you')
        user_question = st.text_area('why do you want this job?')
        user_file = st.file_uploader(label='upload file', accept_multiple_files = True)

        submit = st.form_submit_button("Submit")

        if submit:
            if registration_form(email, name, last_name, date, user_id, phone_number, user_about, user_question, user_file):
                st.write('The form was successfully received')

            else:
                st.write('Form submission failed')

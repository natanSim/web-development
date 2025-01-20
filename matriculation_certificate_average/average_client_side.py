import streamlit as st
import requests


def send_to_server(user_subjects, user_grades):
    try:
        requests.get('http://127.0.0.1:5000/serverAverage', params={"subject": user_subjects, "grade": user_grades})

        print("Mission Accomplished")
        return True

    except ConnectionError as error:
        print(f'Server error. message - {error}')
        return "Mission Unaccomplished"



def main():
    st.title("Calculating Grade Point Average")

    subjects = []
    grades = []

    num_subjects = st.number_input(r"$\textsf{\Large How many subjects would you like to add?}$", min_value=1, value=1)
    st.divider()

    for i in range(num_subjects):
        subject = st.text_input(f"$\\textsf{{\\Large Enter the name of the subject - {i + 1}}}$")
        grade = st.number_input((f"$\\textsf{{\\Large Enter the name of the grade {i + 1}}}$"), min_value=0, max_value=100)
        st.divider()

        subjects.append(subject)
        grades.append(grade)


    with st.form(key='Text task', clear_on_submit=True):

        submit = st.form_submit_button("Submit")

        if submit:
            values = [subjects, grades]
            if send_to_server(*values) is True:
                st.write(r"$\textsf{\Large The subjects and grades you entered:}$")
                for i in range(len(subjects)):
                    st.write(f"{subjects[i]}: {grades[i]}")

                    average_grade = sum(grades) / len(grades)
                    st.write(f"Your average is: {average_grade}")
            else:
                st.write("No grades entered")



if __name__ == "__main__":
    main()

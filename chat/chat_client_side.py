import streamlit as st
import requests


def send_to_server(user_message):
    try:
        requests.get('http://127.0.0.1:5000/chatBox', params={"user_message": user_message})

        print("Mission Accomplished")
        return True

    except ConnectionError as error:
        print(f'Server error. message - {error}')
        return "Mission Unaccomplished"


def main():
    with st.container(height=800):

        st.write(r"$\textsf{\Large Chat box}$")
        message_user = st.container(height=650)

        if 'messages' not in st.session_state:
            st.session_state['messages'] = []

        user_message = st.chat_input("Say something")

        if user_message:

            st.session_state['messages'].append(f"user: {user_message}")
        value = user_message
        if send_to_server(value) is True:
            for message in st.session_state['messages']:
                message_user.chat_message("user").write(message)


if __name__ == "__main__":
    main()

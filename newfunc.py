import streamlit as st


def functionality():
    st.title("Hello Streamlit")
    st.write("This is your first Streamlit app!")

    # Add a button
    if st.button("Click me now "):
        st.write("You clicked the button!")

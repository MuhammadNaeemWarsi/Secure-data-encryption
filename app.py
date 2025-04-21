
import streamlit as st
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text

st.title("Secure Data Encryption")
key = generate_key()
data = st.text_input("Data")

if st.button("Encrypt"):
    encrypted_data = encrypt_data(data, key)
    st.success(f"Encrypted Data: {encrypted_data}")



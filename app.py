
import streamlit as st
from cryptography.fernet import Fernet

# Generate or load a key (you can also save and reuse this securely)
@st.cache_resource
def load_key():
    return Fernet.generate_key()

key = load_key()
fernet = Fernet(key)

st.title("🔐 Secure Data Encryption App")

menu = st.sidebar.selectbox("Choose an option", ["Encrypt", "Decrypt"])

if menu == "Encrypt":
    st.subheader("🔏 Encrypt Your Message")
    user_input = st.text_area("Enter the text to encrypt:")

    if st.button("Encrypt"):
        if user_input:
            encrypted = fernet.encrypt(user_input.encode())
            st.success("Encrypted Data:")
            st.code(encrypted.decode())
        else:
            st.warning("Please enter text to encrypt.")

elif menu == "Decrypt":
    st.subheader("🔓 Decrypt Your Message")
    encrypted_input = st.text_area("Enter the encrypted text:")

    if st.button("Decrypt"):
        try:
            decrypted = fernet.decrypt(encrypted_input.encode()).decode()
            st.success("Decrypted Data:")
            st.code(decrypted)
        except Exception as e:
            st.error(f"Decryption failed: {str(e)}")



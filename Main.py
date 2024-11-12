import streamlit as st
import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute(
    """CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT
             )"""
)
conn.commit()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def add_user(username, password):
    hashed_password = hash_password(password)
    c.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, hashed_password),
    )
    conn.commit()


def verify_user(username, password):
    hashed_password = hash_password(password)
    c.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, hashed_password),
    )
    return c.fetchone() is not None


st.title("User Authentication")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.subheader("Register or Login")

    option = st.selectbox("Choose Action", ["Register", "Login"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if option == "Register":
        if st.button("Register"):
            if username and password:
                try:
                    add_user(username, password)
                    st.success("Registration successful! Please login to continue.")
                except sqlite3.IntegrityError:
                    st.error(
                        "Username already exists. Please choose a different username."
                    )
            else:
                st.error("Please enter both a username and password.")

    elif option == "Login":
        if st.button("Login"):
            if verify_user(username, password):
                st.success("Login successful!")
                st.session_state.authenticated = True
            else:
                st.error("Invalid username or password.")

# Main Encryption/Decryption Interface
if st.session_state.authenticated:
    st.title("Encryption and Decryption Tool")

    Val = {
        "A": 0.1,
        "B": 0.2,
        "C": 0.3,
        "D": 0.4,
        "E": 0.5,
        "F": 0.6,
        "G": 0.7,
        "H": 0.8,
        "I": 0.9,
        "J": 0.01,
        "K": 0.02,
        "L": 0.03,
        "M": 0.04,
        "N": 0.05,
        "O": 0.06,
        "P": 0.07,
        "Q": 0.08,
        "R": 0.09,
        "S": 0.001,
        "T": 0.002,
        "U": 0.003,
        "V": 0.004,
        "W": 0.005,
        "X": 0.006,
        "Y": 0.007,
        "Z": 0.008,
        " ": 0.009,
    }

    def encryption(message, key):
        encrypted_message = []

        message = message.upper()
        key = key.upper()

        extended_key = (key * ((len(message) // len(key)) + 1))[: len(message)]

        for i in range(len(message)):
            if message[i] in Val:
                if message[i] == " ":
                    encrypted_message.append(Val[" "])
                else:
                    message_char = message[i]
                    key_char = extended_key[i]
                    shift_value = (
                        ord(message_char) - ord("A") + (ord(key_char) - ord("A"))
                    ) % 26
                    encrypted_char = chr(shift_value + ord("A"))
                    encrypted_message.append(Val[encrypted_char])
            else:
                encrypted_message.append(message[i])

        return encrypted_message

    def decryption(encrypted_message, key):
        decrypted_message = []

        key = key.upper()

        encrypted_digits = list(map(float, encrypted_message.split(",")))

        reverse_val = {v: k for k, v in Val.items()}

        extended_key = (key * ((len(encrypted_digits) // len(key)) + 1))[
            : len(encrypted_digits)
        ]

        for i in range(len(encrypted_digits)):
            if encrypted_digits[i] in reverse_val:
                encrypted_char = reverse_val[encrypted_digits[i]]
                if encrypted_char == " ":
                    decrypted_message.append(" ")
                else:
                    key_char = extended_key[i]
                    shift_value = (
                        ord(encrypted_char) - ord("A") - (ord(key_char) - ord("A"))
                    ) % 26
                    decrypted_char = chr(shift_value + ord("A"))
                    decrypted_message.append(decrypted_char)

        return "".join(decrypted_message)

    option = st.selectbox("Select an option:", ("Encryption", "Decryption"))

    if option == "Encryption":
        message = st.text_input("Enter the message to be encrypted:")
        key = st.text_input("Enter the encryption key:")
        if st.button("Encrypt"):
            if message and key:
                encrypted_message = encryption(message, key)
                encrypted_message_str = ", ".join(map(str, encrypted_message))
                st.success("Encrypted Message: " + encrypted_message_str)
            else:
                st.error("Please provide both a message and a key.")

    elif option == "Decryption":
        encrypted_message = st.text_input(
            "Enter the encrypted message (comma-separated digits):"
        )
        key = st.text_input("Enter the decryption key:")
        if st.button("Decrypt"):
            if encrypted_message and key:
                decrypted_result = decryption(encrypted_message, key)
                st.success("Decrypted Message: " + decrypted_result)
            else:
                st.error("Please provide both an encrypted message and a key.")

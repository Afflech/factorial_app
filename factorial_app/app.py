import streamlit as st
from factorial import fact
import os


def load_users():
    try:
        if os.path.exists("user.txt"):
            with open("user.txt", "r", encoding = "utf-8") as f:
                users = [line.strip() for line in f.readlines() if
                         line.strip()]
            return users
        else:
            st.error("File user.txt ko ton tai")
            return []
        
    except Exception as e:
        st.error(f"Loi khi doc file user.txt")
        return []
    
def login_page():
    st.title("Dang nhap")

    username = st.text_input("Nhap username")

    if st.button("Dang nhap"):
        if username:
            users = load_users()
            if username in users:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            
            else:
                st.session_state.show_greeting = True
                st.session_state.username = username
                st.rerun()

        else:
            st.warning("Vui long nhap ten nguoi dung")

def factorial_calculator():
    st.tilte("Factorial Calculator")
    st.write(f"Xin chao, {st.session_state.username}")

    if st.button("Dang xuat"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
    
    st.divider()

    #Chuc nang tinh giai thua 

    number = st.number_input("Nhap so ban can tinh giai thua:", 
                             min_value = 0, 
                             max_value = 1000)
    
    if st.button("Tinh giai thua"):
        res = fact(number)
        st.write("Ket qua giai thua cua {number} la: {res}")

def greeting_page():
    st.title("Xin chao")
    st.write(f"Xin chao {st.session_state.username}")
    st.write("Ban khong co quyen truy cap vao chuc nang giai thua")

    if st.button("Quay lai dang nhap"):
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if 'username' not in st.session_state:
        st.session_state.username = ""

    if 'show_greeting' not in st.session_state:
        st.session_state.show_greeting = False

    if st.session_state.logged_in:
        factorial_calculator()
    
    elif st.session_state.show_greeting:
        greeting_page()

    else:
        login_page()

if __name__ == "__main__":
    main()


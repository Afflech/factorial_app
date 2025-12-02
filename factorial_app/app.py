import streamlit as st
from factorial import fact

def main():
    st.title("Factorial Calculator")
    number = st.number_input("Enter a number", 
                             min_value = 0, 
                             max_value = 1000)

    if st.button("Calculate"):
        res = fact(number)
        st.write(f"The factorial of number you pressed is {res}")

if __name__ == "__main__":
    main()

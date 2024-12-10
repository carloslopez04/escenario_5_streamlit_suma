import streamlit as st

st.write("**Simulador de calculadora**")
st.write("Ingrese los valores a sumar")
a = st.number_input("Primer número")
b = st.number_input("Segundo número")
resultado = st.write(f"El resultado de la suma es: {a + b}")
if resultado:
    st.write("El resultado es: ", resultado)
import streamlit as st
from math import comb

st.title("Special Card Draw Probability Calculator")

# User inputs
N = st.number_input("Number of cards in deck", min_value=1, value=60)
x = st.number_input("Number of special card copies", min_value=1, value=4)
k = st.number_input("Number of cards drawn", min_value=1, value=2)

# Calculation
if N - x >= k:
    total_combinations = comb(N, k)
    fail_combinations = comb(N - x, k)
    success_probability = 1 - fail_combinations / total_combinations
    st.success(f"Probability of drawing at least one special card: {success_probability*100:.2f}%")
else:
    st.warning("You are drawing more cards than non-special ones: probability 100%")

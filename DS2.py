import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write('This App predicts the Iris flower type !')

st.siderbar.header('User Input Parameters')

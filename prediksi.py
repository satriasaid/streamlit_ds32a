import requests
import joblib #library untuk menyimpan prediksi terbaik
import os
import streamlit as st
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from numerize import numerize

def prediksi():
    imdb_joblib = joblib.load('imdb_joblib')
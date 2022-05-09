import numpy as np
import pandas as pd
import pickle
import streamlit as st
import base64
from PIL import Image
import sklearn
model = pickle.load(open('sentiment_analysis_model.pkl','rb'))

st.set_page_config(page_title="Sentiment Analysis Web App",page_icon="",layout="centered",initial_sidebar_state="expanded")
st.title('Amazon Review Sentiment Analysis')
st.subheader('The Review from the user predicts if the sentiment of the text is positive or negative')

st.subheader('Enter Text')
message = st.text_area("","")
if st.button('PREDICT'):
  disp=""
  a=model.predict([message])[0]
  if(a== 'pos'):
        disp = "Positive Review!"
  else:
        disp = "Negative Review!"
  st.header(f"**{a}**")
 
  prediction = model.predict([message])

  
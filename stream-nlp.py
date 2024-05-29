import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# load save model
model_fraud = pickle.load(open('model_fraud.sav','rb'))

tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("new_selected_feature_tf-idv.sav", "rb"))))

# judul halaman
st.title ('Deteksi SMS Penipuan SCAMSAFE')

# Display an image
st.image('logo.png', use_column_width=False, width=200)

clean_teks = st.text_input('Masukkan Teks SMS')

fraud_detection = ''

if st.button('Hasil Deteksi'):
    predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))
    
    if (predict_fraud == 0):
        fraud_detection = 'SMS Normal'
    elif (predict_fraud == 1):
        fraud_detection = 'SMS Penipuan'
    else :
        fraud_detection = 'SMS Promo'

st.success(fraud_detection)

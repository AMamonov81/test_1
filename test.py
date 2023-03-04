import streamlit as st
import pickle


def load():
    with open ("model.pcl", "rb") as fid:
        return pickle.load(fid)


age = st.slider('Возраст, дней', 0, 43800, key='age')
gender = st.slider('Пол', 1, 2, key='gender')
height = st.slider('Рост', 50, 250, key='height')
weight = st.slider('Вес', 30, 300, key='weight')
ap_hi = st.slider('АД, сист', 30, 300, key='ap_hi')
ap_lo = st.slider('АД, диаст', 30, 300, key='ap_lo')
cholesterol = st.slider('Холестерин', 1, 3, key='cholesterol')
gluc = st.slider('Глюкоза', 1, 3, key='gluc')
smoke = st.checkbox('Курение', key='smoke')
alco = st.checkbox('Алкоголь', key='alco')
active = st.checkbox('Активный образ жизни', key='active')



model = load()
y_pr = model.predict_proba([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]])[:, 1]

st.write(y_pr)
if weight/(height/100) > 30:
    st.write('Для снижения риска сердечной патологии необходимо снизить массу тела')

if ap_hi > 140:
    st.write('Необходимо обратиться к терапевту для подбора гипотензивной терапии')

if gluc >= 2:
    st.write('Необходимо обратиться к терапевту по поводу гипергликемии')

if smoke == 1:
    st.write('Рекомендуется бросить курить')

if alco == 1:
    st.write('Рекомендуется снизить потребление алкоголя')

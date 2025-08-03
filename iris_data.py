import streamlit as st
import pickle
import numpy as np


with open("knn_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)


iris_class_names = ['setosa', 'versicolor', 'virginica']

st.title(" Iris Flower Classifier using KNN")
st.write("Enter features  of the Iris flower species.")


sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal width (cm)", 2.0, 4.5, 3.6)
petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 0.2)


features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

prediction = loaded_model.predict(features)[0]
species = ['Setosa', 'Versicolor', 'Virginica'][prediction]
#predicted_class = iris_class_names[prediction]


st.subheader("Prediction:")
st.success(f"The predicted Iris class is **{species}**.")




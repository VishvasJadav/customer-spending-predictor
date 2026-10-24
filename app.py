# streamlit UI
import pickle
import pandas as pd
import streamlit as st

#page setup
st.set_page_config(page_title="Customer Spending Prediction",
                   page_icon="assest/images.png")

#sidebar
with st.sidebar:
    st.title("Customer Spending Prediction")
    st.image("assest/images.png")

#load the model (model deserialization)
with open("best_model/best_model_pipeline.pkl","rb") as f:
    best_pipeline = pickle.load(f)

#user input fields
with st.container(border = True):
        col1,col2= st.columns(2)
#load the dataset
df = pd.read_csv("Datasets/cleaned_data.csv")

with col1:
    Age=st.number_input("Age",min_value=1,max_value=100)
    Annual_Income=st.number_input("Annual Income",min_value=100000,max_value=6000000)
    Website_Visits=st.number_input("Website Visits",min_value=1)
    Previous_Purchases=st.number_input("Previous Purchases")

with col2:
    Membership_Type=st.selectbox("Membership Type",options=df["Membership_Type"].unique())
    Preferred_Category=st.selectbox("Preferred Category",options=df["Preferred_Category"].unique())
    City_Tier=st.selectbox("City Tier",options=df["City_Tier"].unique())
    Discount_Used=st.number_input("Discount Used",min_value=0,max_value=100)

new_data = {
    'Age':Age,
    'Annual_Income':Annual_Income,
    'Website_Visits':Website_Visits,
    'Previous_Purchases':Previous_Purchases,
    'Membership_Type':Membership_Type,
    'Preferred_Category':Preferred_Category,
    'City_Tier':City_Tier,
    'Discount_Used':Discount_Used
}

new_data = pd.DataFrame(new_data,index=[0])

if st.button("Predict spend"):
    prediction = best_pipeline.predict(new_data)[0]
    st.success(f"Predicted Spend: {prediction[0]:.2f} Rs.")
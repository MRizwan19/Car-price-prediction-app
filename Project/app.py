import streamlit as st
import pandas as pd
import pickle 

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
st.image(r'C:\Users\devel\Documents\Car-price-prediction-app\Project\cars_cover.webp', use_container_width=True)
st.title("Car Price Predictor")

st.markdown("""
This app predicts the price of a car you want to sell. Try filling the details below:
""")

company = st.selectbox("Select the company:", 
                       ['Honda','Maruti', 'Hyundai', 'Toyota', 'Ford', 'BMW', 'Mercedes', 'Audi', 'Volkswagen', 'Tata', 'Other'])

name = st.text_input("Enter the model name (e.g., Honda City):", value="")

year = st.slider("Select Year of Purchase:", 1995, 2025, step=1, value=2019)

fuel_type = st.selectbox("Select the Fuel Type:", ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])

kms_driven = st.number_input("Enter the Number of Kilometers the car has travelled:", min_value=0, step=1)

if st.button("Predict Price"):
    input_data = pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                              columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
    try:
        predicted_price_inr = model.predict(input_data)[0]

        exchange_rate = 86.96  # 1 USD = 86.96 INR 
        predicted_price_usd = predicted_price_inr / exchange_rate

        st.success(f"The predicted price for the car is: ${predicted_price_usd:,.2f}")
    except Exception as e:
        st.error(f"Error: {str(e)}. Please ensure the input values are valid.")

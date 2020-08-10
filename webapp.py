import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('delhi_house_price_model.pickle', 'rb'))

columns = ['Area', 'BHK', 'Bathroom', 'Furnishing', 'Budh Vihar',
       'Budh Vihar Phase 1', 'Chhattarpur', 'Chhattarpur Enclave Phase2',
       'Chittaranjan Park', 'Commonwealth Games Village 2010',
       'Dilshad Garden', 'Dwarka', 'Dwarka Mor', 'Dwarka Sector 12',
       'Greater Kailash', 'Hauz Khas', 'Kalkaji', 'Karol Bagh', 'Kirti Nagar',
       'Lajpat Nagar', 'Lajpat Nagar 2', 'Lajpat Nagar 3', 'Laxmi Nagar',
       'Mahavir Enclave', 'Mahavir Enclave Part 1', 'Malviya Nagar',
       'Mathura Road', 'Mehrauli', 'Narela', 'New Friends Colony', 'Okhla',
       'Other', 'Paschim Vihar', 'Patel Nagar', 'Patel Nagar West',
       'Punjabi Bagh', 'Punjabi Bagh West', 'Rohini Sector 23',
       'Rohini Sector 24', 'Safdarjung Enclave', 'Saket', 'Shahdara',
       'Sheikh Sarai', 'Sheikh Sarai Phase 1', 'Sultanpur', 'Uttam Nagar',
       'Uttam Nagar West', 'Vasant Kunj', 'Vasundhara Enclave',
       'Property_Type']

columns = np.array([columns])
columns = columns.astype('object')

def predict_price(area, bhk, bathroom, furnishing, locality, property_type): 
    loc_index = np.where(columns==locality)[1][0]

    x = np.zeros(50)
    x[0] = area
    x[1] = bhk
    x[2] = bathroom
    if x[3] == 'Furnished':
        x[3] = 2
    elif x[3] == 'Semi - Furnished':
        x[3] = 1
    else:
        x[3] = 0
    if loc_index >= 0:
        x[loc_index] = 1
    if x[49] == 'New_Property':
        x[49] = 1
    else:
        x[49] = 0

    return int(round(model.predict([x])[0], -5))


def main():

    st.title('Delhi House Price Prediction')
    st.write('Select the parameters to predict the house price')
    
    st.title('House Area')
    area = st.number_input('Enter the House Area')
    
    st.title('BHK')
    bhk = st.number_input('Enter the number of Bedrooms')
    
    st.title('Bathroom')
    bathroom = st.number_input('Enter the number of Bathrooms')
    
    st.title('Furnishing')
    furnishing = st.selectbox('Type of Furnishing', ['Furnished', 'Semi-Furnished', 'Unfurnished'])
    
    st.title('Locality')
    locality = st.selectbox('Select the Location', ['Budh Vihar',
       'Budh Vihar Phase 1', 'Chhattarpur', 'Chhattarpur Enclave Phase2',
       'Chittaranjan Park', 'Commonwealth Games Village 2010',
       'Dilshad Garden', 'Dwarka', 'Dwarka Mor', 'Dwarka Sector 12',
       'Greater Kailash', 'Hauz Khas', 'Kalkaji', 'Karol Bagh', 'Kirti Nagar',
       'Lajpat Nagar', 'Lajpat Nagar 2', 'Lajpat Nagar 3', 'Laxmi Nagar',
       'Mahavir Enclave', 'Mahavir Enclave Part 1', 'Malviya Nagar',
       'Mathura Road', 'Mehrauli', 'Narela', 'New Friends Colony', 'Okhla',
       'Paschim Vihar', 'Patel Nagar', 'Patel Nagar West',
       'Punjabi Bagh', 'Punjabi Bagh West', 'Rohini Sector 23',
       'Rohini Sector 24', 'Safdarjung Enclave', 'Saket', 'Shahdara',
       'Sheikh Sarai', 'Sheikh Sarai Phase 1', 'Sultanpur', 'Uttam Nagar',
       'Uttam Nagar West', 'Vasant Kunj', 'Vasundhara Enclave', 'Other'])
    
    st.title('Property Type')
    property_type = st.selectbox('Type of Property', ['New_Property', 'Resale'])
    
    if st.button("Predict"):
        output=predict_price(area, bhk, bathroom, furnishing, locality, property_type)
        st.success('The predicted house price is {}'.format(output))
        
if __name__ == '__main__':
    main()
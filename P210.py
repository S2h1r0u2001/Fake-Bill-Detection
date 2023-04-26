

import pickle
import streamlit as st


load = open('mod.pkl','rb')
model = pickle.load(load)

def predict(diagonal, height_left, height_right, margin_low, margin_up, length):
    prediction = model.predict([[diagonal, height_left, height_right, margin_low, margin_up, length]])
    return prediction

def main():
    st.title('Fake-Bill Detection')
    
    diagonal= st.number_input('Diagonal :')
    height_left= st.number_input('Height_left :')
    height_right = st.number_input('Height_right :')
    margin_low = st.number_input('Margin_low:')
    margin_up = st.number_input('Margin_up :')
    length = st.number_input('Length :')
    
    if st.button('Predict'):
        result = predict(diagonal, height_left, height_right, margin_low, margin_up, length)
        st.success('The Bill is genuine : {}'.format(result))

        

if __name__== '__main__':
    main()
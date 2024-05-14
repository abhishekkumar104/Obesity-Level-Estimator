import streamlit as st
import pickle
import numpy as np


pipe = pickle.load(open('pipe.pkl','rb'))

st.title("Obesity Level Estimator")

gender=st.radio("Gender ",["Female","Male"],index=None)
age=st.number_input("Age: ",min_value=5.,max_value=100.,value=None)
ht=st.number_input("Height: ",min_value=1.,max_value=2.75,value=None )
wt = st.number_input("Weight: ",min_value=10.,max_value=173.,value =None )
family_history_with_overweight=st.radio("Family history with Overweight ",['yes','no'],index=None)
favc=st.selectbox("Do you eat high caloric food frequently? ",['no','yes'],index=None)
fcvc=st.number_input("How many vegetables do you usually eat  in your meals?",min_value=1.,max_value=3.,value=None,placeholder="enter a number between 1 and 3(both inclusive)")
ncp=st.number_input("How many main meals do you have daily?",min_value=1.,max_value=4.,value=None,placeholder="enter an number between 1 and 4(both inclusive)")
caec=st.selectbox("Do you eat any food between meals? ",['Sometimes', 'Frequently', 'Always', 'no'],index=None)
smoke=st.selectbox("Do you smoke? ",['no', 'yes'],index=None)
ch2o=st.number_input("How much water do you drink daily? (in litres)",min_value=0.,max_value=5.,value=None)
scc=st.selectbox("Do you monitor the calories you eat daily? ",['no','yes'],index=None)
faf=st.number_input("How often do you have physical activity? ",min_value=0.,max_value=3.,value=None,placeholder="enter the exercise hour between 0 and 3(both inclusive)")
tue=st.number_input("How much time(in hours) do you use technological devices such as cell phone, videogames, television, computer and others?",min_value=0.,max_value=18.,value=None)
calc=st.selectbox("How often do you drink alcohol?",['no', 'Sometimes', 'Frequently', 'Always'],index=None)
mtrans=st.selectbox("Which transportation do you usually use? ",['Public_Transportation', 'Walking', 'Automobile', 'Motorbike', 'Bike'],index=None)
if st.button("Predict"):
    input_feature= []
    input_feature.append(gender)
    input_feature.append(age)
    input_feature.append(ht)    
    input_feature.append(wt)
    input_feature.append(family_history_with_overweight)
    input_feature.append(favc)
    input_feature.append(fcvc)
    input_feature.append(ncp)
    input_feature.append(caec)
    input_feature.append(smoke)
    input_feature.append(ch2o)
    input_feature.append(scc)
    input_feature.append(faf)
    input_feature.append(tue)
    input_feature.append(calc)
    input_feature.append(mtrans)

    vector_input = np.array(input_feature).reshape(1,16)
    result=pipe.predict(vector_input)[0]
    if result==0:
        st.header("Insufficient Weight")
    elif result==1:
        st.header("Normal Weight")
    elif result==2:
        st.header("Obesity Type I")
    elif result==3:
        st.header("Obesity Type II")
    elif result==4:
        st.header("Obesity Type III")
    elif result==5:
        st.header("Overweight Level I")
    elif result==6:
        st.header("Overweight Level II")
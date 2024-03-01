import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

df=pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')
df['Gender']=pd.factorize(df.Gender)[0]
df['family_history_with_overweight']=pd.factorize(df.family_history_with_overweight)[0]
df['FAVC']=pd.factorize(df.FAVC)[0]
df['CAEC']=pd.factorize(df.CAEC)[0]
df['SMOKE']=pd.factorize(df.SMOKE)[0]
df['SCC']=pd.factorize(df.SCC)[0]
df['CALC']=pd.factorize(df.CALC)[0]
df['MTRANS']=pd.factorize(df.MTRANS)[0]
df['NObeyesdad']=pd.factorize(df.NObeyesdad)[0]

df=df.drop_duplicates(keep='first')
feature=df.iloc[:,:-1]
target=df.iloc[:,-1]

scaler=StandardScaler()
scaler.fit(feature)
standardized_data=scaler.transform(feature)
feature=standardized_data
model=pickle.load(open('model.pkl','rb'))

st.title("Obesity Level Estimator")
gender=st.radio("Gender ",["Female","Male"])
age=st.number_input("Age: ",min_value=14.,max_value=61.)
ht=st.number_input("Height: ",min_value=1.45,max_value=2.00)
wt=st.number_input("Weight: ",min_value=39.,max_value=173.)
family_history_with_overweight=st.radio("Family history with Overweight ",['Yes','No'])
favc=st.selectbox("Do you eat high caloric food frequently? ",['No','Yes'])
fcvc=st.slider("How many vegetables do you usually eat  in your meals?",1.,3.)
ncp=st.slider("How many main meals do you have daily?",1.,4.)
caec=st.selectbox("Do you eat any food between meals? ",['Sometimes', 'Frequently', 'Always', 'no'])
smoke=st.selectbox("Do you smoke? ",['No', 'Yes'])
ch2o=st.slider("How much water do you drink daily? ",1.,3.)
scc=st.selectbox("Do you monitor the calories you eat daily? ",['No','Yes'])
faf=st.number_input("How often do you have physical activity? ",0.,3.)
tue=st.slider("How much time do you use technological devices such as cell phone, videogames, television, computer and others?",0.,2.)
calc=st.selectbox("How often do you drink alcohol?",['No', 'Sometimes', 'Frequently', 'Always'])
mtrans=st.selectbox("Which transportation do you usually use? ",['Public_Transportation', 'Walking', 'Automobile', 'Motorbike', 'Bike'])
if st.button("Predict"):
    input=[]
    if gender=="Female":
        gender=0
    else:
        gender=1
    input.append(gender)
    input.append(age)
    input.append(ht)
    input.append(wt)
    if family_history_with_overweight=='Yes':
        family_history_with_overweight=0
    else:
        family_history_with_overweight=1
    input.append(family_history_with_overweight)
    if favc=="No":
        favc=0
    else:
        favc=1
    input.append(favc)
    input.append(fcvc)
    input.append(ncp)
    if caec=="Sometimes":
        caec=0
    elif caec=='Frequently':
        caec=1
    elif caec=='Always':
        caec=2
    else:
        caec=3
    input.append(caec)
    if smoke=="No":
        smoke=0
    else:
        smoke=1
    input.append(smoke)
    input.append(ch2o)
    if scc=="No":
        scc=0
    else:
        scc=1
    input.append(scc)
    input.append(faf)
    input.append(tue)
    if calc=="No":
        calc=0
    elif calc=="Sometimes":
        calc=1
    elif calc=="Frequently":
        calc=2
    else:
        calc=3
    input.append(calc)
    if mtrans=='Public_Transportation':
        mtrans=0
    elif mtrans=='Walking':
        mtrans=1
    elif mtrans=='Automobile':
        mtrans=2
    elif mtrans=="Motobike":
        mtrans=3
    else:
        mtrans=4
    input.append(mtrans)
    input_as_np_array=np.asarray(input)
    reshaped_input=input_as_np_array.reshape(1,-1)
    standard_input=scaler.transform(reshaped_input)
    result=model.predict(standard_input)[0]
    if result==0:
        st.header("Normal Weight")
    elif result==1:
        st.header("Overweight Level I")
    elif result==2:
        st.header("Overweight Level II")
    elif result==3:
        st.header("Obesity Type I")
    elif result==4:
        st.header("Insufficient Weight")
    elif result==5:
        st.header("Obesity Type II")
    else:
        st.header("Obesity Type III")
    
    
    
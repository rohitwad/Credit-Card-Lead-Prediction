#!/usr/bin/env python
# coding: utf-8

# In[4]:
import numpy as np
from flask import Flask, request, render_template
import pickle
from pickle import load



# In[5]:
app=Flask(__name__)
# load the model
model = load(open('Logistic_CCLP.pkl', 'rb'))
# load the scaler
scaler = load(open('scaler_CCLP.pkl', 'rb'))


# In[6]:
@app.route('/')
def home():
    return render_template('index.html')


# In[7]:
@app.route('/predict',methods=['POST'])
def predict():
      p_ID=request.form["ID1"]
      p_Gender=request.form["Gender1"]
      p_Age=request.form["Age1"]
      p_Region_Code=request.form["Region_Code1"]
      p_Occupation=request.form["Occupation1"]
      p_Channel_Code=request.form["Channel_Code1"]
      p_Vintage=request.form["Vintage1"]
      p_Credit_Product_Present=request.form["Credit_Product_Present1"]
      p_Avg_Account_Balance=request.form["Avg_Account_Balance1"]
      p_Is_Active=request.form["Is_Active1"]
#     final_features=[np.array(int_features)]
#     prediction=model.predict(final_features)
#     print(features)
      output="Yes"
      #output=round(prediction[0],2)
      
      
        
      # 1) ID is all good
      ID=p_ID
    
      ## Order followed below is as per input required in building model
      
      # 2) Gender needs modification
      is_Male=0
      if p_Gender=="male":
            is_Male=1
      
      # 3) Age is all good
      Age=p_Age
    
      # 4) Region Code needs modification
      Region_Code=p_Region_Code[2:]
    
      # 5) Vinatge is all good
      Vintage=p_Vintage
    
      # 6) Credit_Product_Present needs modification
      Credit_Product_Present=1
      if p_Credit_Product_Present=="no":
            Credit_Product_Present=0
            
      # 7) Avg_Account_Balance is all good
      Avg_Account_Balance=p_Avg_Account_Balance
        
      # 8) Is_Active needs modification
      Is_Active=1
      if p_Is_Active=="no":
        Is_Active=0
        
      # 9) Occupation needs modification
      # default meaning of occupation is entrepreneur
      Occupation_Other=0
      Occupation_Salaried=0
      Occupation_Self_Employed=0
      if p_Occupation=="selfEmployed":
          Occupation_Self_Employed=1
      elif p_Occupation=="salaried":
          Occupation_Salaried=1
      elif p_Occupation=="other":
          Occupation_Other=1
            
       # 10) Channel_Code needs modification
       # default meaning of Channel_Code is X1
      Channel_Code_X2=0
      Channel_Code_X3=0
      Channel_Code_X4=0
      if p_Channel_Code=="X2":
         Channel_Code_X2=1
      elif p_Channel_Code=="X3":
         Channel_Code_X3=1
      elif p_Channel_Code=="X4":
         Channel_Code_X4=1
            
            
      # Creating a list of input values
      Input_Values_after_Processing=[is_Male, 
                                     Age, 
                                     Region_Code, 
                                     Vintage, 
                                     Credit_Product_Present, 
                                     Avg_Account_Balance, 
                                     Is_Active, Occupation_Other, 
                                     Occupation_Salaried,
                                     Occupation_Self_Employed, 
                                     Channel_Code_X2, 
                                     Channel_Code_X3, 
                                     Channel_Code_X4
                                    ]
      
      # performing scaling on input values   
      Scaled_Input = scaler.transform([Input_Values_after_Processing]);
      
      #prediction=model.predict(Scaled_Input)
      prediction=model.predict_proba(Scaled_Input)
      
      #output=round(prediction[0][1],2)  
      output=round(prediction[0][1]*100,2) 
      
      return render_template('index.html',prediction_text="Customer : {} buying a Credit Card has a probability of {} %  ".format(p_ID,output))

      #return render_template("index.html")

# In[8]:


if __name__=="__main__":
    app.run(debug=True)
# In[11]:


tb
# In[ ]:





# Credit-Card-Lead-Prediction
<b>Analytics Vidhya - Hackathon 28-30 May 2021</b>
</br>https://datahack.analyticsvidhya.com/contest/job-a-thon-2/

<b>Problem Statement</b>: Bank is looking for our help in identifying customers that could show higher intent towards a recommended credit card in the form of percentage 

<br/><b>1) Data gathering</b>
<br/>&emsp;Train & Test csv files were provided
<br/><b>2) Feature Engineering</b>
<br/> &emsp;i) Handling missing values - in column 'Credit_Product' by filling na with value 'No' 
<br/> &emsp;ii) Handling Binary Categorical variables - columns 'Gender', Is_Active 
<br/> &emsp;iii) Handling Multiple-valued Categorical variables - columns 'Occupation',Channel_Code 
<br/> &emsp;iv) Data formatting - column 'Region_Code' , removing RG from start of string
<br/> &emsp;v) Scaling all column values to a single scale using 'Standard Scaler' 
<br/> <b>3) Feature Selection</b>
<br/> &emsp;Dropping columns : ID & Is_Lead (y), not required in model building
<br/><b>4) Model Creation</b>
<br/> &emsp; i) 
<br/> &emsp; ii) 
<br/><b>5) Testing the model</b>
<br/> &emsp;1) Logistic Regression - With Percentage - Private Score : 0.727
<br/> &emsp;2) Catboost Classifier - 5000 iterations - Private Score : 0.783
<br/> &emsp;Public Rank : 1727 
<br/> &emsp;Public Leaderboard: 0.7319135583
<br/> &emsp;Metrics : Confusion matrix & ROC curve
<br/> <b>6)Deployment</b>
<br/> &emsp;Model built has been deployed in <b>Heroku (PaaS) using Flask</b>
<br/> &emsp;It can be accessed via link: https://creditcard-purchase-prediction.herokuapp.com/
<br/> &emsp;For time being, Logistic Regression is used in api prediction
<br/> &emsp;Files reqd for deployment : 2 pickle files-scaler & model, app.py, index.html, procfile, requirements.txt
<br/> &emsp;Credits : Krish Naik - 
<br/> &emsp;Reference Links :
<br/> &emsp;&emsp;1) Deployment of ML models in Heroku using FLASK : 
<br/> &emsp;&emsp;https://www.youtube.com/watch?v=mrExsjcvF4o&t=880s
<br/> &emsp;&emsp;2) How To Debug Logs And Web Application In Heroku|Data Science :
<br/> &emsp;&emsp;https://www.youtube.com/watch?v=U350rWtxGwg&t=952s

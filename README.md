# Phonepe-Pulse-Data-Visualization
DS_Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly


Importing required libraries
import streamlit as st
from PIL import Image
import os
import json
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
import plotly.express as px
if the module shows any error or module not found it can be overcome by using below command
pip install<module name>
In order to get the data clone the github
Inorder to clone the github data into to working environment use below command
import requests
response = requests.get(url)
repo = response.json()
clone_url = repo['clone_url']
repo_name = "pulse"
clone_dir = os.path.join(os.getcwd(), repo_name)
Creating csv file
after cloning the data from github the dat in the form of json file
In order to convert json file into data frame we use below code
clm={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))

# Successfully created a dataframe
df_aggregated_transaction=pd.DataFrame(clm)
After creating dataframe insert the dataframe into sql server by using sqlite3
To Establish the connection with sql server
connection = sqlite3.connect("phonepe pulse.db")
cursor = connection.cursor()
Create sql queries to fetch the data as per the user requirement
SELECT * FROM "Table"
WHERE "Condition"
GROUP BY "Columns"
ORDER BY "Data"
create the streamlit app with basic tabs Reference
visualizing the data with plotly and streamlit
I hope this project helps you to the understand more about phonepe

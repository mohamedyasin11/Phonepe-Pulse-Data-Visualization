# importing libraries and package for phonepe pulse
import streamlit as st
from PIL import Image
import os
import json
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
import plotly.express as px

# To clone the data directly from github  using !git clone (code coped from git hub)
# !git clone https://github.com/PhonePe/pulse.git
# Once created the clone of GIT-HUB repository then,Succesfully created a dataframe using codes in colab
# Exporting the DataFrame to csv file

# inserting the image and videos
phn=Image.open(r'C:\Users\ELCOT\phonepe_pulse\phonepe-logo-icon.png')
phn1=Image.open(r'C:\Users\ELCOT\phonepe_pulse\phonepe.png')
phn2=Image.open(r'C:\Users\ELCOT\phonepe_pulse\phonepe1.png')
video_file = open(r'C:\Users\ELCOT\phonepe_pulse\Phonepe.mp4', 'rb')
video1 = video_file.read()
vedio_file1=open(r'C:\Users\ELCOT\phonepe_pulse\phonepesample.mp4','rb')
vedio2=vedio_file1.read()

# setting page title
st.set_page_config(page_title='PhonePe Pulse',page_icon=phn,layout="wide")
col1, col2 = st.columns((2,1))
with col1:
    st.title(':violet[ PhonePe Pulse Data Visualization]:white[2018-2022]')
with col2:
    st.image(phn, width=200)
 

# Reading the data from csv files
# Aggregated_Transaction
df_Aggregated_Transaction = pd.read_csv('Aggregated_Transaction.csv')
# Aggregated_User
df_Aggregated_User = pd.read_csv('Aggregated_User.csv')
# Map_Transaction
df_Map_Transaction = pd.read_csv('Map_Transaction.csv')
# Map_User
df_Map_User = pd.read_csv('Map_User.csv')
# Top_District_Transaction
df_Top_District_Transaction = pd.read_csv('Top_District_Transaction.csv')
# Top_Pincodes_Transaction
df_Top_Pincodes_Transaction = pd.read_csv('Top_Pincodes_Transaction.csv')
# Top_District_User
df_Top_District_User = pd.read_csv('Top_District_User.csv')
# Top_Pincodes_User
df_Top_Pincodes_User = pd.read_csv('Top_Pincodes_User.csv')

# CREATING CONNECTION WITH SQL SERVER
connection = sqlite3.connect("phonepe_pulse.db")
cursor = connection.cursor()

# Inserting each Data frame into sql server
df_Aggregated_Transaction.to_sql('Aggregated_Transaction', connection, if_exists='replace')
df_Aggregated_User.to_sql('Aggregated_User', connection, if_exists='replace')
df_Map_Transaction.to_sql('Map_Transaction', connection, if_exists='replace')
df_Map_User.to_sql('Map_User', connection, if_exists='replace')
df_Top_District_Transaction.to_sql('Top_District_Transaction', connection, if_exists='replace')
df_Top_Pincodes_Transaction.to_sql('Top_Pincodes_Transaction', connection, if_exists='replace')
df_Top_District_User.to_sql('Top_District_User', connection, if_exists='replace')
df_Top_Pincodes_User.to_sql('Top_Pincodes_User', connection, if_exists='replace')

# creating  for App
SELECT = option_menu(
        menu_title = None,
        options = ["About","Home","INSIGHTS"],
        icons =["bar-chart","house","toggles"],
        default_index=0,
        orientation= "horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "purple"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-1px" },
            "nav-link-selected": {"background-color": "#6739b7"}
        })
#st.image(phn2,width=450)    

if SELECT == "Home":
    st.subheader(
        "PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
    col1,col2 = st.columns(2)
    with col1:
        st.image(phn)
    with col2:
        st.video(video1)
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")    

if SELECT == "About":
    st.subheader("The Indian digital payments story has truly captured the world's imagination."
                 " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                 " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                 "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
    col1,col2 = st.columns(2)
    with col1:
        st.image(phn1)
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.subheader("Phonepe Now Everywhere..!")
        st.video(vedio2)
        
        
if SELECT == "INSIGHTS":
    st.title("BASIC INSIGHTS")
    st.subheader("Let's know basic insights")
    options = ["--select--","Top 10 States Transaction","Least 10 States Transaction",
               "Top 10 district Transaction","Least 10 district Transaction",
               "Top 10 District based on User","Top 10 mobile brands user",
               "Top 10 Registered-users based on District(pincode)",
               "Top 10 Districts based on states and amount of transaction",
               "Least 10 Districts based on states and amount of transaction",
               "Least 10 registered-users based on Districts and states",
               "Top 10 transactions_type based on Transacion type and transaction_amount"]
    
    select = st.selectbox("Select the option",options)
    
    if select=="Top 10 States Transaction":
        cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quater FROM Top_Pincodes_Transaction GROUP BY State ORDER BY Transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quater'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 states based on type and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)
                
    if select=="Least 10 States Transaction":
        cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quater FROM Top_Pincodes_Transaction GROUP BY State ORDER BY Transaction_amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quater'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 states based on type and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)            
                
    if select=="Top 10 district Transaction":
        cursor.execute("SELECT DISTINCT State,District_name	,Transaction_amount,Year,Quater FROM Top_District_Transaction GROUP BY District_name ORDER BY Transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District_name','Transaction_amount','Year','Quater'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 district Transaction")
            fig=px.bar(df,x="District_name",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)
                
    if select=="Least 10 district Transaction":
        cursor.execute("SELECT DISTINCT State,District_name	,Transaction_amount,Year,Quater FROM Top_District_Transaction GROUP BY District_name ORDER BY Transaction_amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District_name','Transaction_amount','Year','Quater'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 district Transaction")
            fig=px.bar(df,x="District_name",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)   
         
   
         
    if select=="Top 10 District based on User":
        cursor.execute("SELECT DISTINCT State,District_name,RegisteredUsers,Year,Quater FROM Top_District_User GROUP BY State,District_name ORDER BY RegisteredUsers DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District_name','RegisteredUsers','Year','Quater'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 District based on User")
            fig=px.bar(df,x="District_name",y="RegisteredUsers")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)      
 
    if select=="Top 10 mobile brands user":
        cursor.execute("SELECT DISTINCT user_brand,user_count,user_percentage FROM Aggregated_User GROUP BY user_brand ORDER BY user_percentage DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['user_brand','user_count','user_percentage'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 mobile brands user")
            fig=px.pie(df,names="user_brand",values="user_percentage")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)  
                 
    if select=="Top 10 Registered-users based on District(pincode)":
        cursor.execute("SELECT DISTINCT State,pincodes,RegisteredUsers FROM Top_Pincodes_User GROUP BY State,pincodes ORDER BY RegisteredUsers DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','pincodes','RegisteredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 Registered-users based on state & District(pincode)")
            fig=px.bar(df,x="State",y="RegisteredUsers")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)  
                
    elif select=="Top 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT State,District_name,Transaction_amount FROM Map_Transaction GROUP BY State,District_name ORDER BY Transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District_name','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 Districts based on states and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)
                
    if select=="Least 10 Districts based on states and amount of transaction": 
        cursor.execute("SELECT DISTINCT State,District_name,Transaction_amount FROM Map_Transaction GROUP BY State,District_name ORDER BY Transaction_amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District_name','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 Districts based on states and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)
                
    if select=="Least 10 registered-users based on Districts and states":
        cursor.execute("SELECT DISTINCT State,District_name,RegisteredUsers FROM Top_District_User GROUP BY State,District_name ORDER BY RegisteredUsers ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District_name','RegisteredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 registered-users based on Districts and states")
            fig=px.bar(df,x="State",y="RegisteredUsers")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)   
               
    if select=="Top 10 transactions_type based on Transacion type and transaction_amount":
        cursor.execute("SELECT DISTINCT Transacion_type,Transacion_amount FROM Aggregated_Transaction GROUP BY Transacion_type ORDER BY Transacion_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['Transacion_type','Transacion_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 transactions_type based on states and transaction_amount")
            fig=px.pie(df,names="Transacion_type",values="Transacion_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)            
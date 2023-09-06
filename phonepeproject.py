# importing libraries and package for phonepe pulse
import streamlit as st
from PIL import Image
#import os
#import json
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
import plotly.express as px

# To clone the data directly from github  using !git clone (code coped from git hub) !git clone https://github.com/PhonePe/pulse.git
# Once created the clone of GIT-HUB repository then,Succesfully created a dataframe using codes in colab,Exporting the DataFrame to csv file

# inserting the image and videos
phn=Image.open(r'image and video files/phonepe-logo-icon.png')
phn1=Image.open(r'image and video files/phonepe.png')
video_file = open(r'image and video files/Phonepe.mp4', 'rb')
video1 = video_file.read()
vedio_file1=open(r'image and video files/phonepesample.mp4','rb')
vedio2=vedio_file1.read()

# setting page title
st.set_page_config(page_title='PhonePe Pulse',page_icon=phn,layout="wide")
col1, col2 = st.columns((2,1))
with col1:
    st.title(':violet[ PhonePe Pulse Data Visualization]:white[2018-2022]')
with col2:
    st.image(phn,width=200)
    
# Reading the data from csv files
df_Aggregated_Transaction = pd.read_csv(r'csv files/Aggregated_Transaction.csv') # Aggregated_Transaction
df_Aggregated_User = pd.read_csv(r'csv files/Aggregated_User.csv') # Aggregated_User
df_Map_Transaction = pd.read_csv(r'csv files/Map_Transaction.csv') # Map_Transaction
df_Map_User = pd.read_csv(r'csv files/Map_User.csv') # Map_User
df_Top_District_Transaction = pd.read_csv(r'csv files/Top_District_Transaction.csv') # Top_District_Transaction
df_Top_Pincodes_Transaction = pd.read_csv(r'csv files/Top_Pincodes_Transaction.csv') # Top_Pincodes_Transaction
df_Top_District_User = pd.read_csv(r'csv files/Top_District_User.csv') # Top_District_User
df_Top_Pincodes_User = pd.read_csv(r'csv files/Top_Pincodes_User.csv')    # Top_Pincodes_User

# CREATING CONNECTION WITH SQL SERVER 
connection = sqlite3.connect("phonepepulse.db")
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

# Load the data into Pandas dataframes
agg_trans = pd.read_sql("SELECT * FROM Aggregated_Transaction", con=connection)
agg_users = pd.read_sql("SELECT * FROM Aggregated_User", con=connection)
map_trans = pd.read_sql("SELECT * FROM Map_Transaction", con=connection)
map_users = pd.read_sql("SELECT * FROM Map_User", con=connection)
top_trans = pd.read_sql("SELECT * FROM Top_Pincodes_Transaction", con=connection)
top_users = pd.read_sql("SELECT * FROM Top_Pincodes_User", con=connection)

#List the India State name
States = ['Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli','NCT of Delhi','Goa','Gujarat',
          'Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya',
          'Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']

# Define a dictionary of state name replacements for choropleth geo visualization
state_replacements = {
    'andaman-&-nicobar-islands': 'Andaman & Nicobar Island','andhra-pradesh': 'Andhra Pradesh', 'arunachal-pradesh': 'Arunanchal Pradesh','assam': 'Assam',
    'bihar': 'Bihar','chandigarh': 'Chandigarh','chhattisgarh': 'Chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu': 'Dadara & Nagar Havelli','delhi': 'NCT of Delhi',
    'goa': 'Goa','gujarat': 'Gujarat','haryana': 'Haryana','himachal-pradesh': 'Himachal Pradesh','jammu-&-kashmir': 'Jammu & Kashmir', 'jharkhand': 'Jharkhand',
    'karnataka': 'Karnataka','kerala': 'Kerala','ladakh': 'Ladakh','lakshadweep': 'Lakshadweep', 'madhya-pradesh': 'Madhya Pradesh', 'maharashtra': 'Maharashtra',
    'manipur': 'Manipur','meghalaya': 'Meghalaya','mizoram': 'Mizoram','nagaland': 'Nagaland','odisha': 'Odisha','puducherry': 'Puducherry','punjab': 'Punjab',
    'rajasthan': 'Rajasthan','sikkim': 'Sikkim','tamil-nadu': 'Tamil Nadu','telangana': 'Telangana','tripura': 'Tripura','uttar-pradesh': 'Uttar Pradesh','uttarakhand': 'Uttarakhand',
    'west-bengal': 'West Bengal',
}

# Replace state names in each dataframe
for tables in ['agg_trans', 'agg_users', 'map_trans', 'map_users', 'top_trans', 'top_users']:
   df = globals()[tables]  # Get the dataframe by name
   df['State'] = df['State'].replace(state_replacements)

# creating option for App   
SELECT = option_menu( menu_title = None,
        options = ["About","Home","INSIGHTS","India Wise","State Wise"],
        icons =["bar-chart","house","toggles","list-task","list-task"],default_index=1,orientation= "horizontal",
        styles={ "container": {"padding": "0!important", "background-color": "purple"},
                "icon": {"color": "black", "font-size": "20px"},
                "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-1px" },
                "nav-link-selected": {"background-color": "#6739b7"}        })

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
        
if SELECT == "Home":
    st.subheader("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
    col1,col2 = st.columns(2)
    with col1:
        st.image(phn)
    with col2:
        st.video(video1)
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")  
       
if SELECT=="India Wise":
    option = st.radio("Which type of visualisation you need ", ["Transactions","Users"], index=1)    
    if option == "Transactions":
        option8 = st.selectbox('--Select--',("Transaction_count","Transaction_amount"))    
    if option == "Users":
      option8 = st.selectbox('--Select--',("RegisteredUsers","AppOpens"))
       
if SELECT=="State Wise":
    option = st.radio("Which visualisation you Need", ["Transactions","Users"], index=1)
    if option == "Transactions":
     option1 = st.selectbox('Select the State Name',States)
     option2 = st.selectbox('Select the Year',(2018, 2019, 2020, 2021, 2022))
     option3 = st.selectbox('Select the Quarter ',(1, 2, 3, 4))
     option4 = st.selectbox('Select the Drop',("Transaction_count","Transaction_amount"))
        
    if option == "Users":
      option1 = st.selectbox('Select the State Name',States)
      option2 = st.selectbox('Select the Year',(2018, 2019, 2020, 2021, 2022))
      option3 = st.selectbox('Select the Quarter',(1, 2, 3, 4))
      option4 = st.selectbox('Select the Drop',("RegisteredUsers","AppOpens"))

# Functional Block
def fig(bar,xc,yc):
    fig=px.bar(df,x=xc,y=yc)
    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    with tab2:
        st.plotly_chart(fig, theme=None, use_container_width=True)  

def df(query,col):
    cursor.execute(query);
    df = pd.DataFrame(cursor.fetchall(),columns=col)
    return df

def indiamap():
    c= map_trans.groupby(["State","Year"]).sum()
    c.reset_index(inplace = True)
    return c 

def transName():
    p= map_trans.groupby(["State","Year","Transaction_count","Transaction_amount"]).sum()
    p.reset_index(inplace = True)
    return p

def trantype():
    t= agg_trans.groupby(["State","Year","Transaction_type","Transaction_count","Transaction_amount"]).sum()
    t.reset_index(inplace= True)
    return t

def mapUser():
    u= map_users.groupby(["State","Year"]).sum()
    u.reset_index(inplace = True)
    return u

def aggTrans(option1,option2,option3):
    a= agg_trans[(agg_trans.State == option1) & (agg_trans.Year == option2) & (agg_trans.Quater == option3)]
    a.reset_index(inplace = True)
    return a

def mapTrans(option1,option2,option3):
    mt= map_trans[(map_trans.State == option1) & (map_trans.Year == option2) & (map_trans.Quater == option3)]
    mt.reset_index(inplace = True)
    return mt

def mapUserState(option1,option2,option3):
    au= map_users[(map_users.State == option1) & (map_users.Year == option2) & (map_users.Quater == option3)]
    au.reset_index(inplace = True)
    return au

# query
query1 = "SELECT DISTINCT State,Transaction_amount,Year,Quater FROM Top_Pincodes_Transaction GROUP BY State ORDER BY Transaction_amount DESC LIMIT 10"
col1 = ['State','Transaction_amount','Year','Quater']
query2 = "SELECT DISTINCT State,Transaction_amount,Year,Quater FROM Top_Pincodes_Transaction GROUP BY State ORDER BY Transaction_amount ASC LIMIT 10"
col2 = ['State','Transaction_amount','Year','Quater']
query3 ="SELECT DISTINCT District_name,Transaction_amount,Year,Quater FROM Top_District_Transaction GROUP BY District_name ORDER BY Transaction_amount DESC LIMIT 10"
col3 = ['District_name','Transaction_amount','Year','Quater']
query4 = "SELECT DISTINCT District_name	,Transaction_amount,Year,Quater FROM Top_district_Transaction GROUP BY District_name ORDER BY Transaction_amount ASC LIMIT 10"
col4 = ['District_name','Transaction_amount','Year','Quater']
query5 ="SELECT DISTINCT State,District_name,RegisteredUsers,Year,Quater FROM Top_District_User GROUP BY State,District_name ORDER BY RegisteredUsers DESC LIMIT 10"
col5 = ['State','District_name','RegisteredUsers','Year','Quater']
query6 ="SELECT DISTINCT user_brand,user_count,user_percentage FROM Aggregated_User GROUP BY user_brand ORDER BY user_percentage DESC LIMIT 10"
col6 = ['user_brand','user_count','user_percentage']
query7 ="SELECT DISTINCT State,pincodes,RegisteredUsers FROM Top_Pincodes_User GROUP BY State,pincodes ORDER BY RegisteredUsers DESC LIMIT 10"
col7 = ['State','pincodes','RegisteredUsers']
query8 = "SELECT DISTINCT State,District_name,Transaction_amount FROM Map_Transaction GROUP BY State,District_name ORDER BY Transaction_amount DESC LIMIT 10"
col8 = ['State','District_name','Transaction_amount']
query9 = "SELECT DISTINCT State,District_name,Transaction_amount FROM Map_Transaction GROUP BY State,District_name ORDER BY Transaction_amount ASC LIMIT 10"
col9 = ['State','District_name','Transaction_amount']
query10 = "SELECT DISTINCT State,District_name,RegisteredUsers FROM Top_District_User GROUP BY State,District_name ORDER BY RegisteredUsers ASC LIMIT 10"
col10 = ['State','District_name','RegisteredUsers']
query11 ="SELECT DISTINCT Transaction_type,Transaction_amount FROM Aggregated_Transaction GROUP BY Transaction_type ORDER BY Transaction_amount DESC LIMIT 10"
col11 = ['Transaction_type','Transaction_amount']

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
    
    # option for insight dropdown 
    if select == "Top 10 States Transaction":
        df=df(query1,col1)
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 states based on type and amount of transaction")
            fig('bar','State','Transaction_amount')
            
    if select=="Least 10 States Transaction":
        df=df(query2,col2)
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 states transaction")
            fig('bar','State','Transaction_amount')   

    if select=="Top 10 district Transaction":
        df=df(query3,col3)
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 district Transaction")
            fig('bar',"District_name","Transaction_amount")   

                
    if select=="Least 10 district Transaction":
        df=df(query4,col4)    
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 district Transaction")
            fig('bar',"District_name","Transaction_amount")

    if select=="Top 10 District based on User":
        df=df(query5,col5)
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 District based on User")
            fig('bar',"District_name","RegisteredUsers")

    if select=="Top 10 mobile brands user":
        df=df(query6,col6)
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
        df=df(query7,col7)
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 Registered-users based on state & District(pincode)")
            fig('bar',"State","RegisteredUsers")    

    if select=="Top 10 Districts based on states and amount of transaction":
        df=df(query8,col8)
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 Districts based on states and amount of transaction")
            fig('bar',"State","Transaction_amount")          
                  
    if select=="Least 10 Districts based on states and amount of transaction": 
        df=df(query9,col9)
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 Districts based on states and amount of transaction")
            fig('bar',"State","Transaction_amount")
      
    if select=="Least 10 registered-users based on Districts and states":
        df=df(query10,col10)
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 registered-users based on Districts and states")
            fig('bar',"State","RegisteredUsers")
        
    if select=="Top 10 transactions_type based on Transacion type and transaction_amount":
        df=df(query11,col11)
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 transactions_type based on states and transaction_amount")
            fig=px.pie(df,names="Transaction_type",values="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)
            
#Button for Indian Map
if SELECT =="India Wise":
  if option == "Transactions":
      if st.button("Show"):
          c = indiamap()
          p = transName()  
          t= trantype()
          
          fig=px.choropleth(c,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
             featureidkey='properties.ST_NM',
             locations='State',   color=option8,   animation_frame='Year',
             color_continuous_scale='twilight',
             height=700,width=900)
          
          fig.update_geos(fitbounds="locations", visible=False)
          fig.update_layout(margin=dict(l=60, r=60, t=50, b=50))   
          st.write("Transactions")
          st.write(fig)     
#          pi = px.bar(p, x="State", y=option8,animation_frame= 'Year' ,title="Transaction and its Contribution with respect to State",width=900,height=700)
#          st.write(pi)        
          tt = px.bar(t, x="State", y=option8, color= "Transaction_type", animation_frame= 'Year' ,title="Transaction Types and its Contribution with respect to State",width=900,height=700)
          st.write(tt)           
            
  if option == "Users":
   if st.button("Show"):
    u = mapUser()
    
    fig=px.choropleth(
       u,
       geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
       featureidkey='properties.ST_NM',
       locations='State',
       color=option8,
       animation_frame='Year',
       color_continuous_scale='ice',
       height=700,
       width=900
      )
      
    fig.update_geos(fitbounds="locations", visible=False)
    st.write("About User")
    st.write(fig)
                             
#Button for statewise
if SELECT=="State Wise":
  if option == "Transactions":
   if st.button('Show'):
    a= aggTrans(option1,option2,option3)
    mt= mapTrans(option1,option2,option3)
   
    fig = px.choropleth(
       a,
       geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
       featureidkey='properties.ST_NM',
       locations='State',
       color= option4,
       animation_frame="Year",
       color_continuous_scale='aggrnyl'
      )

    fig.update_geos(fitbounds="locations", visible=False)      
    st.write("total transaction")
    st.write(fig)
    fi = px.bar(mt, x='District_name', y=option4)
    st.write(fi)

  if option == "Users":
   if st.button('Show'):
    au= mapUserState(option1,option2,option3)
  
    fig = px.choropleth(
       au,
       geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
       featureidkey='properties.ST_NM',
       locations='State',
       color=option4,
       color_continuous_scale='ice'
      )

    fig.update_geos(fitbounds="locations", visible=False)
      
    st.write("total transaction")
    st.write(fig)  

    fi = px.bar(au, x='District_name', y=option4)
    st.write(fi)               

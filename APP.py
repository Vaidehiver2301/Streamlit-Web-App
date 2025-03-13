#importing packages
import streamlit as st
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

#Title and Subheader
st.title("Data Analysis")
st.subheader("Data Analysis using python and streamlit.")

#Uploading data
upload=st.file_uploader("Upload Your File in csv format")
if upload is not None:
    data=pd.read_csv(upload)

#Preview dataset
if upload is not None:
    if st.checkbox("Preview DataSet"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

#Check Datatypes
if upload is not None:
    if st.checkbox("Data Types of each column"):
        st.text("Data Types")
        st.write(data.dtypes)
        
#Check the shape 
if upload is not None:
   if st.button("Shape of dataset"):
       data_shape=st.radio("What dimensions do you want to check",('rows','columns'))
       
       
       if data_shape=='rows':
           st.text("Number of Rows")
           st.write(data.shape[0])
       if data_shape=='columns':
           st.text("Number of columns")
           st.write(data.shape[1])
#Find null values
if upload is not None:
    test=data.isnull().values.any()
    #when test has value true
    if test==True:
        if st.button("Null Values"):
            st.text("Null Values Heatmap")
            plt.figure(figsize=(10, 6))
            sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
            st.pyplot(plt)
    else:
        st.success("No Null Values Found in the Dataset!")
    
#Find duplicate values
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("Duplicate values found!")
        dup=st.selectbox("Do you want to remove duplicate values?",("Select one", "yes", "No"))
        if dup=="yes":
            data=data.drop_duplicates()
            st.text("Duplicate values are removed!")
    
#View overall statistics
if upload is not None:
    if st.button("Summary"):
        st.write(data.describe(include="all"))
    
    
#About Section
if st.button("About"):
    st.text("This app is made with streamlit.")
    st.text("Other libraries used: Pandas, Seaborn and Matplotlib.")
    st.success("Built by Vaidehi Verma.")
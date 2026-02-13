import streamlit as st
from pymongo import MongoClient

st.title("Days to Weeks Converter")

# connect to MongoDB
try:
    client = MongoClient("mongodb://127.0.0.1:27017/")
    # create database
    db = client["database_name"]
    # create collection
    collection = db["collection_name"]
    st.success("Connected to MongoDB")
except Exception as e:
    st.error(f"Failed to connect to MongoDB: {e}")

days = st.number_input("Enter number of days:", min_value=0, step=1, value=0)

if days is not None:
    # Calculate weeks and remaining days
    weeks = days // 7
    remaining_days = days % 7

    # Display result
    st.write(f"{weeks} week(s) and {remaining_days} day(s)")
    
    # Insert data into MongoDB
    if st.button("Save to Database"):
        data = {"days": days, "weeks": weeks, "remaining_days": remaining_days}
        collection.insert_one(data)
        st.success("Data saved to MongoDB!")
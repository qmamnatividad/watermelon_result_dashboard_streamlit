import streamlit as st
import pandas as pd

# Load the CSV data
@st.cache
def load_data():
    data = pd.read_csv("watermelon_result.csv")
    return data

# Create a Streamlit app
def main():
    st.title("Watermelon Ripeness Result")
    
    # Load the data
    data = load_data()
    
    # Display the data
    st.write("Raw data:")
    st.write(data)
    
    # Print out the column names to verify the correct column name
    st.write("Column names:")
    st.write(data.columns)
    
    # Create pie chart for ripeness
    st.write("Pie chart for ripeness:")
    if 'ripeness' in data.columns:
        ripeness_counts = data['ripeness'].value_counts()
        st.pyplot(ripeness_counts.plot.pie(autopct='%1.1f%%'))
    else:
        st.write("Error: 'ripeness' column not found in the data.")

# Run the app
if __name__ == "__main__":
    main()

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
    
    # Create pie chart for ripeness
    st.write("Pie chart for ripeness:")
    ripeness_counts = data['ripeness'].value_counts()
    st.pyplot(ripeness_counts.plot.pie(autopct='%1.1f%%'))

# Run the app
if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
@st.cache
def load_data():
    data = pd.read_csv("watermelon_result.csv")
    return data

# Create a Streamlit app
def main():
    st.title("Fruit Data")
    
    # Load the data
    data = load_data()
    
    # Display the data
    st.write("Raw data:")
    st.write(data)
    
    # Create pie chart for ripeness
    st.write("Pie chart for ripeness:")
    ripeness_counts = data['ripeness'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(ripeness_counts, labels=ripeness_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

# Run the app
if __name__ == "__main__":
    main()

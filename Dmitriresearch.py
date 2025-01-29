import streamlit as st
import pandas as pd

# Title of the app
st.title("Dmitri Frantz Research")

# Collect basic information
name = "Mr Dmitri Frantz"
field = "Doctorate in Philosophy Development Studies"
institution = "University of the Western Cape"

# Display basic profile information
st.header("Unravelling the challenges of basic service delivery in local municipalities: Exploring the factors underlying inefficiencies and inadequacies in Cederberg Municipality ")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("This study aims to investigate the challenges contributing to the inefficiencies and inadequacies in basic service delivery within the Cederberg Municipality in South Africa. The research will explore the specific challenges impeding basic service delivery and identify key areas where improvements can be made to enhance the effectiveness and responsiveness of local governance. The study is significant as it aligns with the constitutional objective, other government policies and strategies relating to the provision of services to the community in a sustainable manner and aims to contribute to the well-being and quality of life of the local communities. The findings of this research will offer valuable insights into the root causes of basic service delivery challenges and provide recommendations for improving governance practices at the local level. ")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")
        
# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Dmitri Frantz")
email = "dmitrifrantz@yahoo.com"
st.write(f"You can reach {name} at {email}.")

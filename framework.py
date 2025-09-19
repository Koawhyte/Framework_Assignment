import streamlit as st
import pandas as pd
import matplotlib.pyplot  as plt

#Load the data
df = pd.read_csv('metadata.csv')

#converting published time to  datetime format
df['publish_time'] = pd.to_datetime(df['publish_time'])
df['year'] = df['publish_time'].dt.year

#Explore the data
print(df.shape)
print(df.info())
print(df.head())

# creating a streamlit app
st.title('CORD-19 Research Dataset')
st.write(df.head())

st.write("The dataset contains", df.shape[0], "rows and", df.shape[1], "columns.")
st.write("The columns are:", df.columns.tolist())

#creating a drop down menu to select different authors
authors = df['authors'].unique()
selected_author = st.delectbox('delect an author', authors)

#Filtering the data by author
author_data = df[df['authors'] == selected_author]

#creating a bar chart of publication by year
year_counts = author_data['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title(f'Publications by {selected_author}')
st.pyplot(fig)


st.write(f"{selected_author} has published", len(author_data), "papers in the dataset.")
st.write("The top 5 years with the most publications are:")
st.write(year_counts.nlargest(5))

#create a histogram of publication years
fig , ax = plt.subplots()
ax.hist(df['year'], bins=10)
ax.set_title('Histogram of Publication Years')
st.pyplot(fig)

st.write("The Histogram shows the distribution of publication year in the dataset")
st.write("The most common publication year is:", df['year'].mode()[0])

top_authors = df['authors'].value_counts().nlargest(10)
fig, ax = plt.subplots()
ax.bar(top_authors.index, top_authors.values)
ax.set_title('Top 10 Authors')
st.pyplot(fig)

st.write("The top 10 authors with the most publications are:")
st.write(top_authors)

















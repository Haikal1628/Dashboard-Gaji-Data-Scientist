# Import Library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dashboard Title
st.title("Dashboard Gaji Data Scientist")
st.markdown("Dashboard ini memberikan gambaran sederhana tentang data gaji Data Scientist untuk audiens awam.")

# Load Dataset
file_path = 'cleaned_dataset.csv' 
df = pd.read_csv(file_path)

# Sidebar Filters
st.sidebar.header("Filter Data")

# Input boxes for year range
start_year = st.sidebar.number_input(
    "Tahun Mulai", 
    min_value=int(df['work_year'].min()), 
    max_value=int(df['work_year'].max()), 
    value=int(df['work_year'].min())
)
end_year = st.sidebar.number_input(
    "Tahun Akhir", 
    min_value=int(df['work_year'].min()), 
    max_value=int(df['work_year'].max()), 
    value=int(df['work_year'].max())
)

# Validation: Ensure start_year <= end_year
if start_year > end_year:
    st.sidebar.error("Tahun Mulai harus lebih kecil atau sama dengan Tahun Akhir")

# Multiselect for experience level
selected_exp = st.sidebar.multiselect(
    "Pilih Tingkat Pengalaman", 
    options=df['experience_level'].unique(), 
    default=df['experience_level'].unique()
)

# Apply Filters
filtered_df = df[(df['work_year'] >= start_year) & (df['work_year'] <= end_year)]
filtered_df = filtered_df[filtered_df['experience_level'].isin(selected_exp)]

# Display Overview of Filtered Data
st.subheader("Data")
st.write(f"Jumlah data yang ditampilkan: {len(filtered_df)}")
st.dataframe(filtered_df.head())

# Average Salary Over Years 
st.subheader("1. Rata-rata Gaji Berdasarkan Tahun")
avg_salary = filtered_df.groupby('work_year')['salary_in_usd'].mean()
fig, ax = plt.subplots()
avg_salary.plot(kind='line', marker='o', color='blue', ax=ax)
ax.set_title("Rata-rata Gaji Berdasarkan Tahun")
ax.set_xlabel("Tahun")
ax.set_ylabel("Gaji Rata-rata (USD)")
st.pyplot(fig)

#  Total Jobs by Year 
st.subheader("2. Total Jumlah Pekerjaan Berdasarkan Tahun")
job_count = filtered_df.groupby('work_year').size()
fig2, ax2 = plt.subplots()
job_count.plot(kind='bar', color='skyblue', ax=ax2)
ax2.set_title("Total Jumlah Pekerjaan Berdasarkan Tahun")
ax2.set_xlabel("Tahun")
ax2.set_ylabel("Jumlah Pekerjaan")
st.pyplot(fig2)

#  Average Salary by Experience Level 
st.subheader("3. Rata-rata Gaji Berdasarkan Tingkat Pengalaman")
avg_salary_exp = filtered_df.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False)
fig3, ax3 = plt.subplots()
avg_salary_exp.plot(kind='bar', color='green', ax=ax3)
ax3.set_title("Rata-rata Gaji Berdasarkan Tingkat Pengalaman")
ax3.set_xlabel("Tingkat Pengalaman")
ax3.set_ylabel("Gaji Rata-rata (USD)")
st.pyplot(fig3)

# Average Salary by Company Size 
st.subheader("4. Rata-rata Gaji Berdasarkan Ukuran Perusahaan")
avg_salary_size = filtered_df.groupby('company_size')['salary_in_usd'].mean().sort_values(ascending=False)
fig4, ax4 = plt.subplots()
avg_salary_size.plot(kind='bar', color='orange', ax=ax4)
ax4.set_title("Rata-rata Gaji Berdasarkan Ukuran Perusahaan")
ax4.set_xlabel("Ukuran Perusahaan")
ax4.set_ylabel("Gaji Rata-rata (USD)")
st.pyplot(fig4)

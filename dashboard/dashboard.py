import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Memuat dataset yang sudah dibersihkan
guanyuan_df = pd.read_csv('all_data.csv')

# title untuk dashboard
st.title('Dashboard Analisis Kualitas Udara di Guanyuan Pada Tahun 2013-2017')

# Menambahkan deskripsi
st.markdown('Dashboard ini menyajikan hasil analisis kualitas udara di Guanyuan yang berfokus pada polutan utama PM2.5, CO, PM10, SO2, NO2 dab O3.')

# Pilihan untuk memilih polutan
polutan = st.selectbox('Pilih polutan', ['PM2.5', 'CO', 'PM10', 'SO2', 'NO2', 'O3'])

# Menampilkan visualisasi berdasarkan pilihan polutan
if polutan == 'PM2.5':
    # Menampilkan grafik untuk PM2.5
    st.subheader('Tren Kualitas Udara (PM2.5)')
    pm2_5_plot = guanyuan_df.groupby('year')['PM2.5'].mean().plot(kind='line', marker='o', color='b', label='PM2.5')
    plt.title('Tren Tahunan PM2.5')
    plt.xlabel('Tahun')
    plt.ylabel('Konsentrasi PM2.5 (µg/m³)')
    st.pyplot(pm2_5_plot.figure)
    
elif polutan == 'CO':
    # Menampilkan grafik untuk CO
    st.subheader('Tren Kualitas Udara (CO)')
    co_plot = guanyuan_df.groupby('year')['CO'].mean().plot(kind='line', marker='o', color='g', label='CO')
    plt.title('Tren Tahunan CO')
    plt.xlabel('Tahun')
    plt.ylabel('Konsentrasi CO (µg/m³)')
    st.pyplot(co_plot.figure)

elif polutan == 'PM10':
    # Menampilkan grafik untuk PM10
    st.subheader('Tren Kualitas Udara (PM10)')
    co_plot = guanyuan_df.groupby('year')['PM10'].mean().plot(kind='line', marker='o', color='r', label='PM10')
    plt.title('Tren Tahunan PM10')
    plt.xlabel('Tahun')
    plt.ylabel('Konsentrasi PM10 (µg/m³)')
    st.pyplot(co_plot.figure)

elif polutan == 'SO2':
    # Menampilkan grafik untuk SO2
    st.subheader('Tren Kualitas Udara (SO2)')
    co_plot = guanyuan_df.groupby('year')['SO2'].mean().plot(kind='line', marker='o', color='m', label='SO2')
    plt.title('Tren Tahunan SO2')
    plt.xlabel('Tahun')
    plt.ylabel('Konsentrasi SO2 (µg/m³)')
    st.pyplot(co_plot.figure)

elif polutan == 'NO2':
    # Menampilkan grafik untuk NO2
    st.subheader('Tren Kualitas Udara (NO2)')
    co_plot = guanyuan_df.groupby('year')['NO2'].mean().plot(kind='line', marker='o', color='gray', label='NO2')
    plt.title('Tren Tahunan NO2')
    plt.xlabel('Tahun')
    plt.ylabel('Konsentrasi NO2 (µg/m³)')
    st.pyplot(co_plot.figure)

elif polutan == 'O3':
    # Menampilkan grafik untuk O3
    st.subheader('Tren Kualitas Udara (O3)')
    co_plot = guanyuan_df.groupby('year')['O3'].mean().plot(kind='line', marker='o', color='brown', label='O3')
    plt.title('Tren Tahunan O3')
    plt.xlabel('Tahun')
    plt.ylabel('Konsentrasi O3 (µg/m³)')
    st.pyplot(co_plot.figure)

st.text("Gambar ini menunjukan fluktuasi setiap Polutan yang berada di daerah Guanyuan dari tahun 2013-2017")


# Menampilkan Boxplot

if polutan == 'PM2.5':
    # Menampilkan grafik untuk PM2.5
    st.subheader('Perbandingan Konsentrasi PM2.5 antara Musim Dingin dan Musim Panas')
    boxplot = plt.figure(figsize=(8, 6))
    sns.boxplot(x='season', y='PM2.5', data=guanyuan_df)
    plt.title('Perbandingan PM2.5 berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Konsentrasi PM2.5 (µg/m³)')
    st.pyplot(boxplot)
    
elif polutan == 'CO':
    # Menampilkan grafik untuk CO
    st.subheader('Perbandingan Konsentrasi CO antara Musim Dingin dan Musim Panas')
    boxplot = plt.figure(figsize=(8, 6))
    sns.boxplot(x='season', y='CO', data=guanyuan_df)
    plt.title('Perbandingan CO berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Konsentrasi CO (µg/m³)')
    st.pyplot(boxplot)

elif polutan == 'PM10':
    # Menampilkan grafik untuk PM10
    st.subheader('Perbandingan Konsentrasi PM10 antara Musim Dingin dan Musim Panas')
    boxplot = plt.figure(figsize=(8, 6))
    sns.boxplot(x='season', y='PM10', data=guanyuan_df)
    plt.title('Perbandingan PM10 berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Konsentrasi PM10 (µg/m³)')
    st.pyplot(boxplot)

elif polutan == 'SO2':
    # Menampilkan grafik untuk SO2
    st.subheader('Perbandingan Konsentrasi SO2 antara Musim Dingin dan Musim Panas')
    boxplot = plt.figure(figsize=(8, 6))
    sns.boxplot(x='season', y='SO2', data=guanyuan_df)
    plt.title('Perbandingan SO2 berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Konsentrasi SO2 (µg/m³)')
    st.pyplot(boxplot)

elif polutan == 'NO2':
    # Menampilkan grafik untuk NO2
    st.subheader('Perbandingan Konsentrasi NO2 antara Musim Dingin dan Musim Panas')
    boxplot = plt.figure(figsize=(8, 6))
    sns.boxplot(x='season', y='NO2', data=guanyuan_df)
    plt.title('Perbandingan NO2 berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Konsentrasi NO2 (µg/m³)')
    st.pyplot(boxplot)

elif polutan == 'O3':
    # Menampilkan grafik untuk O3
    st.subheader('Perbandingan Konsentrasi O3 antara Musim Dingin dan Musim Panas')
    boxplot = plt.figure(figsize=(8, 6))
    sns.boxplot(x='season', y='O3', data=guanyuan_df)
    plt.title('Perbandingan O3 berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Konsentrasi O3 (µg/m³)')
    st.pyplot(boxplot)


st.text("Gambar ini menunjukan Boxplot Polutan berdasarkan Musimnya")

# Menghitung korelasi antar variabel numerik
numeric_cols = guanyuan_df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = guanyuan_df[numeric_cols].corr()

# Menampilkan heatmap korelasi
st.subheader('**Heatmap Korelasi Antar Polutan dan Variabel Lainnya**:')
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.9)
plt.title('Correlation Heatmap Air Quality')
st.pyplot(plt)


# Membuat line plot untuk melihat fluktuasi Polutan berdasarkan jam
plt.figure(figsize=(12, 6))
guanyuan_df.groupby('hour')['PM2.5'].mean().plot(kind='line', marker='o', color='blue', label='PM2.5')
guanyuan_df.groupby('hour')['CO'].mean().plot(kind='line', marker='o', color='g', label='CO')
guanyuan_df.groupby('hour')['PM10'].mean().plot(kind='line', marker='o', color='r', label='PM10')
guanyuan_df.groupby('hour')['SO2'].mean().plot(kind='line', marker='o', color='m', label='SO2')
guanyuan_df.groupby('hour')['NO2'].mean().plot(kind='line', marker='o', color='y', label='NO2')
guanyuan_df.groupby('hour')['O3'].mean().plot(kind='line', marker='o', color='c', label='O3')

# Menampilkan Visualisasi Fluktuasi Polutan Udasar Berdasarkan Jam dalam Sehari
st.subheader('**Fluktuasi Polutan Udasar Berdasarkan Jam dalam Sehari**:')
plt.title('Fluktuasi Polutan Udara Berdasarkan Jam dalam Sehari', fontsize=16)
plt.xlabel('Jam dalam Sehari', fontsize=14)
plt.ylabel('Konsentrasi Polutan (µg/m³)', fontsize=14)
plt.grid(True)
plt.ylim(0,200)
plt.legend()
st.pyplot(plt)


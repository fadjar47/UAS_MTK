import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title("Aplikasi Model Persediaan (EOQ)")

# Input untuk model persediaan
st.header("Model Persediaan (EOQ)")
demand = st.number_input("Masukkan permintaan tahunan:", min_value=0)
holding_cost = st.number_input("Masukkan biaya penyimpanan per unit:", min_value=0)
ordering_cost = st.number_input("Masukkan biaya pemesanan per order:", min_value=0)
unit_cost = st.number_input("Masukkan biaya per unit:", min_value=0)

if demand and holding_cost and ordering_cost and unit_cost:
    eoq = np.sqrt((2 * demand * ordering_cost) / holding_cost)
    total_cost = (demand / eoq) * ordering_cost + (eoq / 2) * holding_cost + (demand * unit_cost)

    # Menghitung persentase biaya per unit terhadap total biaya
    percentage_cost = (demand * unit_cost / total_cost) * 100 if total_cost != 0 else 0
    
    st.write(f"Jumlah Order Ekonomis (EOQ): {eoq:.2f}")
    st.write(f"Total Biaya Tahunan: {total_cost:.2f}")
    st.write(f"Persentase Biaya Per Unit terhadap Total Biaya: {percentage_cost:.2f}%")

    # Visualisasi
    plt.figure(figsize=(10, 5))
    plt.plot([1, 2, 3], [1, 2, eoq], label='EOQ')
    plt.title('Grafik EOQ')
    plt.xlabel('Waktu')
    plt.ylabel('Jumlah')
    plt.legend()
    st.pyplot(plt)

# Tambahkan dokumentasi atau instruksi di sidebar
st.sidebar.header("Instruksi")
st.sidebar.write("1. Masukkan nilai yang diperlukan.")
st.sidebar.write("2. Hasil akan ditampilkan di halaman utama.")
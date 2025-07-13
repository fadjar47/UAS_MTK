import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title("Aplikasi Model Matematika")

# Menu Tab
tabs = ["Optimasi Produksi", "Model Persediaan", "Model Antrian"]
selected_tab = st.sidebar.selectbox("Pilih Model", tabs)

if selected_tab == "Optimasi Produksi":
    st.header("Model Optimasi Produksi (Linear Programming)")
    st.write("Masukkan fungsi tujuan dan kendala.")
    # Tambahkan logika untuk optimasi produksi di sini

elif selected_tab == "Model Persediaan":
    st.header("Model Persediaan (EOQ)")
    demand = st.number_input("Masukkan permintaan tahunan:", min_value=0)
    holding_cost = st.number_input("Masukkan biaya penyimpanan per unit:", min_value=0)
    ordering_cost = st.number_input("Masukkan biaya pemesanan per order:", min_value=0)
    
    if demand and holding_cost and ordering_cost:
        eoq = np.sqrt((2 * demand * ordering_cost) / holding_cost)
        st.write(f"Jumlah Order Ekonomis (EOQ): {eoq:.2f}")

        # Visualisasi
        plt.figure(figsize=(10, 5))
        plt.plot([1, 2, 3], [1, 2, eoq], label='EOQ')
        plt.title('Grafik EOQ')
        plt.xlabel('Waktu')
        plt.ylabel('Jumlah')
        plt.legend()
        st.pyplot(plt)

elif selected_tab == "Model Antrian":
    st.header("Model Antrian (M/M/1)")
    arrival_rate = st.number_input("Masukkan laju kedatangan (λ):", min_value=0)
    service_rate = st.number_input("Masukkan laju pelayanan (μ):", min_value=0)

    if arrival_rate and service_rate:
        traffic_intensity = arrival_rate / service_rate
        st.write(f"Intensitas Lalu Lintas (ρ): {traffic_intensity:.2f}")

# Tambahkan dokumentasi atau instruksi di sidebar
st.sidebar.header("Instruksi")
st.sidebar.write("1. Pilih model dari dropdown.")
st.sidebar.write("2. Masukkan nilai yang diperlukan.")
st.sidebar.write("3. Hasil akan ditampilkan di halaman utama.")
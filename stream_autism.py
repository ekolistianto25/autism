import streamlit as st
import pickle
import pandas as pd

# Muat model pertama
with open('modelgnb.pkl', 'rb') as file:
    gnb_model = pickle.load(file)

# Muat model kedua
with open('modelsvm.pkl', 'rb') as file:
    svm_model = pickle.load(file)


# Judul web
st.title('Klasifikasi Penyakit Autisme')
# Menentukan teks dengan HTML markup untuk mengatur font
caption_text = "<div style='font-size: 12px; color: blue; text-align: left;'>Diadaptasi dari aplikasi ASDTests yang dikembangkan oleh Dr. Fadi Thabtah</div>"
# Menampilkan teks di Streamlit menggunakan st.markdown
st.markdown(caption_text, unsafe_allow_html=True)

st.markdown('#### Pertanyaan Ciri-Ciri Perilaku')
A1_Score_input = st.selectbox('Apakah pasien cenderung memperhatikan suara-suara kecil di sekitarnya?', ['Sangat setuju', 'Setuju', 'Kurang setuju', 'Tidak setuju'])
# Menggunakan if-else untuk mengubah nilai A1_Score
if A1_Score_input in ['Sangat setuju', 'Setuju']:
    A1_Score = 1
else:
    A1_Score = 0
# Menampilkan nilai A1_Score
st.markdown(f"<h2 style='font-size: 10px; text-align: right;'>Nilai A1_Score: {A1_Score}</h2>", unsafe_allow_html=True)

A2_Score_input = st.selectbox('Apakah pasien cenderung lebih fokus dalam melihat gambar secara keseluruhan daripada secara rinci?', ['Sangat setuju', 'Setuju', 'Kurang setuju', 'Tidak setuju'])
# Menggunakan if-else untuk mengubah nilai A2_Score
if A2_Score_input in ['Kurang setuju', 'Tidak setuju']:
    A2_Score = 1
else:
    A2_Score = 0
# Menampilkan nilai A2_Score
st.markdown(f"<h2 style='font-size: 10px; text-align: right;'>Nilai A1_Score: {A2_Score}</h2>", unsafe_allow_html=True)

A3_Score_input = st.selectbox('Apakah pasien mampu melakukan lebih dari satu pekerjaan?', ['Sangat setuju', 'Setuju', 'Kurang setuju', 'Tidak setuju'])
# Menggunakan if-else untuk mengubah nilai A3_Score
if A3_Score_input in ['Kurang setuju', 'Tidak setuju']:
    A3_Score = 1
else:
    A3_Score = 0
# Menampilkan nilai A3_Score
st.markdown(f"<h2 style='font-size: 10px; text-align: right;'>Nilai A1_Score: {A3_Score}</h2>", unsafe_allow_html=True)

A4_Score_input = st.selectbox('Apakah pasien dapat dengan cepat beralih kembali ke pekerjaan/ tugas setelah menghadapi suatu gangguan?', ['Sangat setuju', 'Setuju', 'Kurang setuju', 'Tidak setuju'])
# Menggunakan if-else untuk mengubah nilai A4_Score
if A4_Score_input in ['Kurang setuju', 'Tidak setuju']:
    A4_Score = 1
else:
    A4_Score = 0
# Menampilkan nilai A4_Score
st.markdown(f"<h2 style='font-size: 10px; text-align: right;'>Nilai A1_Score: {A4_Score}</h2>", unsafe_allow_html=True)

A5_Score_input = st.selectbox('Ketika melakukan percakapan, apakah pasien paham apa yang dikatakan orang lain?', ['Sangat setuju', 'Setuju', 'Kurang setuju', 'Tidak setuju'])
# Menggunakan if-else untuk mengubah nilai A5_Score
if A5_Score_input in ['Kurang setuju', 'Tidak setuju']:
    A5_Score = 1
else:
    A5_Score = 0
# Menampilkan nilai A5_Score
st.markdown(f"<h2 style='font-size: 10px; text-align: right;'>Nilai A1_Score: {A5_Score}</h2>", unsafe_allow_html=True)

A6_Score_input = st.selectbox('Ketika sedang berbicara, apakah pasien dapat mengetahui jika lawan bicara sudah mulai bosan mendengarkannya?', ['Sangat setuju', 'Setuju', 'Kurang setuju', 'Tidak setuju'])
# Menggunakan if-else untuk mengubah nilai A6_Score
if A6_Score_input in ['Kurang setuju', 'Tidak setuju']:
    A6_Score = 1
else:
    A6_Score = 0
# Menampilkan nilai A6_Score
st.markdown(f"<h2 style='font-size: 10px; text-align: right;'>Nilai A1_Score: {A6_Score}</h2>", unsafe_allow_html=True)

A7_Score_input = st.selectbox('Apakah pasien kesulitan untuk memahami suatu karakter dalam sebuah cerita?', ['Sangat setuju', 'Setuju', 'Kurang setuju', 'Tidak setuju'])
# Menggunakan if-else untuk mengubah nilai A7_Score
if A7_Score_input in ['Sangat setuju', 'Setuju']:
    A7_Score = 1
else:
    A7_Score = 0
# Menampilkan nilai A7_Score
st.markdown(f"<h2 style='font-size: 10px; text-align: right;'>Nilai A1_Score: {A7_Score}</h2>", unsafe_allow_html=True)

A8_Score_input = st.selectbox('Apakah pasien tertarik untuk mengumpulkan informasi tentang kategori benda?', ['Sangat setuju', 'Setuju', 'Kurang setuju', 'Tidak setuju'])
# Menggunakan if-else untuk mengubah nilai A8_Score
if A8_Score_input in ['Sangat setuju', 'Setuju']:
    A8_Score = 1
else:
    A8_Score = 0
# Menampilkan nilai A8_Score
st.markdown(f"<h2 style='font-size: 10px; text-align: right;'>Nilai A1_Score: {A8_Score}</h2>", unsafe_allow_html=True)

A9_Score_input = st.selectbox('Apakah pasien paham dengan bahasa gerak tubuh atau ekspresi yang dilakukan oleh orang lain?', ['Sangat setuju', 'Setuju', 'Kurang setuju', 'Tidak setuju'])
# Menggunakan if-else untuk mengubah nilai A9_Score
if A9_Score_input in ['Kurang setuju', 'Tidak setuju']:
    A9_Score = 1
else:
    A9_Score = 0
# Menampilkan nilai A9_Score
st.markdown(f"<h2 style='font-size: 10px; text-align: right;'>Nilai A1_Score: {A9_Score}</h2>", unsafe_allow_html=True)

A10_Score_input = st.selectbox('Apakah pasien mengalami kesulitan ketika membantu permasalahan orang lain?', ['Sangat setuju', 'Setuju', 'Kurang setuju', 'Tidak setuju'])
# Menggunakan if-else untuk mengubah nilai A10_Score
if A10_Score_input in ['Sangat setuju', 'Setuju']:
    A10_Score = 1
else:
    A10_Score = 0
# Menampilkan nilai A10_Score
st.markdown(f"<h2 style='font-size: 10px; text-align: right;'>Nilai A1_Score: {A10_Score}</h2>", unsafe_allow_html=True)

# Menghitung total skor
total_score = A1_Score + A2_Score + A3_Score + A4_Score + A5_Score + A6_Score + A7_Score + A8_Score + A9_Score + A10_Score

# Menampilkan total skor    
st.markdown(f"<h2 style='font-size: 12px; text-align: right'>Total Skor Anda : {total_score}</h2>", unsafe_allow_html=True)

st.markdown('#### Pertanyaan Ciri-Ciri Individu')
col1, col2 = st.columns(2)
with col1:
    age_input = st.text_input('Berapakah usia anda saat ini?') 
    # Memastikan input_total_score selalu berisi nilai numerik
    if not age_input.isdigit():
        st.error('Input tidak valid. Harap masukkan angka.')
    else:
        age = int(age_input)

with col2:
    jundice_input = st.selectbox('Apakah anda mempunyai riwayat penyakit kuning?', ['Iya', 'Tidak'])
    jundice = 1 if jundice_input == 'Iya' else 0
with col1:
    austim_input = st.selectbox('Apakah dari pihak keluarga memiliki riwayat autisme?', ['Iya', 'Tidak'])
    austim = 1 if austim_input == 'Iya' else 0
with col2:
    result_input = st.text_input('Berapa hasil total dari pertanyaan ciri-ciri perilaku?:', total_score, key='total_score_input')
    # Memastikan result_input selalu berisi nilai numerik
    try:
        result = int(result_input)
    except ValueError:
        result = 0

# Fungsi prediksi untuk GNB
def predict_gnb(A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, A6_Score, A7_Score, A8_Score, A9_Score, A10_Score, age, jundice, austim, result):
    gnb_prediction = gnb_model.predict([[A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, A6_Score, A7_Score, A8_Score, A9_Score, A10_Score, age, jundice, austim, result]])

    if gnb_prediction[0] == 1:
        return 'Pasien terindikasi menderita autisme'
    else:
        return 'Pasien terindikasi tidak menderita autisme'

# Fungsi prediksi untuk SVM
def predict_svm(A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, A6_Score, A7_Score, A8_Score, A9_Score, A10_Score, age, jundice, austim, result):
    svm_prediction = svm_model.predict([[A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, A6_Score, A7_Score, A8_Score, A9_Score, A10_Score, age, jundice, austim, result]])

    if svm_prediction[0] == 1:
        return 'Pasien terindikasi menderita autisme'
    else:
        return 'Pasien terindikasi tidak menderita autisme'


# Pilihan model
selected_model = st.selectbox('Pilih Model', ['GNB', 'SVM'])

st.markdown('---')
# Tombol untuk prediksi
if st.button('Test Prediksi Autisme'):
    if selected_model == 'GNB':
        diagnosis = predict_gnb(A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, A6_Score, A7_Score, A8_Score, A9_Score, A10_Score, age, jundice, austim, result)  
    elif selected_model == 'SVM':
        diagnosis = predict_svm(A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, A6_Score, A7_Score, A8_Score, A9_Score, A10_Score, age, jundice, austim, result)  
    st.success('Hasil prediksi menggunakan model {}: {}'.format(selected_model, diagnosis))

st.markdown('---')

import streamlit as st

def home():
    # Page title and logo
    _, col2, _ = st.columns(3)

    with col2:
        st.markdown('## Binatopedia')
        st.image("./asset/logoapp.svg", width=200)

    # Welcome message
    st.markdown('''<div style="text-align: center; font-size: 18px; background-color: #dff6ff; padding: 10px; border-radius: 10px;">
        Selamat datang di <b>Binatopedia: Klasifikasi Hewan</b>! 🌿🐾 <br>
        Temukan berbagai informasi menarik tentang klasifikasi hewan. Jelajahi data yang lengkap dan akurat untuk memperluas pengetahuan kamu tentang dunia fauna!
    </div>''', unsafe_allow_html=True)

    # Divider
    st.markdown("---")

    # Interactive Guide Section
    st.markdown("### 📋 Lihat Apa yang Bisa kamu Lakukan di Sini!")

    # Interactive Section 1: Home
    # with st.expander("1. Home"):
    #     st.markdown("This is the main page where you can explore general information about the app.")

    # Bagian Interaktif 2: Klasifikasi
    with st.expander("2. Klasifikasi"):
        st.markdown("""
        - Mengunggah gambar hewan untuk diklasifikasikan.
        - Memberikan karakteristik hewan tertentu untuk mendapatkan klasifikasi yang lebih rinci.
        """)

    # Bagian Interaktif 3: Kuis
    with st.expander("3. Kuis"):
        st.markdown("""
        - Uji pengetahuan kamu dengan mengikuti kuis tentang klasifikasi hewan.
        - Jawab serangkaian pertanyaan pilihan ganda dan temukan fakta menarik di sepanjang perjalanan.
        """)

    # Bagian Interaktif 4: Tentang
    with st.expander("4. Tentang"):
        st.markdown("""
        Pelajari lebih lanjut tentang misi Binatopedia, tim di baliknya, serta dedikasi kami terhadap pemahaman klasifikasi hewan.
        """)

    # Divider
    st.markdown("---")

    # Interactive Instructions for Classification Menu
    st.markdown("### 🐾 Petunjuk Mudah: Eksplorasi Menu Klasifikasi")

    with st.expander("Langkah-Langkah Seru Menggunakan Fitur Klasifikasi"):
        st.markdown("""
        Fitur **Klasifikasi** memudahkan kamu untuk mengenali berbagai hewan melalui gambar atau karakteristik mereka. Ikuti langkah seru berikut:
        1. **Pilih tab Klasifikasi** di menu utama aplikasi.
        2. **Unggah gambar hewan** dengan format JPG, JPEG, dan PNG.
        3. **Klik tombol 'Klasifikasi Hewan'** dan biarkan sistem bekerja untuk memberikan hasil terbaik.
        4. **Temukan hasil klasifikasi yang lengkap dan akurat**, termasuk nama hewan, nama kelas, ciri-ciri dan fakta menarik.
        """)

    # Footer with Call to Action
    st.markdown("""
    <div style="text-align: center; margin-top: 20px; background-color: #d4f6ff; padding: 20px; border-radius: 10px;">
        Mudah, bukan? Mulailah sekarang dan temukan dunia hewan yang menakjubkan! 🚀
    </div>
    """, unsafe_allow_html=True)

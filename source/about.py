import streamlit as st

def about():
    """
    Fungsi untuk menampilkan halaman 'Tentang' dengan informasi latar belakang,
    tujuan, cara kerja, dan pembuat aplikasi.
    """

    # Header
    st.markdown(
        """
        <div style='background-color: #F0F8FF; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #ADD8E6;'>
            <h3 style='text-align: center;'>✨ Tentang Aplikasi ✨</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Latar Belakang
    st.markdown(
        """
        ### 📜 Latar Belakang
        Aplikasi inovatif ini dirancang untuk membantu anak-anak mempelajari dunia hewan dengan cara yang menyenangkan sekaligus memperkenalkan mereka pada teknologi modern. 
        Dengan pendekatan yang interaktif dan edukatif, aplikasi ini memungkinkan pengguna untuk mengeksplorasi berbagai jenis hewan melalui fitur unggulan seperti klasifikasi hewan berdasarkan nama, ciri-ciri fisik, dan fakta unik yang menarik. 
        Tidak hanya itu, aplikasi ini juga memanfaatkan kecanggihan **Convolutional Neural Network (CNN)**, sebuah teknologi kecerdasan buatan yang mampu mengenali dan mengklasifikasikan hewan dengan tingkat akurasi tinggi, sehingga memberikan pengalaman belajar yang cerdas dan relevan.  
        \n
        Untuk mendukung pengalaman pengguna yang optimal, aplikasi ini dilengkapi dengan antarmuka yang sederhana namun interaktif, dibangun menggunakan framework modern **Streamlit**. Dengan desain yang ramah pengguna, anak-anak dapat dengan mudah menavigasi fitur yang ada, menjadikan proses belajar tidak hanya efektif tetapi juga menyenangkan. 
        Kombinasi teknologi canggih dan tampilan visual yang menarik menjadikan aplikasi ini alat edukasi yang ideal untuk menumbuhkan rasa ingin tahu anak-anak tentang dunia hewan sambil mengenalkan mereka pada potensi teknologi masa kini.
        """
    )

    # Tujuan
    st.markdown(
        """
        ### 🎯 Tujuan
        1. Menyediakan informasi akurat tentang klasifikasi hewan yang mudah dipahami.
        2. Memberikan pengalaman belajar yang interaktif melalui kuis dan fitur menarik lainnya.
        3. Meningkatkan wawasan masyarakat tentang keberagaman fauna di dunia.
        """
    )

    # Pembuat
    st.markdown(
        """
        ### 👩‍💻 Pembuat
        Aplikasi ini dikembangkan oleh individu yang berdedikasi pada teknologi dan edukasi. Berikut adalah informasi pengembang:
        """
    )

    # Foto Pembuat dengan Frame Bulat
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{convert_image_to_base64('./asset/profile.jpg')}" 
                    style="border-radius: 10px; border: 1px solid #ADD8E6; max-width: 150px;" 
                    alt="Foto Pembuat">
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            - **Nama**: Naia Shaffa Camila  
            - **Email**: naiashaffa.2022@student.uny.ac.id 
            - **Versi**: 0.8
            - **Dosen Pembimbing**: Akhsin Nurlayli, S.Pd., M.Eng.  
            Saya berharap aplikasi ini bermanfaat bagi banyak orang. Terima kasih telah menggunakan aplikasi ini!
            """
        )
        
    # Footer
    st.markdown(
        """
        <p style='text-align: center; font-size: 12px; font-family: Arial, sans-serif; color: #333; margin-top: 20px;'>
            <strong>© 2024 Binatopedia</strong>. Semua hak cipta dilindungi.
        </p>
        """,
        unsafe_allow_html=True,
    )


    
def convert_image_to_base64(image_path):
    """
    Konversi gambar menjadi base64 untuk ditampilkan di HTML.
    """
    import base64
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
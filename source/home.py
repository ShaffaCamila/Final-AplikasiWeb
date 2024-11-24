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

    # Bagian Interaktif 2: Classification
    with st.expander("2. Classification"):
        st.markdown("""
        - Mengunggah gambar hewan untuk diklasifikasikan.
        - Tercantum informasi tentang hewan yang telah diklasifikasikan.
        """)

    # Bagian Interaktif 3: Quiz
    with st.expander("3. Quiz"):
        st.markdown("""
        - Uji pengetahuan kamu dengan mengikuti kuis tentang klasifikasi hewan.
        - Jawab serangkaian pertanyaan pilihan ganda dan lihat hasil mu.
        """)

    # Bagian Interaktif 4: About
    with st.expander("4. About"):
        st.markdown("""
        Pelajari lebih lanjut tentang misi Binatopedia dan tim di baliknya.
        """)

    # Divider
    st.markdown("---")

    # Interactive Instructions for Classification Menu
    st.markdown("### 🐾 Petunjuk Mudah: Eksplorasi Menu Classification")

    with st.expander("Langkah-Langkah Seru Menggunakan Fitur Classification"):
        st.markdown("""
        Fitur **Classification** memudahkan kamu untuk mengenali berbagai hewan melalui gambar atau karakteristik mereka. Ikuti langkah seru berikut:
        1. **Pilih tab Classification** di menu utama aplikasi.
        2. **Unggah gambar hewan** dengan format JPG, JPEG, dan PNG.
        3. **Klik tombol 'Klasifikasi Hewan'** dan biarkan sistem bekerja untuk memberikan hasil terbaik.
        4. **Temukan hasil klasifikasi yang lengkap dan akurat**, termasuk nama hewan, nama kelas, ciri-ciri dan fakta menarik.
        """)

    # Divider
    st.markdown("---")

    # Judul Utama
    st.markdown("### 🌟 Penjelasan Kelas Hewan")

    # **Invertebrata**
    st.markdown("#### 🐜 **Invertebrata**")
    with st.expander("**Insecta**"):
        st.markdown("""
        Kelas **Insecta** merupakan kelompok invertebrata (hewan tanpa tulang belakang) terbesar di dunia, mencakup lebih dari 1 juta spesies.

        #### **Ciri-Ciri Umum Insecta**
        1. Tubuh terdiri dari tiga bagian utama: **kepala**, **toraks**, dan **abdomen**.
        2. Memiliki **tiga pasang kaki** (total enam kaki).
        3. Sebagian besar memiliki **dua pasang sayap**, tetapi ada yang tidak bersayap (seperti kutu).
        4. Bernapas menggunakan sistem **trakea**.
        5. Sistem peredaran darah terbuka.
        6. Memiliki mata majemuk dan antena untuk mendeteksi lingkungan.
        """)

    # **Vertebrata**
    st.markdown("#### 🦴 **Vertebrata**")
    # Penjelasan Aves
    with st.expander("**Aves**"):
        st.markdown("""
        Kelas Aves merupakan anggota Vertebrata yang memiliki ciri khas, yaitu tubuh ditutupi oleh bulu yang berasal dari epidermis. 
        Anggota kelas Aves umumnya memiliki alat gerak berupa sayap yang digunakan untuk terbang.

        #### **Ciri-Ciri Umum Aves**
        1. Habitat di rawa-rawa, padang rumput, pesisir pantai, tengah lautan, gua-gua batu, perkotaan, dan wilayah kutub.
        2. Simetri bilateral.
        3. Triploblastik.
        4. Homoiterm (berdarah panas).
        5. Memiliki sepasang sayap yang umumnya digunakan untuk terbang dan sepasang kaki untuk berjalan.
        6. Tubuh ditutupi bulu dari keratin kecuali kaki dan paruh. Bulu burung berganti minimal sekali dalam setahun.
        7. Bentuk paruh disesuaikan dengan jenis makanan.
        8. Tulang berongga untuk meringankan tubuh Aves.
        9. Peredaran darah tertutup.
        10. Jantung terbagi menjadi 4 ruang (2 serambi dan 2 bilik).
        """)

    # Penjelasan Amphibia
    with st.expander("**Amphibia**"):
        st.markdown("""
        Amphibia berasal dari bahasa Yunani, yaitu *amphi* yang berarti **kedua** dan *bios* yang berarti **hidup**. Kelas Amphibia merupakan hewan yang dapat hidup di dua alam, yaitu darat dan air tawar, tetapi tidak hidup di air laut.

        #### **Ciri-Ciri Umum Amphibia**
        1. Tubuh terdiri dari kepala dan badan untuk katak, namun saat masih berudu memiliki ekor.
        2. Tubuh terdiri dari kepala, badan, dan ekor untuk salamander.
        3. Tubuh dilapisi oleh kulit berlendir.
        4. Pada kepala katak terdapat kelopak mata dan membran niktitan (selaput/membran pelindung mata saat katak berenang di air).
        5. Lidah katak dapat dijulurkan panjang untuk menangkap mangsa.
        6. Simetri bilateral.
        7. Selomata (memiliki rongga tubuh sejati).
        8. Triploblastik (memiliki tiga lapisan embrionik).
        9. Poikiloterm (berdarah dingin, suhu tubuh tergantung lingkungan).
        10. Sistem peredaran darah tertutup.
        """)

    # Penjelasan Pisces
    with st.expander("**Pisces**"):
        st.markdown("""
        Kelas Pisces (ikan) adalah kelas dari subfilum Vertebrata yang seluruh anggotanya hidup di air (akuatik), baik air tawar maupun air laut.

        #### **Ciri-Ciri Umum Pisces**
        1. Habitat di perairan.
        2. Triploblastik (memiliki tiga lapisan embrionik).
        3. Selomata (memiliki rongga tubuh sejati).
        4. Struktur tubuh terdiri dari kepala (mengandung otak), badan, dan ekor.
        5. Memiliki gurat sisi untuk merasakan tekanan air.
        6. Badan berotot yang mengelilingi rongga berisi organ internal.
        7. Kulit dilengkapi dengan kelenjar penghasil lendir agar licin, sering tertutup sisik.
        8. Memiliki otot ekor post-anal yang membantu pergerakan di air.
        9. Bernapas menggunakan insang berbentuk lembaran tipis berwarna merah muda dan selalu lembap.
        10. Jantung terdiri dari dua ruangan, yaitu satu serambi dan satu bilik.
        """)

    # Penjelasan Reptil
    with st.expander("**Reptil**"):
        st.markdown("""
        Reptilia berasal dari bahasa Latin, yaitu *repto* yang berarti **melata**. Reptilia meliputi hewan-hewan seperti kadal, tokek, buaya, kura-kura, atau cicak. 
        Anggota Reptilia cenderung beradaptasi dengan kehidupan darat, namun ada juga yang hidup di perairan seperti rawa, sungai, danau, atau laut.

        #### **Ciri-Ciri Umum Reptilia**
        1. Habitat di darat atau air.
        2. Simetri bilateral.
        3. Triploblastik.
        4. Poikiloterm (berdarah dingin).
        5. Eksotermik (bergantung pada suhu lingkungan).
        6. Tubuh terdiri dari kepala, leher, badan, dan ekor.
        7. Tubuh ditutupi sisik dari keratin sehingga kedap air dan mencegah dehidrasi.
        8. Memiliki 4 kaki untuk melata, kecuali ular.
        9. Alat pencernaan lengkap.
        """)

    # Penjelasan Mammalia
    with st.expander("**Mammalia**"):
        st.markdown("""
        Mammalia berasal dari bahasa Latin, yaitu *mamae* yang berarti **susu**. Kelas Mammalia meliputi hewan yang memiliki kelenjar susu pada hewan betinanya, 
        sedangkan kelenjar susu pada hewan jantan mengalami reduksi (menyusut).

        #### **Ciri-Ciri Umum Mammalia**
        1. Habitat di darat (beberapa spesies juga hidup di air seperti paus dan lumba-lumba).
        2. Memiliki kelenjar susu untuk menyusui anak-anaknya.
        3. Simetri bilateral.
        4. Selomata (memiliki rongga tubuh sejati).
        5. Triploblastik (memiliki tiga lapisan embrionik).
        6. Tubuh ditutupi oleh rambut, yang berfungsi untuk menjaga suhu tubuh.
        7. Homoiterm (berdarah panas, mampu mengatur suhu tubuh).
        8. Alat gerak digunakan untuk berjalan, berenang, atau memegang sesuatu.
        9. Beberapa spesies memiliki kuku atau cakar, terutama pada mamalia pemanjat.
        10. Memiliki struktur gigi yang lengkap, yaitu:
            - Gigi taring untuk mencabik makanan.
            - Gigi seri untuk memotong.
            - Gigi geraham untuk menggiling makanan.
        """)

    # Footer with Call to Action
    st.markdown("""
    <div style="text-align: center; margin-top: 20px; background-color: #d4f6ff; padding: 20px; border-radius: 10px;">
        Mudah, bukan? Mulailah sekarang dan temukan dunia hewan yang menakjubkan! 🚀
    </div>
    """, unsafe_allow_html=True)

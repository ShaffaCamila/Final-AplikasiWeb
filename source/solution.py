import streamlit as st

def solution(animal_name):
    # Animal-specific details
    def antelope():
        st.subheader("Antelope")
        st.markdown("""
        **Kelas:** Mamalia  
        **Ciri-ciri:**  
        - Hewan berkuku genap.  
        - Memiliki tubuh ramping dengan tanduk melengkung.  
        - Hidup di padang rumput atau savana.  
        **Fakta unik:** Antelope adalah pelari cepat; beberapa spesies seperti pronghorn dapat berlari hingga kecepatan 90 km/jam.
        """)

    def badger():
        st.subheader("Badger || Luwak")
        st.markdown("""
        **Kelas:** Mamalia  
        **Ciri-ciri:**  
        - Bertubuh kekar dengan cakar kuat untuk menggali.  
        - Aktif di malam hari (nokturnal).  
        - Hidup di liang bawah tanah.  
        """)
        st.markdown("""**Fakta unik:** Badger terkenal karena keberaniannya; bahkan hewan besar seperti serigala sering menghindarinya.""")
    
    def bat():
        st.subheader("Bat || Kelelawar")
        st.markdown("""
        **Kelas:** Mamalia  
        **Ciri-ciri:**  
        - Satu-satunya mamalia yang bisa terbang.
        - Menggunakan ekolokasi untuk navigasi.
        - Memakan buah, serangga, atau nektar tergantung spesies.
        """)
        st.markdown("""**Fakta unik:** Koloni kelelawar terbesar di dunia ada di gua Bracken, Texas, dengan jumlah lebih dari 20 juta kelelawar.""")

    def bear():
        st.subheader("Bear || Beruang")
        st.markdown("""
        **Kelas:** Mamalia  
        **Ciri-ciri:**  
        - Tubuh besar, bulu tebal, dan cakar tajam.
        - Omnivora, memakan buah, daging, hingga madu.
        - Biasanya hidup soliter kecuali induk dengan anaknya.
        """)
        st.markdown("""**Fakta unik:** Beruang kutub dapat mencium bau anjing laut hingga jarak 1 km melalui es tebal.""")
    
    
    def bee():
        st.subheader("Bee || Lebah")
        st.markdown("""
        **Kelas:** Insecta   
        **Ciri-ciri:**  
        - Tubuh bersegmen dengan sayap transparan.
        - Hidup dalam koloni dengan hierarki sosial (ratu, pekerja, prajurit).
        - Memiliki sengatan untuk pertahanan.
        """)
        st.markdown("""**Fakta unik:** Lebah madu adalah satu-satunya serangga yang menghasilkan makanan yang dikonsumsi manusia (madu).""")

    
    def beetle():
        st.subheader("Beetle || Kumbang")
        st.markdown("""
        **Kelas:** Insecta   
        **Ciri-ciri:**  
        - Memiliki tubuh keras dengan eksoskeleton.
        - Sayap depan keras (elytra) melindungi sayap belakang.       
        """)
        st.markdown("""**Fakta unik:** Kumbang Hercules dapat mengangkat benda 850 kali berat tubuhnya!""")

    def bison():
        st.subheader("Bison")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh besar dengan punuk di punggungnya.
        - Hewan herbivora yang hidup di padang rumput.       
        """)
        st.markdown("""**Fakta unik:** Bison Amerika hampir punah pada abad ke-19, tetapi program konservasi berhasil menyelamatkan mereka.""")
        
    def boar():
        st.subheader("Boar || Babi Hutan")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh kekar dengan bulu kasar.
        - Gigi taring panjang sebagai alat pertahanan.       
        """)
        st.markdown("""**Fakta unik:** Babi hutan sangat adaptif dan bisa hidup di hampir semua habitat.""")
    
    def butterfly():
        st.subheader("Butterfly || Kupu-Kupu ")
        st.markdown("""
        **Kelas:** Insecta    
        **Ciri-ciri:**  
        - Tubuh ringan dengan sayap berwarna-warni.
        - Mengalami metamorfosis dari ulat menjadi kupu-kupu.       
        """)
        st.markdown("""**Fakta unik:** Beberapa kupu-kupu, seperti Monarch, bermigrasi ribuan kilometer setiap tahun.""")

    def cat():
        st.subheader("Cat || Kucing ")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Hewan karnivora kecil dengan tubuh fleksibel.
        - Dikenal karena penglihatannya yang tajam di malam hari.       
        """)
        st.markdown("""**Fakta unik:** Kucing mampu menghasilkan lebih dari 100 jenis suara.""")
        
    def caterpillar():
        st.subheader("Caterpillar || Ulat ")
        st.markdown("""
        **Kelas:** Insecta    
        **Ciri-ciri:**  
        - Tubuh berbentuk silindris dan lunak.
        - Memiliki kaki semu untuk bergerak.       
        """)
        st.markdown("""**Fakta unik:** Ulat makan terus-menerus untuk mengumpulkan energi sebelum menjadi kepompong.""")
        
    def chimpanzee():
        st.subheader("Chimpanzee")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Hewan primata cerdas dengan kemampuan menggunakan alat.
        - Hidup di hutan tropis.       
        """)
        st.markdown("""**Fakta unik:** DNA simpanse mirip dengan manusia hingga 98%.""")
        
    def cockroach ():
        st.subheader("cockroach  || Kecoak")
        st.markdown("""
        **Kelas:** Insecta    
        **Ciri-ciri:**  
        - Tubuh pipih dengan antena panjang.
        - Sangat adaptif terhadap lingkungan.       
        """)
        st.markdown("""**Fakta unik:** Kecoak dapat hidup selama seminggu tanpa kepala!""")
        
    def cow():
        st.subheader("Cow || Sapi")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Merupakan hewan pemakan tumbuhan atau disebut herbivora.
        - Ada beberapa jenis sapi yang memiliki tanduk, contohnya Sapi Bali dan Sapi Madura       
        """)
        st.markdown("""**Fakta unik:** Sapi dapat mengenali wajah hingga 50 individu dalam kawanan.""")

    def coyote():
        st.subheader("Coyote")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh mirip anjing dengan bulu kecokelatan.
        - Pemakan daging dan juga tumbuhan disebut Omnivora 
        """)
        st.markdown("""**Fakta unik:** Coyote dapat beradaptasi di kota besar, termasuk Los Angeles.""")

    def crab():
        st.subheader("Crab || Kepiting")
        st.markdown("""
        **Kelas:** Pisces    
        **Ciri-ciri:**  
        - Hidup di laut, sungai, atau darat.
        - MemilKepiting dapat meregenerasi kaki atau penjepit yang hilang saat bertarung atau melindungi diri.       
        """)
        st.markdown("""**Fakta unik:** Beberapa kepiting, seperti kepiting kelapa dapat memanjat pohon.""")

    def crow():
        st.subheader("Crow || Gagak")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Bulu hitam dan suara serak.
        - Burung cerdas yang bisa menggunakan alat.       
        """)
        st.markdown("""**Fakta unik:** Gagak dapat mengingat wajah manusia yang dianggap ancaman.""")

    def deer():
        st.subheader("Deer || Rusa")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Herbivora yang hidup di padang rumput atau hutan.
        - Hewan dengan tanduk bercabang (jantan).        
        """)
        st.markdown("""**Fakta unik:** """)

    def dog():
        st.subheader("Dog || Anjing")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Hewan yang setia.
        - Memiliki variasi bentuk dan ukuran.       
        """)
        st.markdown("""**Fakta unik:** Anjing dapat memahami hingga 250 kata dan perintah manusia.""")

    def dolphin():
        st.subheader("Dolphin || Lumba-lumba")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Bernapas menggunakan paru-paru.
        - Merupakan binatang menyusui yang memberikan anak makanan.       
        """)
        st.markdown("""**Fakta unik:** Lumba-lumba tidur dengan satu sisi otak aktif untuk tetap sadar terhadap ancaman.""")

    def donkey():
        st.subheader("Donkey || Keledai")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Hewan herbivora dengan tubuh kekar dan telinga panjang.
        - Digunakan untuk membawa beban sejak zaman kuno.       
        """)
        st.markdown("""**Fakta unik:** Keledai memiliki ingatan tajam dan dapat mengingat lokasi atau teman hingga 25 tahun.""")

    def dragonfly():
        st.subheader("Dragonfly || Capung")
        st.markdown("""
        **Kelas:** Insecta    
        **Ciri-ciri:**  
        - Sayap transparan dan tubuh panjang.
        - Predator yang memakan serangga kecil.       
        """)
        st.markdown("""**Fakta unik:** Capung memiliki kemampuan terbang ke segala arah, termasuk mundur.""")

    def duck():
        st.subheader("Duck || Bebek")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Paruh lebar dan kaki berselaput.
        - Hidup di air tawar dan pesisir.       
        """)
        st.markdown("""**Fakta unik:** Suara bebek tidak menghasilkan gema.""")

    def eagle():
        st.subheader("Eagle || Elang")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Burung besar dengan penglihatan tajam.
        - Predator puncak dengan cakar kuat.       
        """)
        st.markdown("""**Fakta unik:** Elang dapat melihat mangsa sejauh 3,2 km.""")

    def elephant():
        st.subheader("Elephant || Gajah")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh besar, belalai panjang, dan gading. 
        - Herbivora yang hidup dalam kawanan.       
        """)
        st.markdown("""**Fakta unik:** Gajah adalah salah satu dari sedikit hewan yang memiliki kemampuan mengenali dirinya di cermin.""")

    def flamingo():
        st.subheader("Flamingo")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh merah muda dengan kaki panjang.
        - Hidup di danau dangkal atau rawa asin.       
        """)
        st.markdown("""**Fakta unik:** Warna merah muda flamingo berasal dari pigmen karotenoid yang mereka konsumsi.""")

    def fly():
        st.subheader("Fly || Lalat")
        st.markdown("""
        **Kelas:** Insecta    
        **Ciri-ciri:**  
        - Tubuh kecil dengan sayap transparan.
        - Hidup pendek, biasanya hanya beberapa minggu.       
        """)
        st.markdown("""**Fakta unik:** Lalat memiliki mata majemuk yang dapat mendeteksi gerakan lebih cepat daripada manusia.""")
        
    def fox():
        st.subheader("Fox || Rubah")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh kecil hingga sedang dengan ekor lebat.
        - Karnivora, tetapi juga memakan buah.       
        """)
        st.markdown("""**Fakta unik:** Rubah menggunakan medan magnet bumi untuk berburu.""")
 
    def goat():
        st.subheader("Goat || Kambing")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh ramping dengan tanduk melengkung.
        - Herbivora yang memakan hampir semua jenis tumbuhan.       
        """)
        st.markdown("""**Fakta unik:** Kambing dapat mengenali emosi kambing lain dari suara mereka.""")
        
    def goldfish():
        st.subheader("Goldfish || Ikan Mas")
        st.markdown("""
        **Kelas:** Pisces   
        **Ciri-ciri:**  
        - Hidup di air tawar.
        - Ikan kecil dengan tubuh berwarna cerah.       
        """)
        st.markdown("""**Fakta unik:** Ikan mas memiliki ingatan yang lebih baik dari yang diperkirakan dan dapat mengingat pola hingga 5 bulan.""")
        
    def goose():
        st.subheader("Goose || Angsa")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Hidup di sekitar air.
        - Tubuh besar, paruh panjang, dan kaki berselaput       
        """)
        st.markdown("""**Fakta unik:** Angsa bermigrasi dalam formasi "V" untuk menghemat energi.""")
        
    def gorilla():
        st.subheader("Gorilla")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Herbivora yang tinggal di hutan tropis.
        - Primata besar dengan tubuh kekar.       
        """)
        st.markdown("""**Fakta unik:** Gorilla berbicara dengan isyarat tangan sederhana dalam kelompoknya.""") 
        
    def grasshopper ():
        st.subheader("Grasshopper || Belalang")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh panjang dengan kaki belakang kuat untuk melompat.
        - Herbivora, memakan daun atau rumput.       
        """)
        st.markdown("""**Fakta unik:** Belalang dapat mendeteksi getaran tanah dengan kakinya.""")    

    def hamster():
        st.subheader("Hamster")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh kecil berbulu halus.
        - Herbivora yang suka menggali.      
        """)
        st.markdown("""**Fakta unik:** Hamster menyimpan makanan di pipinya yang elastis.""")    

    def hare():
        st.subheader("Hare || Kelinci Liar")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh lebih besar dan telinga lebih panjang dibandingkan kelinci biasa.
        - Pelari cepat untuk menghindari predator.      
        """)
        st.markdown("""**Fakta unik:** Beberapa spesies kelinci liar berubah warna menjadi putih di musim dingin.""")    
        
    def hedgehog():
        st.subheader("Hedgehog || Landak")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh kecil dengan duri keras.
        - Melindungi diri dengan menggulung tubuh menjadi bola.       
        """)
        st.markdown("""**Fakta unik:** Landak dikenal sebagai hewan anti-racun karena kekebalannya terhadap beberapa jenis racun ular.""")           

    def hippopotamus():
        st.subheader("Hippopotamus || Kuda Nil")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh besar dengan kulit tebal.
        - Hidup di perairan tawar.       
        """)
        st.markdown("""**Fakta unik:** Keringat kuda nil berfungsi sebagai tabir surya alami""")    


    def hornbill ():
        st.subheader("Hornbill || Rangkong")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Hidup di hutan tropis
        - Paruhnya yang besar, bentuknya khas, dan warnanya mencolok        
        """)
        st.markdown("""**Fakta unik:** Rangkong jantan mengurung betina di sarang untuk melindungi mereka saat bertelur.""")    

    def horse():
        st.subheader("Horse || Kuda")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh besar dengan kaki kuat. 
        - Digunakan untuk transportasi atau olahraga.       
        """)
        st.markdown("""**Fakta unik:** Kuda dapat tidur berdiri berkat struktur kakinya yang unik.""")    

    def hummingbird ():
        st.subheader("Hummingbird  || Burung Kolibri")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Burung kecil dengan kemampuan terbang di tempat
        - Memakan nektar bunga.       
        """)
        st.markdown("""**Fakta unik:** Kolibri adalah satu-satunya burung yang bisa terbang mundur.""")    

    def hyena():
        st.subheader("Hyena || Hiena")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh kekar dengan rahang kuat. 
        - Karnivora yang juga pemakan bangkai.       
        """)
        st.markdown("""**Fakta unik:** Suara tertawa hiena sebenarnya adalah bentuk komunikasi kompleks.""")    

    def jellyfish():
        st.subheader("Jellyfish || Ubur-Ubur")
        st.markdown("""
        **Kelas:** Invertebrata     
        **Ciri-ciri:**  
        - Tubuh transparan tanpa tulang.
        - Hidup di laut.       
        """)
        st.markdown("""**Fakta unik:**Beberapa spesies ubur-ubur bisa hidup abadi dengan regenerasi sel.""")    

    def kangaroo():
        st.subheader("Kangaroo || Kanguru")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Hewan marsupial (memiliki kantung di perut untuk anaknya).
        - Kaki belakang panjang untuk melompat.       
        """)
        st.markdown("""**Fakta unik:** Kanguru tidak bisa berjalan mundur karena struktur anatomi kakinya.""")    

    def koala():
        st.subheader("Koala")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Marsupial kecil dengan bulu lebat.
        - Memakan daun eukaliptus sebagai makanan utama.       
        """)
        st.markdown("""**Fakta unik:** Koala tidur hingga 20 jam sehari karena metabolisme lambat akibat diet rendah energi.""")    
        
    def ladybugs():
        st.subheader("Ladybugs || Kepik")
        st.markdown("""
        **Kelas:** Insecta    
        **Ciri-ciri:**  
        - Tubuh kecil, biasanya berwarna merah dengan bintik hitam.
        - Predator serangga kecil seperti kutu daun.       
        """)
        st.markdown("""**Fakta unik:** Kepik dianggap pembawa keberuntungan dalam banyak budaya.""")    

    def leopard():
        st.subheader("Leopard || Macan Tutul")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Karnivora yang pandai memanjat pohon.
        - Tubuh kekar dengan pola bintik roset di bulunya.       
        """)
        st.markdown("""**Fakta unik:**  Leopard sering menyimpan mangsanya di atas pohon untuk menghindari pemangsa lain.""")    
        
    def lion():
        st.subheader("Lion || Singa")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh besar dengan surai pada jantan.
        - Hidup dalam kelompok yang disebut kawanan.       
        """)
        st.markdown("""**Fakta unik:** Singa betina adalah pemburu utama dalam kawanan, sedangkan jantan melindungi wilayahnya.""")    

    def lizard():
        st.subheader("Lizard || Kadal")
        st.markdown("""
        **Kelas:** Reptilia   
        **Ciri-ciri:**  
        - Berdarah dingin.
        - Tubuh bersisik, sebagian memiliki kemampuan memutuskan ekor (autotomi).       
        """)
        st.markdown("""**Fakta unik:** Beberapa kadal, seperti bunglon, dapat mengubah warna tubuhnya untuk kamuflase.""")    
        
    def lobster():
        st.subheader("Lobster")
        st.markdown("""
        **Kelas:** Pisces    
        **Ciri-ciri:**  
        - Hidup di dasar laut. 
        - Memiliki eksoskeleton keras dan sepasang capit besar.       
        """)
        st.markdown("""**Fakta unik:**  Lobster dapat hidup hingga lebih dari 100 tahun dan terus tumbuh sepanjang hidupnya.""")    

    def mosquito():
        st.subheader("Mosquito || Nyamuk")
        st.markdown("""
        **Kelas:** Insecta    
        **Ciri-ciri:**  
        - Tubuh kecil dengan proboscis untuk menghisap darah
        - Menularkan penyakit seperti malaria atau demam berdarah.       
        """)
        st.markdown("""**Fakta unik:** Hanya nyamuk betina yang menggigit, karena membutuhkan darah untuk bertelur.""")            

    def moth():
        st.subheader("Moth || Ngengat")
        st.markdown("""
        **Kelas:** Insecta    
        **Ciri-ciri:**  
        - Aktif di malam hari (nokturnal).
        - Sayap besar, sering kali bercorak menarik.       
        """)
        st.markdown("""**Fakta unik:** Beberapa ngengat tidak memiliki mulut dan hanya hidup untuk berkembang biak.""")   

    def mouse():
        st.subheader("Mouse || Tikus")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh kecil dengan ekor panjang.
        - Omnivora, sering memakan sisa makanan manusia.       
        """)
        st.markdown("""**Fakta unik:** Tikus memiliki kemampuan melompat dan memanjat yang luar biasa.""")            

    def octopus():
        st.subheader("Octopus || Gurita")
        st.markdown("""
        **Kelas:** Insecta    
        **Ciri-ciri:**  
        - Memiliki delapan lengan dengan cawan hisap.
        - Sangat cerdas, mampu memecahkan teka-teki sederhana.       
        """)
        st.markdown("""**Fakta unik:** Gurita memiliki tiga jantung, dan darahnya berwarna biru karena mengandung tembaga.""")   

    def okapi():
        st.subheader("Okapi")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh mirip kuda dengan pola belang seperti zebra di kaki belakang.
        - Hidup di hutan tropis Afrika.       
        """)
        st.markdown("""**Fakta unik:** Okapi adalah kerabat dekat jerapah, meskipun ukurannya jauh lebih kecil.""")            

    def orangutan():
        st.subheader("Orangutan")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Hidup di hutan tropis Asia Tenggara. 
        - Primata besar dengan lengan panjang.       
        """)
        st.markdown("""**Fakta unik:** Orangutan membuat sarang baru di pohon setiap malam untuk tidur.""")   

    def otter():
        st.subheader("Otter || Berang-berang")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh ramping dengan bulu tahan air.
        - Hidup di perairan tawar atau laut.       
        """)
        st.markdown("""**Fakta unik:** Berang-berang laut menggunakan batu untuk memecahkan kerang, menjadikannya salah satu hewan yang menggunakan alat.""")            

    def owl():
        st.subheader("Owl || Burung Hantu")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Nokturnal, berburu di malam hari.
        - Kepala besar dengan mata besar menghadap ke depan.       
        """)
        st.markdown("""**Fakta unik:** Burung hantu dapat memutar kepalanya hingga 270 derajat.""")   

    def ox():
        st.subheader("Ox || Sapi Jantan")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Herbivora, memakan rumput.
        - Tubuh besar, sering digunakan sebagai hewan pekerja.       
        """)
        st.markdown("""**Fakta unik:** Tubuh besar, sering digunakan sebagai hewan pekerja.""")            

    def oyster():
        st.subheader("Oyster || Tiram")
        st.markdown("""
        **Kelas:** Invertebrata    
        **Ciri-ciri:**  
        - Hidup dalam cangkang keras di dasar laut. 
        - Menyaring air untuk mendapatkan makanan.       
        """)
        st.markdown("""**Fakta unik:** Tiram dapat menghasilkan mutiara sebagai respons terhadap iritasi.""")   
        
    def panda():
        st.subheader("Panda")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh besar dengan bulu hitam dan putih.
        - Memakan bambu sebagai makanan utama.       
        """)
        st.markdown("""**Fakta unik:** Panda dapat menghabiskan hingga 14 jam sehari hanya untuk makan bambu.""")            

    def parrot():
        st.subheader("Parrot || Burung Beo")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Pandai meniru suara manusia.
        - Bulu berwarna cerah dan paruh melengkung.       
        """)
        st.markdown("""**Fakta unik:** Beberapa burung beo dapat hidup hingga lebih dari 50 tahun.""")           
        
    def pelecaniformes():
        st.subheader("Pelecaniformes || Pelikan")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Paruh besar dengan kantong untuk menangkap ikan.
        - Hidup di perairan.       
        """)
        st.markdown("""**Fakta unik:** Pelikan dapat menyimpan hingga 3 liter air di kantung paruhnya.""")            

    def penguin():
        st.subheader("Penguin")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Tidak bisa terbang, tetapi pandai berenang.
        - Hidup di belahan bumi selatan.       
        """)
        st.markdown("""**Fakta unik:** Penguin Kaisar dapat menyelam hingga kedalaman 500 meter.""")           
        
    def pig():
        st.subheader("Pig || Babi")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh gemuk, moncong besar, dan berwarna merah muda.
        - Omnivora, memakan berbagai jenis makanan.       
        """)
        st.markdown("""**Fakta unik:** abi adalah salah satu hewan paling cerdas dan memiliki kemampuan kognitif setara dengan anak manusia berusia 3 tahun.""")            

    def pigeon():
        st.subheader("Pigeon || Merpati")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Terbang cepat dan terkenal dengan kemampuan navigasi.
        - Tubuh kecil hingga sedang dengan bulu halus.       
        """)
        st.markdown("""**Fakta unik:** Merpati dapat mengenali wajah manusia dan menemukan jalan pulang dari ratusan kilometer.""")           
        
    def porcupine():
        st.subheader("Porcupine || Landak")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh kecil dengan duri keras yang digunakan untuk pertahanan.
        - Herbivora, memakan daun, kulit kayu, dan buah.       
        """)
        st.markdown("""**Fakta unik:** Landak tidak melemparkan durinya, tetapi duri mudah menempel pada predator.""")            

    def possum():
        st.subheader("Possum")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Kemampuan "berpura-pura mati" untuk menghindari predator.
        - Marsupial kecil yang aktif di malam hari.       
        """)
        st.markdown("""**Fakta unik:** Possum memiliki kekebalan terhadap racun ular berbisa.""")                        

    def raccoon():
        st.subheader("Raccoon || Rakun")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh kecil dengan bulu abu-abu dan ekor bergaris hitam.
        - Pandai membuka benda dengan tangan depannya.       
        """)
        st.markdown("""**Fakta unik:** Raccoon mencuci makanannya sebelum dimakan, meskipun di alam liar itu hanya kebiasaan refleks.""")   
        
    def rat():
        st.subheader("Rat || Tikus")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh kecil dengan ekor panjang.
        - Omnivora, makan segala jenis makanan.       
        """)
        st.markdown("""**Fakta unik:** Tikus dapat bertahan hidup di hampir semua lingkungan, termasuk saluran pembuangan.""")            

    def reindeer():
        st.subheader("Reindeer || Rusa Kutub")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Hidup di daerah dingin seperti tundra Arktik. 
        - Memiliki tanduk bercabang, baik jantan maupun betina.       
        """)
        st.markdown("""**Fakta unik:** Hidung rusa kutub berubah warna menjadi merah karena peningkatan aliran darah saat suhu dingin.""")           
        
    def rhinoceros():
        st.subheader("Rhinoceros || Badak")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh besar, kulit tebal, dan satu atau dua cula. 
        - Herbivora, memakan rumput dan dedaunan.       
        """)
        st.markdown("""**Fakta unik:** Cula badak terbuat dari keratin, bahan yang sama dengan kuku manusia.""")            

    def sandpiper():
        st.subheader("Sandpiper || Burung Kedidi")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Tubuh kecil dengan kaki panjang.
        - Hidup di sekitar pantai atau rawa.       
        """)
        st.markdown("""**Fakta unik:** Sandpiper terkenal karena gerakannya yang cepat saat mencari makanan di pasir.""")           
        
    def seahorse():
        st.subheader("Seahorse || Kuda Laut")
        st.markdown("""
        **Kelas:** Pisces   
        **Ciri-ciri:**  
        - Tubuh kecil berbentuk unik dengan ekor melingkar.
        - Bergerak dengan sirip punggung kecil.      
        """)
        st.markdown("""**Fakta unik:** Kuda laut jantan yang mengandung dan melahirkan anak.""")            

    def seal():
        st.subheader("Seal || Anjing Laut")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh bulat dengan sirip. 
        - Hidup di laut dan pantai berbatu.       
        """)
        st.markdown("""**Fakta unik:** Anjing laut mampu menahan napas hingga 30 menit saat menyelam.""")           
        
    def shark():
        st.subheader("Shark || Hiu")
        st.markdown("""
        **Kelas:** Pisces   
        **Ciri-ciri:**  
        - Predator laut dengan gigi tajam.
        - Tubuh ramping, bersisik kecil, dan sirip besar.       
        """)
        st.markdown("""**Fakta unik:** iu tidak memiliki tulang; kerangkanya terbuat dari tulang rawan.""")            

    def sheep():
        st.subheader("Sheep || Domba")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh berbulu lebat (wol).
        - Herbivora yang hidup berkelompok.       
        """)
        st.markdown("""**Fakta unik:** Domba memiliki ingatan tajam dan dapat mengenali hingga 50 wajah domba lain.""")      

    def snake():
        st.subheader("Snake || Ular")
        st.markdown("""
        **Kelas:** Reptilia   
        **Ciri-ciri:**  
        - Tubuh panjang tanpa kaki.
        - Beberapa spesies berbisa.       
        """)
        st.markdown("""**Fakta unik:** lar bisa "melihat" panas tubuh mangsa dengan organ di sekitar wajahnya.""")           
        
    def sparrow():
        st.subheader("Sparrow || Burung Gereja")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Memakan biji dan serangga kecil.
        - Tubuh kecil, sering dijumpai di sekitar manusia.       
        """)
        st.markdown("""**Fakta unik:** Burung gereja ditemukan hampir di seluruh dunia, kecuali Antartika.""")            

    def squid():
        st.subheader("Squid || Cumi-cumi")
        st.markdown("""
        **Kelas:** Invertebrata   
        **Ciri-ciri:**  
        - Tubuh lunak dengan lengan dan tentakel.
        - Mengeluarkan tinta untuk melindungi diri.       
        """)
        st.markdown("""**Fakta unik:** Cumi-cumi raksasa dapat tumbuh hingga panjang 13 meter.""")      

    def squirrel():
        st.subheader("Squirrel || Tupai")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh kecil dengan ekor lebat.
        - Pandai memanjat pohon dan menyimpan makanan.       
        """)
        st.markdown("""**Fakta unik:** Tupai "menipu" predator dengan berpura-pura menyembunyikan makanan di lokasi palsu.""")           
        
    def starfish():
        st.subheader("Starfish || Bintang Laut")
        st.markdown("""
        **Kelas:** Invertebrata    
        **Ciri-ciri:**  
        - Hidup di dasar laut.
        - Tubuh berbentuk bintang dengan lima lengan atau lebih.       
        """)
        st.markdown("""**Fakta unik:** Bintang laut dapat meregenerasi lengan yang hilang.""")            

    def swan():
        st.subheader("Swan || Angsa")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Tubuh besar dengan leher panjang.
        - Hidup di danau dan sungai.       
        """)
        st.markdown("""**Fakta unik:** Angsa membentuk pasangan seumur hidup, menunjukkan kesetiaan tinggi.""")      
           
    def tiger():
        st.subheader("tiger || Harimau")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Predator soliter.
        - Tubuh besar dengan garis-garis hitam di bulu oranye.       
        """)
        st.markdown("""**Fakta unik:** Setiap harimau memiliki pola garis yang unik seperti sidik jari manusia.""")           
        
    def turkey():
        st.subheader("Turkey || Kalkun")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Tubuh besar dengan ekor berbulu lebar.
        - Herbivora dengan biji dan serangga sebagai makanan.       
        """)
        st.markdown("""**Fakta unik:** Kalkun dapat mengenali lebih dari 20 individu berbeda dalam kawanan.""")            

    def turtle():
        st.subheader("Turtle || Kura-kura")
        st.markdown("""
        **Kelas:** Reptilia   
        **Ciri-ciri:**  
        - Memiliki cangkang keras sebagai perlindungan.
        - Hidup di darat dan air.       
        """)
        st.markdown("""**Fakta unik:** Beberapa kura-kura dapat hidup lebih dari 100 tahun.""")      

    def whale():
        st.subheader("Whale || Paus")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh besar, hidup di laut, bernapas dengan paru-paru.
        - Memakan plankton atau ikan kecil (tergantung spesies).       
        """)
        st.markdown("""**Fakta unik:** Paus biru adalah hewan terbesar di dunia, dengan panjang hingga 30 meter dan berat 200 ton.""")            

    def wolf():
        st.subheader("Wolf || Serigala")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Karnivora, berburu dalam kelompok yang disebut kawanan. 
        - Komunikasi menggunakan auman, gerakan tubuh, dan bau.       
        """)
        st.markdown("""**Fakta unik:** Serigala dapat berlari hingga kecepatan 60 km/jam untuk mengejar mangsa.""")    

    def wombat():
        st.subheader("Wombat")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Hidup di liang bawah tanah.
        - Herbivora, memakan rumput dan tanaman kecil.       
        """)
        st.markdown("""**Fakta unik:** Kotoran wombat berbentuk kubus, membantu mereka menandai wilayah tanpa terguling oleh angin atau hujan.""")            

    def woodpecker():
        st.subheader("Woodpecker || Burung Pelatuk")
        st.markdown("""
        **Kelas:** Aves   
        **Ciri-ciri:**  
        - Paruh kuat untuk mematuk pohon saat mencari serangga atau membuat sarang.
        - Memiliki lidah panjang untuk menangkap mangsa.       
        """)
        st.markdown("""**Fakta unik:** Burung pelatuk dapat mematuk pohon hingga 20 kali per detik tanpa mengalami cedera kepala karena adanya bantalan di tengkoraknya.""")    
        
    def zebra():
        st.subheader("Zebra")
        st.markdown("""
        **Kelas:** Mamalia   
        **Ciri-ciri:**  
        - Tubuh berukuran sedang dengan pola belang hitam-putih unik. 
        - Hidup dalam kawanan untuk perlindungan dari predator.       
        """)
        st.markdown("""**Fakta unik:** Pola belang zebra berfungsi untuk membingungkan predator dan mengusir lalat dengan efek visual yang membingungkan.""")    

    # Map animal names to their respective functions
    animal_functions = {
    "antelope": antelope,
    "badger": badger,
    "bat": bat,
    "bear": bear,
    "bee": bee,
    "beetle": beetle,
    "bison": bison,
    "boar": boar,
    "butterfly": butterfly,
    "cat": cat,
    "caterpillar": caterpillar,
    "chimpanzee": chimpanzee,
    "cockroach": cockroach,
    "cow": cow,
    "coyote": coyote,
    "crab": crab,
    "crow": crow,
    "deer": deer,
    "dog": dog,
    "dolphin": dolphin,
    "donkey": donkey,
    "dragonfly": dragonfly,
    "duck": duck,
    "eagle": eagle,
    "elephant": elephant,
    "flamingo": flamingo,
    "fly": fly,
    "fox": fox,
    "goat": goat,
    "goldfish": goldfish,
    "goose": goose,
    "gorilla": gorilla,
    "grasshopper": grasshopper,
    "hamster": hamster,
    "hare": hare,
    "hedgehog": hedgehog,
    "hippopotamus": hippopotamus,
    "hornbill": hornbill,
    "horse": horse,
    "hummingbird": hummingbird,
    "hyena": hyena,
    "jellyfish": jellyfish,
    "kangaroo": kangaroo,
    "koala": koala,
    "ladybugs": ladybugs,
    "leopard": leopard,
    "lion": lion,
    "lizard": lizard,
    "lobster": lobster,
    "mosquito": mosquito,
    "moth": moth,
    "mouse": mouse,
    "octopus": octopus,
    "okapi": okapi,
    "orangutan": orangutan,
    "otter": otter,
    "owl": owl,
    "ox": ox,
    "oyster": oyster,
    "panda": panda,
    "parrot": parrot,
    "pelecaniformes": pelecaniformes,
    "penguin": penguin,
    "pig": pig,
    "pigeon": pigeon,
    "porcupine": porcupine,
    "possum": possum,
    "raccoon": raccoon,
    "rat": rat,
    "reindeer": reindeer,
    "rhinoceros": rhinoceros,
    "sandpiper": sandpiper,
    "seahorse": seahorse,
    "seal": seal,
    "shark": shark,
    "sheep": sheep,
    "snake": snake,
    "sparrow": sparrow,
    "squid": squid,
    "squirrel": squirrel,
    "starfish": starfish,
    "swan": swan,
    "tiger": tiger,
    "turkey": turkey,
    "turtle": turtle,
    "whale": whale,
    "wolf": wolf,
    "wombat": wombat,
    "woodpecker": woodpecker,
    "zebra": zebra,
}

    # Call the appropriate function based on the predicted animal
    animal_name = animal_name.lower()
    if animal_name in animal_functions:
        animal_functions[animal_name]()
    else:
        st.warning(f"⚠ Informasi tentang {animal_name.capitalize()} belum tersedia.")
import streamlit as st

def quiz():
    # Header
    st.markdown(
        """
        <div style='background-color: #F0F8FF; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #ADD8E6;'>
            <h3 style='text-align: center;'>🎉 Quiz Time! 🎉</h3>
            <p style='text-align: center;'>Uji kemampuan kamu!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Questions and options
    questions = [
        {
            "question": "Kucing, harimau dan kelinci termasuk kelompok hewan?",
            "options": ["Pisces", "Ampibi", "Reptil", "Aves", "Mamalia"],
            "answer": "Mamalia",
        },
        {
            "question": "Ayam dan musang termasuk dalam golongan hewan?",
            "options": ["Insektivora", "Herbivora", "Omnivora", "Karnivora", "Ovipar"],
            "answer": "Omnivora",
        },
        {
            "question": "Yang bukan termasuk kelompok reptilia adalah?",
            "options": ["Belalang", "Buaya", "Ular", "Kura-kura", "Kadal"],
            "answer": "Belalang",
        },
        {
            "question": "Hewan pemakan daging termasuk golongan?",
            "options": ["Herbivora", "Karnivora", "Omnivora", "Ovipar", "Ovovivipar"],
            "answer": "Karnivora",
        },
        {
            "question": "Burung, unggas dan ayam termasuk kelompok hewan?",
            "options": ["Reptil", "Aves", "Mamalia", "Pisces", "Ampibi"],
            "answer": "Aves",
        },
    ]

    # Store user answers in session state to persist across reruns
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}

    if 'all_answered' not in st.session_state:
        st.session_state.all_answered = False

    # Function to check if all questions are answered
    def check_all_answered():
        st.session_state.all_answered = all(answer is not None for answer in st.session_state.user_answers.values())

    # Display each question in a card-like layout
    for idx, q in enumerate(questions):
        with st.container():
            st.markdown(
                f"""
                <div style="background-color: #D1E9F6; padding: 15px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #AED4FF;">
                    <h4>Question {idx + 1}</h4>
                    <p>{q['question']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Radio buttons for answers, preserving state with session_state
            selected_answer = st.radio(
                f"Pilih jawaban untuk Pertanyaan {idx + 1}",
                options=q["options"],
                index=q["options"].index(st.session_state.user_answers.get(idx, None)) if idx in st.session_state.user_answers else None,
                key=f"pertanyaan_{idx}",
                on_change=check_all_answered,
            )

            # Save the selected answer in session state
            st.session_state.user_answers[idx] = selected_answer

    # Disable the submit button until all questions are answered
    submit_button = st.button("Submit", disabled=not st.session_state.all_answered)

    if submit_button:
        # Calculate score
        score = sum(
            st.session_state.user_answers[idx] == q["answer"]
            for idx, q in enumerate(questions)
        )

        # Tampilkan hasil
        st.markdown(
            f"""
            <div style='background-color: #C6E7FF; padding: 20px; border-radius: 10px; margin-top: 20px; border: 2px solid #AED4FF;'>
                <h2 style='text-align: center;'>Hasil kuis</h2>
                <p style='text-align: center; font-size: 20px;'>🎉 Kamu mendapatkan skor <strong>{score}</strong> dari <strong>{len(questions)}</strong>.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("\n")
        
        # Umpan balik berdasarkan skor
        if score == len(questions):
            st.success("Luar biasa! kamu menjawab semua pertanyaan dengan benar! 🌟🎉")
        elif score >= len(questions) / 2:
            st.info("Bagus sekali! kamu menjawab lebih dari setengah pertanyaan dengan benar. Pertahankan! 👍")
        else:
            st.warning("Jangan khawatir! Cobalah lagi untuk meningkatkan skor kamu. 💪")
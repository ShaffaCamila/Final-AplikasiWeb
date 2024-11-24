import streamlit as st

def quiz():
    # Initialize session state for user answers if not already done
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}

    # Initialize state for submission
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    # Questions and options
    questions = [
        {
            "question": "Hewan-hewan dibawah ini termasuk kelompok hewan?",
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
            "question": "Hewan pemakan rumput termasuk golongan?",
            "options": ["Karnivora", "Herbivora", "Omnivora", "Ovipar", "Ovovivipar"],
            "answer": "Herbivora",
        },
        {
            "question": "Burung, unggas dan ayam termasuk kelompok hewan?",
            "options": ["Reptil", "Aves", "Mamalia", "Pisces", "Ampibi"],
            "answer": "Aves",
        },
    ]

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

    # Form for the quiz
    with st.form(key="quiz_form"):
        # Display each question in a form
        for idx, q in enumerate(questions):
            st.markdown(
                f"""
                <div style="background-color: #D1E9F6; padding: 15px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #AED4FF;">
                    <h4>Question {idx + 1}</h4>
                    <p>{q['question']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Add image below Question 1
            if idx == 0:
                st.image("./source/gambar-soal.jpg", caption="Ilustrasi untuk pertanyaan 1", width=300)

            # Get saved answer if exists, otherwise set to None
            default_answer = st.session_state.user_answers.get(idx, None)

            # Radio buttons for answers
            selected_answer = st.radio(
                f"Pilih jawaban untuk Pertanyaan {idx + 1}",
                options=q["options"],
                index=q["options"].index(default_answer) if default_answer else None,
                key=f"radio_{idx}",
            )

            # Save the selected answer in session state
            st.session_state.user_answers[idx] = selected_answer

        # Submit button
        submit_button = st.form_submit_button("Submit")

        # Check if the form is submitted
        if submit_button:
            st.session_state.quiz_submitted = True

    # After form submission, calculate and display the score
    if st.session_state.quiz_submitted:
        score = sum(
            st.session_state.user_answers[idx] == q["answer"]
            for idx, q in enumerate(questions)
        )

        st.markdown(
            f"""
            <div style='background-color: #C6E7FF; padding: 20px; border-radius: 10px; margin-top: 20px; border: 2px solid #AED4FF;'>
                <h2 style='text-align: center;'>Hasil kuis</h2>
                <p style='text-align: center; font-size: 20px;'>🎉 Kamu mendapatkan skor <strong>{score}</strong> dari <strong>{len(questions)}</strong>.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if score == len(questions):
            st.success("Luar biasa! kamu menjawab semua pertanyaan dengan benar! 🌟🎉")
        elif score >= len(questions) / 2:
            st.info("Bagus sekali! kamu menjawab lebih dari setengah pertanyaan dengan benar. Pertahankan! 👍")
        else:
            st.warning("Jangan khawatir! Cobalah lagi untuk meningkatkan skor kamu. 💪")
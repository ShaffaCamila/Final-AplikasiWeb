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

    # Initialize answers dictionary
    user_answers = {i: None for i in range(len(questions))}

    # Form for the quiz
    with st.form(key='quiz_form'):
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

            # Radio buttons for answers
            selected_answer = st.radio(
                f"Pilih jawaban untuk Pertanyaan {idx + 1}",
                options=q["options"],
                index=q["options"].index(user_answers.get(idx)) if user_answers.get(idx) else None,
                key=f"pertanyaan_{idx}",
            )

            # Save the selected answer
            user_answers[idx] = selected_answer

        # Submit button
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        # Calculate score
        score = sum(
            user_answers[idx] == q["answer"]
            for idx, q in enumerate(questions)
        )

        # Show the result
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
        
        # Feedback based on score
        if score == len(questions):
            st.success("Luar biasa! kamu menjawab semua pertanyaan dengan benar! 🌟🎉")
        elif score >= len(questions) / 2:
            st.info("Bagus sekali! kamu menjawab lebih dari setengah pertanyaan dengan benar. Pertahankan! 👍")
        else:
            st.warning("Jangan khawatir! Cobalah lagi untuk meningkatkan skor kamu. 💪")
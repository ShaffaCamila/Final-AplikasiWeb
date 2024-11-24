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

    # Initialize score
    score = 0

    # Loop through questions
    for idx, q in enumerate(questions):
        st.subheader(f"Question {idx + 1}")
        user_answer = st.radio(q["question"], q["options"], key=f"q{idx}")

        # Check answer and update score
        if user_answer == q["answer"]:
            score += 1

    # Submit button to calculate final score
    if st.button("Submit Quiz"):
        st.write(f"Your final score is: {score}/{len(questions)}")
        if score == len(questions):
            st.success("Excellent! You got all questions correct! 🎉")
        elif score > len(questions) // 2:
            st.info("Good job! You did well! 👍")
        else:
            st.error("Keep trying! You'll get better next time. 💪")
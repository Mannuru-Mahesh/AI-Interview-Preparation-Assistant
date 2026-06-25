import streamlit as st
import pandas as pd
import plotly.express as px
import random

from question_generator import generate_questions
from answer_evaluator import evaluate_answer
from database import (
    create_tables,
    save_interview,
    get_all_interviews
)

create_tables()


st.set_page_config(
    page_title="AI Interview Preparation Assistant",
    page_icon="🎤",
    layout="wide"
)
st.markdown("""
<style>

.stApp {
    background: #F5F7FA;
}


[data-testid="stSidebar"] {
    background: #134E4A;
}

[data-testid="stSidebar"] * {
    color: white !important;
}



.main .block-container {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    margin-top: 20px;
}



h1 {
    color: #0F766E !important;
    text-align: center;
    font-size: 42px !important;
    font-weight: 700 !important;
}

h2, h3 {
    color: #0F766E !important;
    font-weight: 600 !important;
}



p, li {
    color: #1F2937 !important;
}

.stMarkdown {
    color: #1F2937 !important;
}



label {
    color: #1F2937 !important;
    font-weight: 600 !important;
}



.stTextInput input {
    background: white !important;
    color: #1F2937 !important;
    border: 2px solid #D1D5DB !important;
    border-radius: 12px !important;
}



.stTextArea textarea {
    background: white !important;
    color: #1F2937 !important;
    border: 2px solid #D1D5DB !important;
    border-radius: 12px !important;
    font-size: 16px !important;
}



/* Main Select Box */
[data-baseweb="select"] > div {
    background-color: #1E1E1E !important;
    color: white !important;
    border: 2px solid #0F766E !important;
    border-radius: 12px !important;
}

/* Selected Text */
[data-baseweb="select"] span {
    color: white !important;
    font-weight: 600 !important;
}

/* Dropdown Popup */
ul[role="listbox"] {
    background-color: #0A0A0A !important;
    border: 1px solid #333 !important;
    border-radius: 12px !important;
}

/* Dropdown Options */
li[role="option"] {
    background-color: #0A0A0A !important;
    color: white !important;
    font-weight: 500 !important;
}

/* Hover Effect */
li[role="option"]:hover {
    background-color: #1A1A1A !important;
    color: #14B8A6 !important;
}

/* Selected Option */
li[aria-selected="true"] {
    background-color: #0F766E !important;
    color: white !important;
}



.stButton button {
    background: #0F766E !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 10px 25px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

.stButton button:hover {
    background: #134E4A !important;
    color: white !important;
}

/* Download Button */

.stDownloadButton button {
    background: #0F766E !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 10px 25px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

.stDownloadButton button:hover {
    background: #134E4A !important;
    color: white !important;
}



[data-testid="metric-container"] {
    background: white;
    border-left: 5px solid #0F766E;
    border-radius: 15px;
    padding: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}



[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
}



.stSuccess {
    border-radius: 12px;
}



.stInfo {
    border-radius: 12px;
}



.question-card {
    background: #FFFFFF;
    padding: 25px;
    border-left: 6px solid #0F766E;
    border-radius: 15px;
    color: #1F2937;
    font-size: 17px;
    line-height: 1.8;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)


st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Mock Interview",
        "Interview History",
        "Dashboard Analytics"
    ]
)


if page == "Mock Interview":

    st.markdown("""
    <h1 style='text-align:center;color:#0F766E;'>
    🎤 AI Interview Preparation Assistant
    </h1>

    <p style='text-align:center;color:#6B7280;font-size:18px;'>
    Practice technical interviews with AI-powered feedback and analytics
    </p>
    """, unsafe_allow_html=True)

    st.write(
        "Practice technical interviews using AI-powered mock interviews."
    )

    candidate_name = st.text_input(
        "Candidate Name"
    )

    role = st.selectbox(
        "Select Job Role",
        [
            "Python Developer",
            "Java Developer",
            "Data Analyst",
            "Data Scientist",
            "Software Engineer"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("Generate Questions"):

        questions = generate_questions(
            role,
            difficulty
        )

        st.session_state["questions"] = questions

    if "questions" in st.session_state:

        st.subheader("Interview Questions")

        st.markdown(
            f"""
            <div class="question-card">
            <pre>{st.session_state["questions"]}</pre>
            </div>
            """,
            unsafe_allow_html=True
        )
        answer = st.text_area(
            "Enter Your Answer",
            height=250
        )

        if st.button("Evaluate Answer"):

            if answer.strip() == "":
                st.warning("Please enter your answer.")
            else:

                result = evaluate_answer(
                    st.session_state["questions"],
                    answer
                )

                score = round(random.uniform(7, 10), 1)

                if not candidate_name.strip():
                    st.warning("Please enter candidate name.")
                    st.stop()

                save_interview(
                    candidate_name,
                    role,
                    score,
                    result
                )

                st.success(
                    "Interview saved successfully!"
                )

                st.subheader(
                    "Evaluation Result"
                )

                st.write(result)


elif page == "Interview History":

    st.title("📋 Interview History")

    history = get_all_interviews()

    if history:

        df = pd.DataFrame(
            history,
            columns=[
                "ID",
                "Candidate Name",
                "Role",
                "Score",
                "Feedback",
                "Interview Date"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        csv = df.to_csv(index=False)

        st.download_button(
            label="📥 Download History CSV",
            data=csv,
            file_name="interview_history.csv",
            mime="text/csv"
        )

    else:
        st.info(
            "No interview history found."
        )


elif page == "Dashboard Analytics":

    st.title("📊 Dashboard Analytics")

    history = get_all_interviews()

    if history:

        df = pd.DataFrame(
            history,
            columns=[
                "ID",
                "Candidate Name",
                "Role",
                "Score",
                "Feedback",
                "Interview Date"
            ]
        )

        df["Score"] = pd.to_numeric(
            df["Score"],
            errors="coerce"
        )

        total_interviews = len(df)

        avg_score = round(
            df["Score"].mean(),
            2
        )

        max_score = df["Score"].max()

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Total Interviews",
            total_interviews
        )

        col2.metric(
            "Average Score",
            avg_score
        )

        col3.metric(
            "Highest Score",
            max_score
        )

        st.divider()

        st.subheader(
            "Score Distribution"
        )

        fig = px.histogram(
            df,
            x="Score"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.subheader(
            "Role Wise Interviews"
        )

        role_chart = px.pie(
            df,
            names="Role"
        )

        st.plotly_chart(
            role_chart,
            use_container_width=True
        )

        st.subheader(
            "Candidate Scores"
        )

        score_chart = px.bar(
            df,
            x="Candidate Name",
            y="Score"
        )

        st.plotly_chart(
            score_chart,
            use_container_width=True
        )

    else:

        st.info(
            "No interview data available."
        )
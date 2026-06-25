# AI Interview Preparation Assistant

## Overview

AI Interview Preparation Assistant is a Streamlit-based web application
that helps users practice technical interviews through AI-generated
questions, answer evaluation, interview history tracking, and
performance analytics.

## Features

-   Role-based interview question generation
-   Multiple difficulty levels (Beginner, Intermediate, Advanced)
-   AI-powered answer evaluation
-   Interview history stored in SQLite
-   Interactive analytics dashboard
-   CSV export of interview history
-   Performance visualization using Plotly

## Technology Stack

-   Python
-   Streamlit
-   SQLite
-   Pandas
-   Plotly Express

## Project Structure

``` text
AI_Interview_Preparation_Assistant/
│
├── app.py
├── database.py
├── question_generator.py
├── answer_evaluator.py
├── interview.db
├── requirements.txt
└── README.md
```

## Installation

``` bash
git clone https://github.com/your-username/AI_Interview_Preparation_Assistant.git
cd AI_Interview_Preparation_Assistant
python -m venv venv
```

### Activate Virtual Environment

**Windows**

``` bash
venv\Scripts\activate
```

**Linux / macOS**

``` bash
source venv/bin/activate
```

### Install Dependencies

``` bash
pip install -r requirements.txt
```

## Running the Application

``` bash
streamlit run app.py
```

Open your browser and visit:

``` text
http://localhost:8501
```

## Application Workflow

1.  Enter candidate name.
2.  Select a job role.
3.  Choose the difficulty level.
4.  Generate interview questions.
5.  Submit your answer.
6.  Receive AI-generated evaluation and score.
7.  View interview history and analytics.

## Supported Roles

-   Python Developer
-   Java Developer
-   Data Analyst
-   Data Scientist
-   Software Engineer

## Dashboard Analytics

-   Total Interviews
-   Average Score
-   Highest Score
-   Score Distribution
-   Role-wise Statistics
-   Candidate Performance

## Future Enhancements

-   Resume-based interview generation
-   Voice interview support
-   User authentication
-   Cloud database integration
-   PDF report generation

## Author

**Harika Lankalapalli**

B.Tech, Computer Science and Engineering

KL University

## License

This project is intended for educational and portfolio purposes.

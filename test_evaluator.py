from answer_evaluator import evaluate_answer

question = "What is Python?"

answer = """
Python is a programming language.
It is used in AI, Machine Learning,
Web Development and Data Science.
"""

result = evaluate_answer(question, answer)

print(result)



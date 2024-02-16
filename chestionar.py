#!/usr/bin/python3.10

# Create questionnaire

# Initialize a list to store the answers
answers = []

# Define the questions
questions = [
    "What is your name?",
    "What job do you desire?",
    "How long do you think it will take to get this job?",
    "What are the steps you need to follow to get hired?",
    "When do you want to start?",
]

# Iterate through each question and collect the answers
for question in questions:
    answer = input(question + " ")
    answers.append(answer)

# Display the results
print("\nThe candidate answered the following questions:")
for i, question in enumerate(questions):
    print(f"{question}: {answers[i]}")

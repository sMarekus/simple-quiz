# True or False Quiz

This project is a True or False quiz application that tests your knowledge on various statements. It presents a series of questions and provides immediate feedback on your answers. The quiz questions and answers are stored in a data file, and the application utilizes a question model and a quiz brain to manage the quiz process.

## Features

- The quiz consists of a set of True or False questions.
- Questions and answers are stored in a data file (`data.py`).
- The application uses a question model (`question_model.py`) to represent each question.
- The quiz brain (`quiz_brain.py`) manages the quiz process, tracks the user's score, and provides feedback.
- The user is prompted with each question and can input their answer.
- Immediate feedback is given after each question, displaying whether the answer was correct and the correct answer itself.
- The quiz continues until all questions have been answered.
- At the end of the quiz, the user's final score is displayed.

## Usage

1. Ensure you have Python installed (version 3.0 or above).
2. Clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to start the quiz:
```
python main.py
```
5. The quiz will begin, and you will be presented with each question in the console.
6. Input your answer by typing either "True" or "False" and pressing Enter.
7. Receive immediate feedback on your answer and continue to the next question.
8. Once you have answered all the questions, your final score will be displayed.

## Customization

- You can modify the questions and answers by editing the `question_data` list in `data.py`. Simply update the text and answer values for each question dictionary.
- To add more questions, append additional dictionaries to the `question_data` list following the same structure.


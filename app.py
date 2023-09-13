from flask import Flask, request, render_template, redirect
from surveys import satisfaction_survey

app = Flask(__name__)

# Initialize responses list
responses = []

@app.route('/')
def root():
    survey_title = satisfaction_survey.title
    survey_instructions = satisfaction_survey.instructions
    return render_template('base.html', survey_title=survey_title, survey_instructions=survey_instructions)

@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def show_question(question_id):
    if request.method == 'POST':
       
        answer = request.form.get('answer')
       
        responses.append(answer)

       
        if question_id + 1 < len(satisfaction_survey.questions):
            return redirect(f'/question/{question_id + 1}')
        else:
           
            return redirect('/thank-you')


    question = satisfaction_survey.questions[question_id].question
    choices = satisfaction_survey.questions[question_id].choices
    return render_template('question.html', question=question, choices=choices, question_id=question_id)

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/start-survey')
def start_survey():
    # Redirect to the first question
    return redirect('/question/0')


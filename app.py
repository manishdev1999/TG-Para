from flask import Flask, render_template, request
import logic as lg
import ssl
import nltk
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    question = request.form['question']
    results = lg.get_options_and_analyse(question, text)
    print(results)
    # do something with the text
    return render_template('result.html', text=results)


if __name__ == '__main__':
    app.run()

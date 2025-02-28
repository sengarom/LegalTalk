from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/discussion')
def discussion():
    return render_template('discussion.html')

@app.route('/case-study')
def case_study():
    return render_template('case.html')

if __name__ == '__main__':
    app.run(debug=True)
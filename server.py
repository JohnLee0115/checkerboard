from flask import Flask, render_template  # added render_template!
app = Flask(__name__)


@app.route('/')
def eight_by_eight(num1 = 8, num2 = 8):
    return render_template('index.html', num1 = num1, num2 = num2) 

@app.route('/<int:num1>')
def eight_by_num1(num1, num2 = 8):
    return render_template('index.html', num1 = num1, num2 = num2)
@app.route('/<int:num1>/<int:num2>')
def num1_by_num2(num1, num2):
    return render_template('index.html', num1 = num1, num2 = num2)


if __name__=="__main__":
    app.run(debug=True)
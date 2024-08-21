from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            # The functions that allow the user to input and pin the values to the designated 'nr1 or nr2'
            nr1 = float(request.form['nr1'])
            nr2 = float(request.form['nr2'])
            choice = request.form['choice']

            # The functions that explain how to do the calculations
            if choice == '-':
                result = nr1 - nr2
            elif choice == '+':
                result = nr1 + nr2
            elif choice == '/':
                if nr2 != 0:
                    result = nr1 / nr2
                else:
                    result = 'Error: Division by zero'
            elif choice == '*':
                result = nr1 * nr2
            else:
                result = 'Invalid operation'
        except ValueError:
            result = 'Error: Invalid input'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
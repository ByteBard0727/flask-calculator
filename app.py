from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            # Retrieve input values from the form
            nr1 = float(request.form['nr1'])
            nr2 = float(request.form['nr2'])
            choice = request.form['choice']

            # Perform calculation based on user choice
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
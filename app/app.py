from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('details.html')

@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        projectpath = request.form.get('user_name')
        gender = request.form['gender']
        age = request.form.get('age')
        number = request.form.get('number')
        address = request.form.get('address')

        print(projectpath)
        print(gender)
        print(age)
        print(number)
        print(address)

        return render_template("result.html")
    else:
        return render_template('result.html')

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def homepage():
	return render_template('base.html', NAME='Koriel Lopez')

@app.route('/user/<name>')
def user(name):
	listOfNames = [name, "bozo", "zebra"]
	return render_template('name.html', 
						   NAME=name,
						   nameList=listOfNames)

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name=None):
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)


if __name__ == '__main__':
	app.run(debug=True)
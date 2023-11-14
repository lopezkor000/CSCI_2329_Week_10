from flask import Flask, render_template, request

app = Flask(__name__)


# --------------------DATABASE--------------------
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sampleDataBase.db'
db = SQLAlchemy(app)


class Visitor(db.Model):
	username = db.Column(db.String(100), primary_key=True)
	numVisits = db.Column(db.Integer, default=1)

	def __repr__(self):
		return f'{self.username} - {self.numVisits}'


with app.app_context():
	db.create_all()
# ------------------------------------------------


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
def formDemo():
	name = None
	if request.method == 'POST':
		if request.form['name']:
			name=request.form['name']

			visitor = Visitor.query.get(name)
			if visitor == None:
				visitor = Visitor(username=name)
				db.session.add(visitor)
			else:
				visitor.numVisits += 1

		db.session.commit()

	return render_template('form.html', name=name)

@app.route('/visitors')
def visitors():
	people = Visitor.query.all()
	return render_template('visitors.html', people=people)


if __name__ == '__main__':
	app.run(debug=True)
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	content =db.Column(db.String(200), nullable=False)
	price = db.Column(db.String(200), nullable=False)

def __repr__(self):
	return '<Tasl %r>' % self.id
	


@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/inseart_page.html')
def inseart_page():
	return render_template('inseart_page.html')

@app.route('/product_sheet.html')
def product_sheet():
	return render_template('product_sheet.html')


if __name__ == "__main__":
    app.run(debug=True)
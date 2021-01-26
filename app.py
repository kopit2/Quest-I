from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3_test
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hardware.db'
db = SQLAlchemy(app)


@app.route('/index.html', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		p_name = request.form["productname"]
		if p_name == '':
			p_name = 'dsfdsgsdhsdhsdgddscecewwfwerbbr'
		else:
			p_name = p_name
		try:
			conn = sqlite3.connect('hardware.db')
			c = conn.cursor()
			names = c.execute("SELECT rowid, * FROM products WHERE {} LIKE '%{}%'".format('name',p_name))
			conn.commit()
			return render_template('/index.html', names=names)
		except:
			return render_template('index.html',)
	else:
		return render_template('index.html',)
   


@app.route('/inseart_page.html', methods=['POST'])
def inseart_page():
	if request.method == 'POST':
		p_name = request.form["product_name"]
		p_price = request.form["product_price"]

		try:
			sqlite3_test.add_one(p_name,p_price)
			return redirect('/inseart_page.html')
		except:
			return 'there wan an issue adding your product'
	else:
		return render_template('inseart_page.html')


@app.route('/product_sheet.html')
def product_sheet():
	conn = sqlite3.connect('hardware.db')
	c = conn.cursor()
	items = c.execute("SELECT rowid, * FROM products ORDER BY rowid")
	conn.commit()
	return render_template('product_sheet.html', items=items)


if __name__ == "__main__":
    app.run(debug=True)
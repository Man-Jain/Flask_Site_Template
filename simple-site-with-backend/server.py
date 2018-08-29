from flask import Flask, render_template,request
import back

app=Flask(__name__)

@app.route('/')
def index_fun():
	return render_template('index.html')

@app.route('/forms.html')
def sign_in():
	return render_template('forms.html')

@app.route('/save',methods=['POST'])
def get_data():
	name=request.form['name']
	price=request.form['price']
	back.write_data(name,price)
	return 'OK'

@app.route('/api',methods=['GET'])
def api():
	name=str(request.args.get('name'))
	price=str(request.args.get('price'))
	back.write_data(name,price)
	return 'OK'

if __name__=="__main__":
	app.run(debug=True)
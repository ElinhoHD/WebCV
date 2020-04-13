from flask import Flask,send_file,redirect,render_template

app = Flask(__name__)



@app.route('/cv')
def index():
	with  open("index.html") as f:
		data = f.read()
	return data
@app.route('/cv/index.html')
def  redirindex():
	return redirect("http://93.12.72.173/cv",code=302)
@app.route('/cv/assets/img/elie_ntumba.jpg')
def elie_ntumba_jpg():
	return send_file("assets/img/elie_ntumba.jpg", mimetype="image/jpg")

@app.route('/cv/Facebook.png')
def fb_png():
	return send_file("assets/img/Facebook.png", mimetype='image/png')
@app.route('/cv/assets/css/animated.min.css')
def animated_css():
	return send_file("assets/css/animated.min.css", mimetype='text/css')
@app.route('/cv/assets/css/materialize.min.css')
def materialize_css():
	return send_file("assets/css/materialize.min.css", mimetype='text/css')


@app.route('/background1.jpg')
def back1_jpg():
	return send_file("assets/img/background1.jpg", mimetype='text/jpg')

@app.route('/background2.jpg')
def back2_jpg():
	return send_file("assets/img/background2.jpg", mimetype='text/jpg')

@app.route('/background3.jpg')
def back3_jpg():
	return send_file("assets/img/background3.jpg", mimetype='text/jpg')

@app.route('/js/materialize.js')
def materialize_js():
	return send_file("assets/js/materialize.min.js", mimetype='text/js')
@app.route('/js/init.js')
def materialize_init():
	return send_file("assets/js/init.js", mimetype='text/js')

@app.route('/cv/logo_PC.png')
def logo_png():
	return send_file("logo_PC.png", mimetype='image/png')
@app.route('/cv/assets/css/style.css')
def style_css():
	return send_file("assets/css/style.css", mimetype='text/css')
@app.route('/cv/assets/img/instagram.png')
def instagram_png():
	return send_file("assets/img/instagram.png", mimetype='image/png')
@app.route('/cv/assets/img/Elie_Intro1.jpg')
def elie_png():
	return send_file("assets/img/Elie_Intro1.jpg", mimetype='image/jpg')
@app.route('/cv/assets/img/linkedin.png')
def linkedin_png():
	return send_file("assets/img/linkedin.png", mimetype='image/png')
@app.route('/cv/logo_PC.ico')
def logo_pc_ico():
	return send_file("logo_PC.ico", mimetype='image/x-icon')

if __name__ == '__main__' :
	app.run(debug=True,host='0.0.0.0')


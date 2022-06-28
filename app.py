from markupsafe import escape
from flask import Flask, render_template
# from flask_mail import Message
# from flaskbb.extensions import mail, celery

app = Flask(__name__)

@app.route('/')
def map_func():
	return render_template("map.html")

@app.route('/#close/reports/')
@app.route('/reports/')
def reports_func():
	return render_template("reports.html")

@app.route('/#close/explore')
@app.route('/explore')
def explore_func():
	return render_template("explore.html")

@app.route('/#close/forum')
@app.route('/forum')
def forum_func():
    return render_template("forum.html")



@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

if __name__ == "__main__":
    
	app.run(debug = True)



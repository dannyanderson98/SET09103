from flask import Flask, render_template

app = Flask(__name__)Flask

@app.route('/string:page_name>/')
def render_static(page_name):
	returm render_template('Brain_Stormer.html' % Home)

if __name__ == '__Home__':
	app.run()








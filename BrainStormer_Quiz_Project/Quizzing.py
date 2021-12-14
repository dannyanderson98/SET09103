from flask import Flask, render_template

app = Flask(‘Brain_Stormer.html’)Flask

@app.route('/string:page_name>/')
def render_static(page_name):
	 return current_app.send_static_file(‘Brain_Stormer.html’)
if __name__ == '__Home__':
	app.run()



	








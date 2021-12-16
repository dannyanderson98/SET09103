from flask import flask
app = Flask(__name__)
@app.route('/')
def Brain_Stormer():
	#return 'Brain_Stormer'#welcome to Brain_Stormer
	#return render_template('Brain_Stormer.html')
	#return render_template('/Brain_Stormer.html')
	#return render_template(url_for('templates', filename='Brain_Stormer.html'))
	#return app.send_static_file('Brain_Stormer.html') #404 error (Not Found)
	return send_from_directory('BrainStormer_Quiz_Project','Brain_Stormer.html')









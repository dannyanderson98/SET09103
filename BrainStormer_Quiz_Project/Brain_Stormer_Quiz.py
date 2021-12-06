from flask import Flask, render_template

app = Flask(__name__)Flask

@app.route('/string:page_name>/')
def render_static(page_name):
	return render_template('Brain_Stormer.html' % Home)
    return render_template('HowToPlay.html' % How To Play)
    return render_template('Rules.html' % Rules)
    return render_template('LetsPlay.html' % Lets Play)
    return render_template('music.html' % Music) 
    return render_template('generalknowledge.html' % General Knowledge)
    return render_template('filmNtv.html' % Film N TV)
    return render_template('worldcultures.html' % World Cultures)
if __name__ == '__Home__':
	app.run()








from flask import Flask, current_app
app = Flask(__name__)

@app.route('/')
def SET09103_Quiz_Project():
    return current_app.send_static_file('Brain_Stormer.html')









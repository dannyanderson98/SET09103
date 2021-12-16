from flask import Flask, current_app
app = Flask(__name__)

@app.route('/')
def brain_stormer():
    return current_app.send_static_file('Brain_Stormer.html')









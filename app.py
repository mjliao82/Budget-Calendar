from flask import Flask, render_templates

#this is the backend framework. I (Mike) will work on this
#purpose of the file is to connect processed data with frontend

app = Flask(__name__)

if __name__=="__main__":
    app.run(debug=True)
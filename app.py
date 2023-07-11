from flask import Flask, render_template, request, jsonify
import csv
import os
from datetime import datetime


#this is the backend framework. I (Mike) will work on this
#purpose of the file is to connect processed data with frontend

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/events', methods=['GET', 'POST'])
def handle_events():
    if request.method == 'POST':
        # Add a new event
        new_event = request.get_json()
        with open('events.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'start'])
            writer.writerow(new_event)
        return jsonify(new_event)

    elif request.method == 'GET':
        # Return all events
        if os.path.exists('events.csv'):
            with open('events.csv', 'r') as f:
                reader = csv.DictReader(f)
                events = [ {'title': row['title'], 'start': datetime.fromisoformat(row['start']).isoformat()} for row in reader]
        else:
            events = []
        return jsonify(events)

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import csv
import os
from datetime import datetime
import processor

#this is the backend framework. I (Mike) will work on this
#purpose of the file is to connect processed data with frontend

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/first")
def first():
    return render_template("months.html")

@app.route('/accumulate', methods=['GET'])
def acc():
    processor.cumalative()
    with open('data.csv', 'r') as f:
        reader = csv.DictReader(f)
        events = [ {'title': row['title'], 'start': datetime.fromisoformat(row['start']).isoformat()} for row in reader]
    return jsonify(events)



@app.route('/change_file', methods=['GET', 'POST'])
def change_file():
    if request.method=='POST':
        new_filename = request.get_json().get('filename')
        with open('current_file.txt', 'w') as f:
            f.write(new_filename)
        return jsonify({'message': 'File changed successfully'}), 200
    elif request.method=='GET':
        filename = processor.get_current_filename()
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                events = [ {'title': row['title'], 'start': datetime.fromisoformat(row['start']).isoformat()} for row in reader]
        else:
            events = []
        return jsonify(events)
    #POST THIS SHIT RIGHT HERE



@app.route('/events', methods=['GET', 'POST'])
def handle_events():
    filename = processor.get_current_filename()
    if request.method == 'POST':
        new_event = request.get_json()
        processor.IDs(new_event)
        # Add a new event
        with open(filename, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'start'])
            writer.writerow(new_event)
        return jsonify(new_event)

    elif request.method == 'GET':
        # Return all events
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                events = [ {'title': row['title'], 'start': datetime.fromisoformat(row['start']).isoformat()} for row in reader]
        else:
            events = []
        return jsonify(events)

@app.route('/submit', methods=['POST']) #on submitting year and month on /first
def submit():
    data = request.get_json()
    year = data.get('year')
    month = data.get('month')
    pull = [year, month]

    '''#proves that it works
    with open('data.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([year, month])
    '''
    return jsonify({"message": "Data saved successfully"}), 200


@app.route('/events/<int:event_id>', methods=['GET', 'POST', 'DELETE'])
def handle_event(event_id):
    #BUGGGGGGGGGGGGGGGGGGGGGGG
    filename = processor.get_current_filename()
    try:
        processor.row_delete(filename, event_id)  # Assuming event_id is equal to the row number
        return jsonify({'message': 'Event deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/months')
def month_analytics():
    return render_template("monthEmbed.html")

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():

     # Design and Develop the Code
    data = request.get_json()

    # Validate that a title was provided
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # Implement the Loop and Process Each Element
    # Determine the next ID based on the existing events
    new_id = len(events) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    # Return and Handle Results
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):

     # Design and Develop the Code
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # Implement the Loop and Process Each Element
    for event in events:
        if event.id == event_id:
            event.title = data["title"]
            # Return and Handle Results
            return jsonify(event.to_dict()), 200

    # If no event was found
    return jsonify({"error": "Event not found"}), 404

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):

    # Design and Develop the Code
    # Implement the Loop and Process Each Element
    for event in events:
        if event.id == event_id:
            events.remove(event)
            # Return and Handle Results
            return "", 204

    # If no event was found
    return jsonify({"error": "Event not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

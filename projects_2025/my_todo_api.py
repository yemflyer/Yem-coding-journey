from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to store tasks

tasks= []
task_id_counter = 1 # To keep track of task ids

@app.route('/') # Create a simple home route to check if the API is running
def home():
    """
    A simple home route to check if the API is running.
    """
    return "Welcome to the My Todo List  API!"

# Post : Add a new task
@app.route('/tasks', methods = ['POST'])
def add_task():
    global task_id_counter # Access the global variable to increment task ids
    data = request.json # Get the JSON data from the request body
    
    if 'title' not in data :# Check if the title is provided in the request data
        # If title is missing, return an error response
        return jsonify({"error": "Provide a title for the task"}), 400 # Bad request if title is missing 
    
    task = {
        'id': task_id_counter, # Assign the current task id
        'title': data['title'], # Get the title from the request data
        'completed': False # Default to not completed when created
    }
    
    tasks.append(task) # Add the task to the list of tasks
    task_id_counter += 1 # Increment the task id counter for the next task
    return jsonify(task), 201 # Return the created task with a 201 status code (Created)


# Get : Retrieve all tasks
@app.route('/tasks', methods = ['GET'])
def get_tasks():
    """
    Retrieve all tasks.
    """
    return jsonify(tasks), 200

# Delete : Delete a task by id
@app.route('/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task ["id"] != task_id] # Filter out the task with the given id from the list of tasks
    return jsonify ({"message": " Task deleted succesfully"}), 200 # Return a success message with a 200 status code

'''Example of JSON data for tasks:
# Sample JSON data for tasks
[
  {"id": 1, "title": "Buy milk"},
  {"id": 2, "title": "Do homework"}
]

To delete the homework task, send a DELETE request to /tasks/2.
# Sample DELETE request to delete a task    
DELETE /tasks/2
# Sample response for successful deletion
{
  "message": "Task deleted successfully"
}
'''

if __name__ == '__main__':
    app.run(debug=True) # Run the Flask app with debug mode enabled for development purposes

    """
  NEXT TO DO : 
  + work on the html part of the API to create a simple front end for the API using HTML and JavaScript.
  This will allow us to interact with the API using a web interface.
  + Add more features to the API such as user authentication, task categories, and due dates.
  + Explore using a database to store tasks instead of in-memory storage.
    This will allow us to persist data even when the server restarts.
  + Add error handling and validation to ensure the API is robust and handles edge cases gracefully.
  
    """
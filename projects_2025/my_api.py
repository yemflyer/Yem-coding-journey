#Create a Python Api using Flask framework
"""
This is a simple API using Flask framework in Python.
https://youtu.be/zsYIw6RXjfM (last time skip : 8:42) for a quick video on how to create a simple API with Flask.
"""
from flask import Flask, request, jsonify

#Create our flask app
app = Flask(__name__)


#Create a route : 
#Route = end point of our Api that we can  go to , to get some type of data 
"""
@app.route('/') #add a decorators @ .route('/') to specify the end point of our API

def home(): #dEFINE Data i want user to have access to when they go to the end point
    return  "home"

When runnning an api we use http methods to interact with the API
GET : To retrieve data
POST: To create new data        
PUT : To update existing data
DELETE: To delete existing data

my get request url : http://127.0.0.1:5000/get-user/123?extra=%22hello%22
get-user/123 is the dynamic part of the route where 123 is passed in as a user_id.
get-user/123?extra="hello world" is an example of a request to the API where we can also pass in an extra query parameter.
"""
#Create a simple route to test our API
@app.route("/get-user/<user_id>") #This is an example of a dynamic route where we can pass in a user_id
#This route will accept a GET request and return user data based on the user_id passed in the URL

#Define the function to handle the request for this route
def get_user(user_id):
    user_data = {
        "useer_id": user_id, #This is the dynamic part of the route
        "name": "John Doe", #Static data for example purposes 
        "email": "john.doe@example.com"
        }
    extra = request.args.get('extra') #This allows us to get additional query parameters from the URL
    if extra:#Check if extra is provided in the request
        #If extra is provided, add it to the user_data dictionary
        user_data['extra'] = extra #Add the extra data to the response if provided
    
    return jsonify(user_data), 200 #Return the user data using JSON with a 200 status code


#Create a Post route : can accept a post request , if i wanted get would have to be added
@app.route("/create-user", methods = ['Post']) #This route will accept POST  request
def create_user():
    data = request.get_json() #return all the json data past in the body of the request 

    return jsonify(data), 201
#Return the data back to the user with a 201 status code which to indicate it was created successfully


#RUN OUR FLASK APP
if __name__ == '__main__': #This allows us to run the app directly from this file
    app.run(debug=True) #debug=True will allow us to see errors in the browser and auto-reload the server on code changes

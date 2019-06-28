from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
  
class Employees(Resource):
    def get(self):

        return {1,1,1,2,3,3,4,3} # Fetches first column that is Employee ID
      
api.add_resource(Employees, '/employees') # Route_1

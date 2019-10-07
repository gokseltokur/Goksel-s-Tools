from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# API works with resources
# Every resource has to be class
# student inherits resource **
class Student(Resource):
    def get(self, name):
        return {'student': name}
    # you can define also post, delete etc. ...

# instead of @app.route('/student') we should define like this.
api.add_resource(Student, '/student/<string:name>') # http://127.0.0.1:5000/student/Rolf

app.run(port=5000)

    


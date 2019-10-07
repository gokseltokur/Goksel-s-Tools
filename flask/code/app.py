from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

# API works with resources
# Every resource has to be class
# student inherits resource **
class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) # loopla aramaktan tek satira dusuruyor next ve filter
        return {'item': item}, 200 if item else 404 # 404 not found STATUS CODE are important for mobile apps to checks

    # you can define also post, delete etc. ...
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400 # 400 bad request
        

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # 201 is for created STATUS CODE

class ItemList(Resource):
    def get(self):
        return {'items': items}



# instead of @app.route('/student') we should define like this.
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')

#debug=True shows html debug page 
app.run(port=5000, debug=True)


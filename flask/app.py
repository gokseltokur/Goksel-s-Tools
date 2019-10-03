from flask import Flask

app = Flask(__name__) # Object of flask

stores = [
    {
        'name': 'My Wonderful Store'
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]

    }
]


# POST - used to receive data
# GET - used to send data back only
# POST ve GET ne olduguna gore degisir biz burada serveriz

# POST /store data: {name:}   #Create a store with a name
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>    # Get a store for given name
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    pass

# GET /store                  # return a list of all the stores
@app.route('/store')
def get_stores(name):
    pass

# POST /store/<string:name>/item # create an item inside a specific store with a given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass

# GET /store/<string:name>/item # Get all the items in a specific store
@app.route('/store/<string:name>/item') 
def get_items_in_store(name):
    pass

app.run(port=5000)  # 127.0.0.1:5000




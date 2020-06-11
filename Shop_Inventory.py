import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

items = [
    {'id': '0',
     'name': 'Bubble gum',
     'price': '20$',
     'qty available': '60'},
    {'id': '1',
     'name': 'Ice cream',
     'price': '100$',
     'qty available': '20'},
    {'id': '2',
     'name': 'Yoghurt',
     'price': '50$',
     'qty available': '30'},
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Shop Inventory</h1>
<p>A prototype API for shop inventory.</p>'''
# to get all
@app.route('/api/v1/inventorys/all', methods=['GET'])
def getALlInventorys():
    return jsonify(items)
#to get a specific item
@app.route('/api/v1/inventorys/<inventory_id>', methods =['GET'])
def getInventory(inventory_id):
    urs = [inventory for inventory in items if(inventory['id'] == inventory_id)]
    return jsonify(urs)
# post which is used to update existing DB
@app.route('/api/v1/inventorys/<inventory_id>', methods=['PUT'])
def updateInventory(inventory_id):
    urs = [inventory for inventory in items if (inventory['id'] == inventory_id)]
    if 'name' in request.json:
        urs[0]['name'] = request.json['name']
    if 'price' in request.json:
        urs[0]['price'] = request.json['price']
    if 'qty available' in request.json:
        urs[0]['qty available'] = request.json['qty available']
    return jsonify(urs[0])
#POST is used to create new item in the DB
@app.route('/api/v1/inventorys/all', methods=['POST'])
def createInventory():
    dat = {
    'id': request.json['id'],
    'name': request.json['name'],
    'price': request.json['price'],
    'qty available': request.json['qty available']
    }
    items.append(dat)
    return jsonify(dat)
# used to delete an item
@app.route('/api/v1/inventorys/<inventory_id>',methods=['DELETE'])
def deleteInventory(inventory_id):
    urs = [inventory for inventory in items if(inventory['id'] == inventory_id)]
    if len(urs) == 0:
        abort(404)
    items.remove(urs[0])
    return jsonify({'response':'Success'})
if __name__ == '__main__':
    app.run()

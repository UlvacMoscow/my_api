from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
app.secret_key = "senbka"
api = Api(app)

items = []

class Item(Resource):
	def get(self, name):
		for item in items:
			if item["name"] == name:
				return item, 200
		return {"item" : None}, 404

	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None):
			return {"message": "An item with name '{}' already exists.".format(name)}, 400 

		data = request.get_json()
		item = {"name": name, "price": data['price']}
		items.append(item)
		return item, 201


class ItemsList(Resource):
	def get(self):
		return {'items': items}

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemsList, "/items")

if __name__ == "__main__":
	app.run(port=5000, debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from gestion_bdd import*

app = Flask(__name__)
CORS(app)
bdd_json = 'back/bdd.json'

action_bdd = gestion_bdd(bdd_json)


@app.route('/product', methods=['POST'])
def create_new_product():
    #Récupération des données entrées par l'admin
    new_product = request.json
    #On définit les différents champs
    new_product_fields = ['code','name','description','image','price','category','quantity','inventoryStatus','rating']
    #On vérifie si tout les champs sont bon
    if not all(field in new_product for field in new_product_fields):
        return jsonify({'message':'Error fields'}), 400
    
    action_bdd.read_json()
    action_bdd.add_data(new_product)
    action_bdd.save_bdd()
    #On retourne les informations mise a jour pour la partie front et on confirme que le POST à bien était éffectué
    return jsonify(action_bdd.contenu_json), 201


@app.route('/products', methods=['GET'])
def get_all_product():
    action_bdd.read_json()
    return jsonify(action_bdd.contenu_json)
    
@app.route('/product', methods=['GET'])
def get_first_product():
    action_bdd.read_json()
    #On vérifie que la base de données n'est pas vide
    if action_bdd.contenu_json:
        return jsonify(action_bdd.contenu_json[0])
    return jsonify({'message': 'Pas de produit dans la base'}), 404

@app.route('/product', methods=['PATCH'])
def update_first_product():
    #Récupération des données entrées par l'admin
    update_product = request.json
    action_bdd.read_json()
    #On vérifie que la base de données n'est pas vide
    if action_bdd.contenu_json:
        action_bdd.update_first_product(update_product)
        action_bdd.save_bdd()
        return jsonify(action_bdd.contenu_json)
    return jsonify({'message': 'Product not found'}), 404

@app.route('/product', methods=['DELETE'])
def delete_product():
    action_bdd.read_json()
    #On vérifie que la base de données n'est pas vide
    if action_bdd.contenu_json:
        action_bdd.delete_product()
        action_bdd.save_bdd()
        return jsonify(action_bdd.contenu_json),200
    return jsonify({'message' : 'error'}),404


if __name__ == '__main__':
    app.run(debug=False)

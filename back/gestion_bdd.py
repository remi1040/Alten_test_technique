import json

class gestion_bdd:
    def __init__(self,bdd_path):
        #chemin de la base de données
        self.bdd_path = bdd_path
        #Contenu de la base de données
        self.contenu_json = None

    def add_data(self,new_product):
        """Ajoute des données a la base de données"""
        if self.contenu_json:
            new_product['id'] = self.contenu_json[-1]['id'] + 1
            self.contenu_json.append(new_product)
        else:
            new_product['id'] = 1
            self.contenu_json = [new_product]

    def save_bdd(self):
        """Sauvegarde du nouveau fichier json"""
        with open(self.bdd_path, 'w') as file:
            json.dump(self.contenu_json, file, indent=4)
    
    def read_json(self):
        """Lecture de la base de données json"""
        with open (self.bdd_path,'r') as file:
            self.contenu_json = json.load(file)

    def update_first_product(self,update_product):
        print(update_product)
        print(self.contenu_json)
        """Mise à jour du premier élement de la base de données"""
        for key, value in update_product.items():
                self.contenu_json[0][key] = value

    def delete_product(self):
        """Supprime le premier élement de la base de données"""
        self.contenu_json = self.contenu_json[1:]
       
if __name__  ==  "__main__":
   pass
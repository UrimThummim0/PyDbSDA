from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#from pymongo import MongoClient
import pandas as pd
import os
"""
# MongoDB connection
client = MongoClient('mongodb+srv://rasolofondraiben02:ZkHVj4dyOiubOame@cluster0.ciazj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['mydb']
collection = db['users']
"""

class MongoDBApp(App):
    def build(self):
        return MainLayout()

class MainLayout(BoxLayout):
    def insert_user(self):
        # Get data from input fields
        kilasy = self.ids.kilasy_input.text
        sabata = self.ids.sabata_input.text
        mambra_tonga = self.ids.mambra_tonga_input.text
        nianatra_impito = self.ids.nianatra_impito_input.text

        # Validate inputs
        if kilasy and sabata and mambra_tonga and nianatra_impito:
            try:
                kilasy = str(kilasy)
                kilasy = kilasy.replace(" ", "_")
                sabata = int(sabata)
                mambra_tonga = int(mambra_tonga)
                nianatra_impito = int(nianatra_impito)

                """
                # Insert data into MongoDB
                collection.insert_one({
                    "sabata": sabata,
                    "mambra_tonga": mambra_tonga,
                    "nianatra_im-pito": nianatra_impito
                })
            
                """
                # Show success message
                self.ids.message_label.text = "User added successfully!"

                #Local DATABASE
                database = [{
                    "sabata":sabata,
                    "mambra_tonga":mambra_tonga,
                    "nianatra_impito":nianatra_impito
                    }]

                file_path = f"database/ivandry_ss_db_{kilasy}.csv"
                folder_path = "database"
                
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                if os.path.exists(file_path):
                    # Append to the CSV
                    df = pd.DataFrame(database)
                    df.to_csv(file_path, mode='a', header=False, index=False)
                else:
                    # Create a new CSV with header
                    df = pd.DataFrame(database)
                    df.to_csv(file_path, mode='w', header=True, index=False)

            except ValueError:
                # Handle non-integer input
                self.ids.message_label.text = "Isan'ny mambra tonga sy nianatra im-pito dia tokony ho isa!"
            except Exception as e:
                # Handle other errors
                self.ids.message_label.text = f"Error: {str(e)}"
        else:
            self.ids.message_label.text = "All fields are required!"

        print(database, file_path)

if __name__ == '__main__':
    MongoDBApp().run()

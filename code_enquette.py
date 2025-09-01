from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

uri = "mongodb+srv://2741450:fpcVm5SZwWGIWDgL@cluster0.sysk4be.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Connection failed:", e)
df = pd.read_excel("C://Users//User//OneDrive - Collège la Cité//Bureau//Enquette_sociaux_economique.xlsx")    
df.head()
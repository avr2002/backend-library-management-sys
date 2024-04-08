from pymongo import MongoClient

client = MongoClient("mongodb+srv://avr27:1KkMYKb2lQAEVRfx@libdb.dt7x8w3.mongodb.net/?retryWrites=true&w=majority&appName=LibDB")

db = client.lib_db

collection_name = db["student_collection"]

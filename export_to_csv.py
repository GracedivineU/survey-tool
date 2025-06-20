from pymongo import MongoClient
import csv

client = MongoClient("mongodb://localhost:27017/")
db = client["survey_db"]
collection = db["participants"]

class User:
    def __init__(self, db_collection):
        self.collection = db_collection

    def export_to_csv(self, filename="user_data.csv"):
        data = list(self.collection.find())
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Age', 'Gender', 'Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare'])
            for user in data:
                expenses = user['expenses']
                writer.writerow([
                    user['age'],
                    user['gender'],
                    user['income'],
                    expenses['utilities'],
                    expenses['entertainment'],
                    expenses['school_fees'],
                    expenses['shopping'],
                    expenses['healthcare']
                ])

if __name__ == '__main__':
    u = User(collection)
    u.export_to_csv()
    print("Data exported to user_data.csv!")

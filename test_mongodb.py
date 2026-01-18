
from pymongo import MongoClient

uri = "mongodb+srv://username_db_user:<password@cluster0.nkdbjb5.mongodb.net/?appName=Cluster0"

def run():
    try:
        # Create MongoDB client
        client = MongoClient(uri)

        # Ping the server
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

    except Exception as e:
        print("Error:", e)

    finally:
        client.close()

if __name__ == "__main__":
    run()

# conda activate networksecurity

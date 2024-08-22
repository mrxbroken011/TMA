import threading
from mongoengine import *

# Connect to MongoDB
connect(db='', host='')

# Define the Document structure using MongoEngine
class Broadcast(Document):
    id = IntField(primary_key=True)
    user_name = StringField()

    meta = {'collection': 'broadcast'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Function to add a user to the collection
def add_user(id, user_name):
    try:
        if not Broadcast.objects(id=id):
            Broadcast(id=id, user_name=user_name).save()
    except ValidationError as e:
        print(f"Error saving user: {e}")

# Function to query all user IDs
def query_msg():
    return list(Broadcast.objects.only('id').order_by('id'))

# Example usage
if __name__ == "__main__":
    # Add a user
    add_user(1, "Alice")
    
    # Query messages
    messages = query_msg()
    for msg in messages:
        print(msg)

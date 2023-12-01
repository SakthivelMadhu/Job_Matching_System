from flask import Flask
from mongoengine import connect  # Change this line

app = Flask(__name__)
app.config.from_object('config.Config')

connect(
    db='job_matching_system_db',
    host='localhost',
    port=27017,
)

# Use the MongoEngine JSON encoder
# app.json_encoder = db.DocumentJSONEncoder

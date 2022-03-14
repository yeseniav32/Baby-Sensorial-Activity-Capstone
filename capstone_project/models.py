# Standard Imports
import uuid
from datetime import datetime

# 3rd Part imports aka imports that had to be downloaded
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# Activity Model Creation
class Activity(db.Model):
    id = db.Column(db.String, primary_key = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    activity_name = db.Column(db.String(150), nullable = False)
    sense = db.Column(db.String(50), nullable = False)
    age_range = db.Column(db.String(50), nullable = False)
    supplies = db.Column(db.String(300), nullable = False)
    instructions = db.Column(db.String(1000), nullable = False)
    description = db.Column(db.String(1000))

    def __init__(self, date_created, activity_name, sense, age_range, supplies, instructions, description):
        self.id = self.set_id()
        self.date_created = date_created
        self.activity_name = activity_name
        self.sense = sense
        self.age_range = age_range
        self.supplies = supplies
        self.instructions = instructions
        self.description = description

    def set_id(self):
            return str(uuid.uuid4())

    def __repr__(self):
        return f"The following Activity has been created: {self.activity_name}"

# Creation of API Schema via the Marshmallow Object
class ActivitySchema(ma.Schema):
    class Meta:
        fields = ['id', 'date_created', 'activity_name', 'sense', 'age_range', 'supplies', 'instructions', 'description']

activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)
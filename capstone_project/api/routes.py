from flask import Blueprint, jsonify, request;
from capstone_project.models import db,Activity,activity_schema,activities_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('getdata')
def getdata():
    return{'some': 'value',
            'Other':44.3}

@api.route('/activities', methods=['POST'])
def create_activity():
    activity_name = request.json['activity_name']
    sense = request.json['sense']
    age_range = request.json['age_range']
    supplies = request.json['supplies']
    instructions = request.json['instructions']
    description = request.json['description']

    activity = Activity(activity_name, sense, age_range, supplies, instructions, description)

    db.session.add(activity)
    db.session.commit()

    response = activity_schema.dump(activity)
    return jsonify(response)

# Retrieve all Activities
@api.route('/activities', methods=['GET'])
def get_activities():
    activities = Activity
    response = activities_schema.dump(activities)
    return jsonify(response)

# Retrieve an activity
@api.route('/activities/<id>', methods=['GET'])
def get_activity():
    activity = Activity.query.get(id)
    response = activity_schema.dump(activity)
    return jsonify(response)

@api.route('/activities/<id>', methods=['POST','PUT'])
def update_activity():
    activity = Activity.query.get(id)

    activity.activity_name = request.json['activity_name']
    activity.sense = request.json['sense']
    activity.age_range = request.json['age_range']
    activity.supplies = request.json['supplies']
    activity.instructions = request.json['instructions']
    activity.description = request.json['description']

    db.session.commit()
    response = activity_schema.dump(activity)
    return jsonify(response)

@api.route('/activities/<id>', methods = ['DELETE'])
def delete_activity(id):
    activity = Activity.query.get(id)
    db.session.delete(activity)
    db.session.commit()

    response = activity_schema.dump(activity)
    return jsonify(response)
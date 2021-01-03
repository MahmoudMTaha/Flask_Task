import sqlite3
from datetime import datetime
from flask_restful import Resource, Api, reqparse
import json

#This Resource receive POST req to create new user in users table
class Create_account(Resource):
    def post(self):
        db = sqlite3.Connection('data.db')
        cursor = db.cursor()
        date = datetime.now().date() #get the date when created this entity
        query = 'INSERT INTO users VALUES (NULL, ?)'
        try:
            cursor.execute(query, (date,))
            db.commit()
            db.close()
            return {"user_id": cursor.lastrowid}, 201 #returning the unique id for the new user 
        except:
            db.close()
            return {"message":"cannt Create User"}


#This Resource receive POST req with  user_id and event data and add them into events table
class add_event(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('event', type=str, required=True)
        data = parser.parse_args()
        date = datetime.now().date()
        db = sqlite3.Connection('data.db')
        cursor = db.cursor()
        query = 'INSERT INTO events VALUES (NULL, ?, ?, ?)'
        cursor.execute(query, (data['user_id'], data['event'], date))
        db.commit()
        db.close()
        return 200


#This Resource receive POST req with  user_id and file data and add them into apllications table
class create_application(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('file', type=str, required=True)
        data = parser.parse_args()
        date = datetime.now().date() 
        db = sqlite3.Connection('data.db')
        cursor = db.cursor()
        query = 'INSERT INTO apllications VALUES (NULL, ?, ?, ?)'
        cursor.execute(query, (data['user_id'], data['file'], date))
        db.commit()
        db.close()
        return 200

#This Resource receive GET to fetch all events associated  with user_id and start date in events table 
class Get_all_events(Resource):
    def get(self, user_id, start_date):
        db = sqlite3.Connection('data.db')
        cursor = db.cursor()
        query = 'SELECT  event FROM events WHERE user_id = ? and date = ?'
        cursor.execute(query, (user_id, start_date))
        events = cursor.fetchall()
        db.commit()
        db.close()
        if not events: #if the db return empty object
            return {"message":"no records with that info"}, 400 
        events_list = [] 
        for row in events:
            events_list.append(json.loads(row[0].replace("'", '"')))
        return events_list, 200  #returning list of json events data

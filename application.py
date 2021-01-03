import sqlite3
import create_tables
from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime
import resources

app = Flask(__name__)

api = Api(app)

api.add_resource(resources.Create_account, '/account/create')
api.add_resource(resources.Get_all_events, '/event/search/<string:user_id>/<string:start_date>') #localhost:5000/event/search/1/2021-01-03
api.add_resource(resources.create_application, '/apply')
api.add_resource(resources.add_event, '/event/add')

if __name__ == "__main__":
    if not create_tables.create_database_tables():  #create tables of db if not exists 
        print("cannot create databases")
        exit(1)
    app.run(debug=True)


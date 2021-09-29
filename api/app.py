from flask import Flask
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
import requests
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv("DATABASE_URL"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Person(db.Model): 
   id = db.Column(db.Integer, primary_key=True)
   first_name = db.Column(db.String(100))
   last_name = db.Column(db.String(100))
   job = db.Column(db.String(100))
   address = db.Column(db.String(100))
   city = db.Column(db.String(100))
   country = db.Column(db.String(100))

   def __init__(self,first_name,last_name,job,address,city,country):
      self.first_name = first_name
      self.last_name = last_name
      self.job = job
      self.address = address
      self.city = city
      self.country = country

db.create_all()

class PersonSchema(ma.Schema):
   class Meta:
      fields = ('id','first_name','last_name','job','address','city','country')

person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)

# agregar 13 registros con faker
@app.route('/add_person')
@cross_origin()
def add_person():
   url = 'http://faker-service/datos'
   response = requests.get(url)
   response_json = json.loads(response.text)
   for person in response_json["datos"]:
      data = Person(first_name=person["first_name"],last_name=person["last_name"],job=person["job"],address=person["address"],city=person["city"],country=person["country"])
      db.session.add(data)
   db.session.commit()
   return {'data':"Added Succesfully"}

# eliminar registro
@app.route('/delete_person/<id>', methods=['DELETE'])
def delete_person(id):
   person = Person.query.get(id)
   db.session.delete(person)
   db.session.commit()

   return {'data':"Deleted Succesfully"}

# mostrar registros
@app.route('/get_persons', methods=['GET'])
@cross_origin()
def get_persons():
   all_persons = Person.query.all()
   response = persons_schema.dump(all_persons)
   return jsonify({'data':response})

# eliminar registros
@app.route('/delete_persons', methods=['DELETE'])
@cross_origin(methods=['DELETE'])
def delete_persons():
   rows_deleted = db.session.query(Person).delete()
   db.session.commit()
   return jsonify({'data':rows_deleted})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)

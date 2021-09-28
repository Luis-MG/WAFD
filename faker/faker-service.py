from faker import Faker
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/datos',methods=['GET'])
def datos():
    fake = Faker()
    lista = list()
    for _ in range(13):
        data = dict()
        data["first_name"] = fake.first_name()
        data["last_name"] = fake.last_name()
        data["job"] = fake.job()
        data["address"] = fake.address()
        data["city"] = fake.city()
        data["country"] = fake.country()
        lista.append(data)
    return jsonify({"datos":lista})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug=True)
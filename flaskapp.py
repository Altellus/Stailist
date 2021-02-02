# import main Flask class and request object
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json

# create the Flask app
app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    bigFive = db.Column(db.Text, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    brands = db.Column(db.Text, nullable=False)
    interestsInFashion = db.Column(db.Integer, nullable=False)
    paysAttentionToApperance = db.Column(db.Integer, nullable=False)
    workRequiresFormal = db.Column(db.Boolean, nullable=False)
    howOftenBuysClothes = db.Column(db.String(50), nullable=False)
    likesShopping = db.Column(db.Integer, nullable=False)
    howMuchSpendsOnClothes = db.Column(db.String(20), nullable=False)
    hasALotOfClothes = db.Column(db.String(20), nullable=False)
    whyUsesStailist = db.Column(db.String(50), nullable=False)
    visitsSportStores = db.Column(db.Boolean, nullable=False)
    plan = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Result('{self.id}', '{self.age}', '{self.bigFive}', '{self.colors}')"


@app.route('/stailistResults', methods=['POST'])
def stailist_results():
    request_data = request.get_json()
    print(request_data)
    new_result = Result(
        age=request_data['age'],
        sex=request_data['sex'],
        bigFive=json.dumps(request_data['bigFive']),
        colors=str(request_data['colors']),
        brands=str(request_data['brands']),
        interestsInFashion=request_data['interestsInFashion'],
        paysAttentionToApperance=request_data['paysAttentionToApperance'],
        workRequiresFormal=request_data['workRequiresFormal'],
        howOftenBuysClothes=request_data['howOftenBuysClothes'],
        likesShopping=request_data['likesShopping'],
        howMuchSpendsOnClothes=request_data['howMuchSpendsOnClothes'],
        hasALotOfClothes=request_data['hasALotOfClothes'],
        whyUsesStailist=request_data['whyUsesStailist'],
        visitsSportStores=request_data['visitsSportStores'],
        plan=request_data['plan'],
        username=request_data['username'],
        password=request_data['password']
    )
    print(new_result)
    db.session.add(new_result)
    db.session.commit()
    print('New result added')
    return 'Result received'


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

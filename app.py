from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify
from flask import make_response
from flask import json
from bson import json_util
from random import randint
import pymongo


app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://ankitheroku:Ank1t$eth@ds259711.mlab.com:59711/heroku_bx2c0mfd"
# mongo = PyMongo(app)

DB_NAME = "heroku_bx2c0mfd"
DB_HOST = "ds259711.mlab.com"
DB_PORT = 59711
DB_USER = "ankitheroku" 
DB_PASS = "Ank1t$eth"

connection = pymongo.MongoClient(DB_HOST, DB_PORT)
db = connection[DB_NAME]
db.authenticate(DB_USER, DB_PASS)

#client = pymongo.MongoClient("mongodb://ankitheroku:Ank1t$eth@ds259711.mlab.com:59711/heroku_bx2c0mfd")

def jd(obj):
    return json.dumps(obj, default=json_util.default)

def response(data={}, code=200):
    resp = {
        "code" : code,
        "data" : data
    }
    response = make_response(jd(resp))
    response.headers['Status Code'] = resp['code']
    response.headers['Content-Type'] = "application/json"
    return response
@app.route('/')
def index():
	return "hello world"
@app.route('/AlotAnyNumberNumber/')
def AnyNumber():

	length=1
	finalnum=""
	while length==1:
                anynum=randint(1111111111,9999999999)
                num=db.Numbers.find({'Number':anynum}, {'Number':1,'_id':0})
                if len(list(num))==0:
                    db.Numbers.insert({'Number':anynum})
                    finalnum=anynum
                    length=0
	return jsonify({
	                'status':'New Number Alloted',
	                'NewNumber':finalnum,
	                })

@app.route('/AlotFancyNumberNumber/<int:number>')
def hello_world(number):
            if int(number)>=1111111111 and int(number)<=9999999999:
            	    user=db.Numbers.find({'Number':number}, {'Number':1,'_id':0})
            	    userlist=list(user)
                    length=len(userlist)
                    if length!=0:
                            numb=""
                            finalnum=""
                            l=0    

                            while l==0:
                                        anynum=randint(1111111111,9999999999)
                                        num=db.Numbers.find({'Number':anynum}, {'Number':1,'_id':0})
                                        if len(list(num))==0:
                                                db.Numbers.insert({'Number':anynum})
                                                finalnum=anynum
                                                return jsonify({
							                                'status':str(number)+' Number already Alloted',
							                                'NewNumber':finalnum
							                                })

                           
                    else:
                        db.Numbers.insert({'Number':number})
                        return jsonify({
                            'status':'New Number Alloted',
                            'NewNumber':number,
                            })
            else:
                return  jsonify({
                        'status':'number should be between 111-111-1111 and 999-999-9999',
                        'NewNumber':'No Number Alloted',
                        })

if __name__ == "__main__":
	app.run()                
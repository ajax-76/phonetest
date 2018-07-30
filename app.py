from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify
from flask import make_response
from flask import json
from bson import json_util
from random import randint

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/eve"
mongo = PyMongo(app)

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

@app.route('/AlotAnyNumberNumber/')
def AnyNumber():
	length=1
	finalnum=""
	while length==0:
                anynum=randint(1111111111,9999999999)
                num=mongo.db.Numbers.find({'Number':anynum}, {'Number':1,'_id':0})
                if num.count()==0:
                    mongo.db.Numbers.insert({'Number':anynum})
                    finalnum=anynum
                    length=0
	return jsonify({
	                'status':'New Number Alloted',
	                'NewNumber':finalnum,
	                })

@app.route('/AlotFancyNumberNumber/<int:number>')
def hello_world(number):
            if int(number)>=1111111111 and int(number)<=9999999999:
            	    user=mongo.db.Numbers.find({'Number':number}, {'Number':1,'_id':0})
                    length=user.count()
                    if length!=0:
                            numb=""
                            finalnum=""
                            for num in user:
                                numb=num
                            l=0    

                            while l==0:
                                        anynum=randint(1111111111,9999999999)
                                        num=mongo.db.Numbers.find({'Number':anynum}, {'Number':1,'_id':0})
                                        if num.count()==0:
                                                mongo.db.Numbers.insert({'Number':anynum})
                                                finalnum=anynum
                                                return jsonify({
							                                'status':str(numb["Number"])+' Number already Alloted',
							                                'NewNumber':finalnum
							                                })

                           
                    else:
                        mongo.db.Numbers.insert({'Number':number})
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
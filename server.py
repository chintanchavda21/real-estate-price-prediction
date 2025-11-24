
from flask import Flask,request,jsonify
import util
# from flask_cors import CORS


util.load_saved_artifacts()
app=Flask(__name__)

@app.route('/get_location_names',methods=['GET'])




def get_location_names():
   response = jsonify({
       'location':util.get_location_names()
   })
   response.headers.add('Access-Control-Allow-Origin', '*')
   return response

@app.route('/predict_home_price',methods=['GET','POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])


    response = jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
    return jsonify({"error":"invalid input data type. plese ensure sqft,bhk,and bath are numbers."}),400
    print(f"An unexpeced error occured: {e}")
    return jsonify({"An intenal server error occured"}),500


if __name__ == "__main__":
    print("starting python flask server for Home price prediction")
    util.load_saved_artifacts()


    app.run()


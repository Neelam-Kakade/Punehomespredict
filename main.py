
from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from models.utils import PuneHouse
import config

app = Flask(__name__) # instance

@app.route("/")   #"/" >> home page
def hello_flask():
    print("Pune House Prediction")
    return render_template("index.html")

@app.route("/Pune_House_Price_prediction", methods=["POST", "GET"])
def get_price():
    if request.method == "GET":

        print("We are using GET Method")    
        availability = request.args.get("availability")
        size = request.args.get("size")
        bath = int(request.args.get("bath"))
        balcony = request.args.get("balcony")
        site_location = request.args.get("site_location")
        area_type = request.args.get("area_type")
        new_total_sqft = float(request.args.get("new_total_sqft"))
        
        ins = PuneHouse(availability, size, bath, balcony, site_location, area_type,new_total_sqft)
        charges = ins.get_house_price()
        return render_template("index.html", prediction = charges)
        # return "Working"
          

    else:
        print("We are using POST Method")
        
        availability = request.form.get("availability")
        # print("availability >>>",availability)
        size = request.form.get("size")  
        bath = int(request.form.get("bath"))
        balcony = request.form.get("balcony")
        site_location = request.form.get("site_location")
        area_type = request.form.get("area_type")
        new_total_sqft = float(request.form.get("new_total_sqft"))

        ins = PuneHouse(availability ,size, bath, balcony, site_location, area_type, new_total_sqft)
        charges = ins.get_house_price()
        return render_template("index.html", prediction = charges)
        # return "Success"


if __name__ =="__main__":
    app.run(host = "0.0.0.0",port = config.PORT_NUMBER,debug=True)
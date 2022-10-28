
import numpy as np
import json
import pickle
import config

class PuneHouse():
    def __init__(self, availability ,size, bath, balcony, site_location, area_type, new_total_sqft):
        
        self.availability = availability
        self.size = size
        self.bath = bath
        self.balcony = balcony
        self.site_location = site_location
        self.area_type = "area_type_" + area_type
        self.new_total_sqft = new_total_sqft

    def load_model(self):

        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.project_data = pickle.load(f)

            

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)
            

    def get_house_price(self):
        
        self.load_model()
        array = np.zeros(len(self.json_data["column_dict"]))
        array[0] = self.json_data["availability_dict"][self.availability]
        array[1] = self.json_data["dict_size"][self.size]
        array[2] = self.bath
        array[3] = self.balcony
        array[4] = self.json_data["dict_site_location"][self.site_location]
        array[9] = self.new_total_sqft

        area_type_index = self.json_data["column_dict"].index(self.area_type)
        array[area_type_index]=1

        price = self.project_data.predict([array])[0]
        return round(price,2)

if __name__ == "__main__":

    availability  = "Immediate Possession"
    size = "3 BHK"
    bath = 4.0
    balcony = 3.0
    site_location = "Yerawada"
    area_type = "Super built-up  Area"
    new_total_sqft = 300.7
    

    Obj = PuneHouse(availability ,size, bath, balcony, site_location, area_type, new_total_sqft)
    price = Obj.get_house_price()
    print(f"Price predicted for house in Pune is {price} lakhs only")



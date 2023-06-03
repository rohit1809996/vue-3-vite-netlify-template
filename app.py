from flask import Flask   , jsonify, request
import pickle

from flask_cors import CORS, cross_origin

import numpy as np
# pip install -U flask-cors 
# # # initialize our Flask application
app = Flask(__name__)
app.config['ENV']="development"

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = pickle.load(open('car_dekho.pickle', 'rb'))


@app.route("/")
@cross_origin()
def helloWorld():
    return "Hello, -world!"



@app.route("/model", methods=["GET"])
def predwine():

    if request.method == 'GET':

        try:

            # a = float(request.args.get('alcohol'))
            car_name =          int(request.args.get('Car_Name'))
            model_name =        int(request.args.get('Car_Model'))
            Kms_Driven =        int(request.args.get('Kms_Driven'))
            Years_old =         int(request.args.get('No_of_Years'))
            Fuel_Type =         int(request.args.get('Fuel_Type'))
            Transmission =      int(request.args.get('Transmission'))
            Owner =             int(request.args.get('Owner'))
            #    try:
            Years_old_square =  int(Years_old)**2
            Kms_Driven_square = int(Kms_Driven)**2
    
            if Fuel_Type  == 0:
                Fuel_type_Petrol = 1
                Fuel_Type_Diesel = 0
            elif Fuel_Type  == 1:
                Fuel_type_Petrol = 0
                Fuel_Type_Diesel = 1
    
    
            if Transmission  == 0:
                Transmission_Manual = 1
                Transmission_Automatic = 0
            elif Transmission  == 1:
                Transmission_Manual = 0
                Transmission_Automatic = 1
    
    
            if Owner == 0:
                Owner_First = 1
                Owner_Second = 0
                Owner_Third_Owner = 0
                Owner_Second_Fourth_Above = 0
                Owner_Second_Test_Drive_Car = 0
    
    
            elif Owner == 1:
                Owner_First = 0
                Owner_Second = 1
                Owner_Third_Owner = 0
                Owner_Second_Fourth_Above = 0
                Owner_Second_Test_Drive_Car = 0
    
            elif Owner == 2:
                Owner_First = 0
                Owner_Second = 0
                Owner_Third_Owner = 1
                Owner_Second_Fourth_Above = 0
                Owner_Second_Test_Drive_Car = 0
    
            elif Owner == 3:
                Owner_First = 0
                Owner_Second = 0
                Owner_Third_Owner = 0
                Owner_Second_Fourth_Above = 3
                Owner_Second_Test_Drive_Car = 0
    
            elif Owner  == 4:
                Owner_First = 0
                Owner_Second = 0
                Owner_Third_Owner = 0
                Owner_Second_Fourth_Above = 0
                Owner_Second_Test_Drive_Car = 1


        

            
        except:

            #   Years_old_square= 0
            #   Kms_Driven_square=0
           
       
            #   car_name = 0
            #   model_name = 0
            #   Kms_Driven = 0
            #   Years_old = 0
            #   Fuel_Type = 0
            #   Fuel_type_Petrol = 0
            #   Fuel_Type_Diesel = 0
            #   Transmission  = 0
            #   Transmission_Manual = 0
            #   Transmission_Automatic = 0

            #   Owner =   0                  
  
            #   Owner_First = 0
            #   Owner_Second = 0
            #   Owner_Third_Owner = 0
            #   Owner_Second_Fourth_Above = 0
            #   Owner_Second_Test_Drive_Car = 0

              return jsonify(str("No Input  " ))

        




    final_features = ([[car_name, model_name, Kms_Driven, Years_old,Years_old_square, Kms_Driven_square ,Fuel_type_Petrol,Fuel_Type_Diesel, Transmission_Manual,Transmission_Automatic ,Owner_First,Owner_Second_Fourth_Above,Owner_Second,Owner_Second_Test_Drive_Car,Owner_Third_Owner]])
    # final_features = [[1,45,100.00,6,36,10000,1,0,0,1,1,0,0,0,0]]

    prediction = model.predict(final_features)
    x = prediction
    
    x= list(map(lambda x :str(x) + ' Lacs only',x.round(2)))
    # prediction =("{:.2f}".format(prediction))
    print(x)

    return jsonify(str("Price  " + str(x[0])))


#  main thread of execution to start the server
if __name__ == '__main__':
    app.run(debug=True)
  
import os
import io
import numpy as np
from flask import Flask,render_template,request
from keras.models import load_model
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

upload_folder = os.path.join("static")

app.config["UPLOAD_FOLDER"] = upload_folder

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods = ["post"])
def predict_driver():
    
    img = request.files["image"]  # Getting the image into python from HTML

    img_filename = secure_filename(img.filename)  # Getting the name of the image
    
    img.save(os.path.join(app.config["UPLOAD_FOLDER"],img_filename))  # Saving that image into static folder

    img_path = os.path.join(app.config["UPLOAD_FOLDER"],img_filename) # Getting the image path
    
    # print(img_path)

    model = load_model(r"C:\Users\Kartik\Desktop\Distracted_Driver_Detection\model.h5") # Loading the model

    img1 = Image.open(img_path)  # Opening the image again 
    
    img_object = img1.resize((128,128)) # Resizing the image for our model

    img_object = np.array(img_object)  # Converting the image into numpy array

    img_object = np.expand_dims(img_object,axis = 0) # Expanding  the dimension for our ml model

    pred = model.predict(img_object)  # Predicting the output of the image

    predictions = np.argmax(pred)   # Getting the maximum probabilty value index 

    categories = { 
                   0 : "Normal Driving by Driver",
                   1 : "Texting on mobile using Right Hand",
                   2 : "Talking on the phone using right hand",
                   3 : "Texting on mobile using Left Hand",
                   4 : "Talking on the phone using Left hand",
                   5 : "Operating on the radio",
                   6 : "Drinking",
                   7 : "Reaching behind",
                   8 : "Hair and Makeup",
                   9 : "Talking to Passenger"
                 }

    return render_template("index1.html",img = img_path,desc = categories[predictions]) # Returning the output


app.run()
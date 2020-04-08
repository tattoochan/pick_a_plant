from flask import Flask, render_template, request, redirect, url_for
import os, pymongo	
from bson.objectid import ObjectId

app = Flask(__name__)

# setting up the upload folder
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))+'/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Setting up the MONGODB DATABASES to be link up	
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'pick_a_plant'
COLLECTION_NAME = 'plants'

# set up the connection to MONGO_URI which we set up in bashrc
conn = pymongo.MongoClient(MONGO_URI)
# set 'data' to be the name to represent the database link
data = conn[DATABASE_NAME][COLLECTION_NAME]

""" LANDINGPAGE """
@app.route('/')
def index():
    result = data.find({})
    return render_template ("index.html" , data = result)

""" NEW PLANT ENTRY """
@app.route('/new_plant') 
def new_plant():
    return render_template ("new_plant.html", data={})
@app.route('/new_plant', methods=['POST'])
def save_plant ():
    # Plant name 
    plant_name = request.form.get('plant_name')
    # Plant info
    plant_info = request.form.get('plant_info')
    # Plant price
    plant_price = request.form.get('plant_price')
    # Plant_image
    plant_image = request.files['plant_image']
    if 'plant_image' not in request.files:
        plant_image.filename = "default_plant.png"
    else:
    # if user does not select file, browser also
    # submit a empty part without filename
        if plant_image.filename == '':
            plant_image.filename = "default_plant.png"
        else:
            # Upload image file to static folder
            plant_image.save(os.path.join(app.config['UPLOAD_FOLDER'], plant_image.filename ))

    data.insert({
        'plant_name' : plant_name,
        'plant_info' : plant_info,
        'plant_price' : plant_price,
        'plant_image' : plant_image.filename, 
    })
    return redirect(url_for('index'))
    
""" CHANGES ROUTE """
@app.route('/make_changes/<plant_id>/<image>')
def make_changes(plant_id,image):
    # Get the id of the plant being edited
    result = data.find_one({
        '_id':ObjectId(plant_id)
    })
    return render_template('make_changes.html', data=result)
@app.route('/make_changes/<plant_id>/<image>', methods=["POST"])
def save_changes(plant_id,image):
    # Get the id of the plant being edited
    result = data.find_one({
        '_id':ObjectId(plant_id)
    })
    # Plant name 
    plant_name = request.form.get('plant_name')
    # Plant info
    plant_info = request.form.get('plant_info')
    # Plant benefits
    plant_benefits = request.form.get('plant_benefits')
    # Plant price
    plant_price = request.form.get('plant_price')
    # Plant_image
    plant_image = request.files['plant_image']
    if 'plant_image' not in request.files:
        plant_image.filename = image
    else:
    # if user does not select file, browser also
    # submit a empty part without filename
        if plant_image.filename == '':
            plant_image.filename = image
        else:
            # Upload image file to static folder
            plant_image.save(os.path.join(app.config['UPLOAD_FOLDER'], plant_image.filename ))

    data.update({
        '_id':ObjectId(plant_id)
    }, {
        '$set': {
            'plant_name' : plant_name,
            'plant_info' : plant_info,
            'plant_price' : plant_price,
            'plant_image' : plant_image.filename, 
        }
    })  
    return redirect(url_for('index'))
    
""" DELETE ROUTE """
@app.route('/confirm_delete/<plant_id>')
def confirm_delete(plant_id):
    # Get the id of the plant being edited
    result = data.find_one({
        '_id':ObjectId(plant_id)
    })
    return render_template('confirm_delete.html', data=result)

@app.route('/delete_plant/<plant_id>')
def delete_plant(plant_id):
    data.delete_one({
        '_id':ObjectId(plant_id)
    })
    return redirect(url_for('index'))

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
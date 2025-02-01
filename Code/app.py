from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Student493",
    database="CarDealerShip"
)
cursor = db.cursor()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for adding a new car
@app.route('/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        model_id = request.form['model_id']
        vin = request.form['vin']
        color = request.form['color']
        mileage = request.form['mileage']

        query = "INSERT INTO Cars (ModelID, VIN, Color, Mileage) VALUES (%s, %s, %s, %s)"
        values = (model_id, vin, color, mileage)
        cursor.execute(query, values)
        db.commit()

        return redirect(url_for('home'))

    return render_template('add_car.html')

# Route for deleting a car
@app.route('/delete', methods=['GET', 'POST'])
def delete_car():
    if request.method == 'POST':
        vin = request.form['vin']

        query = "DELETE FROM Cars WHERE VIN = %s"
        cursor.execute(query, (vin,))
        db.commit()

        return redirect(url_for('home'))

    return render_template('delete_car.html')

# Route for modifying a car
@app.route('/modify', methods=['GET', 'POST'])
def modify_car():
    if request.method == 'POST':
        model_id = request.form['model_id']
        vin = request.form['vin']
        color = request.form['color']
        mileage = request.form['mileage']

        query = "UPDATE Cars SET ModelID = %s, Color = %s, Mileage = %s WHERE VIN = %s"
        values = (model_id, color, mileage, vin)
        cursor.execute(query, values)
        db.commit()

        return redirect(url_for('home'))

    return render_template('modify_car.html')

if __name__ == '__main__':
    app.run(debug=True)
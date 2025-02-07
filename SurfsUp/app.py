# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, request
import warnings
warnings.filterwarnings('ignore')
import datetime as dt

import os
os.chdir('/Users/mollyenglish/Desktop/Homework/sqlalchemy-challenge/SurfsUp/Resources')
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
print(Base.classes.keys())

 #Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/stats/<start_date><br/>"
        f"/api/v1.0/stats/<start_date>/<end_date>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of weather data from the last year"""
    # Query for the last year
    # Calculate the date one year from the last date in data set.
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=366)
    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.tobs, Measurement.station, Measurement.prcp).filter(Measurement.date > query_date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of weather
    all_temps = []
    for date, tobs, station, prcp in results:
        temps_dict = {}
        temps_dict["date"] = date
        temps_dict["tobs"] = tobs
        temps_dict["station"] = station
        temps_dict["prcp"] = prcp
        all_temps.append(temps_dict)

    return jsonify(all_temps)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # Query the data
    unique_stations = session.query(Measurement.station).distinct().all()

    # Convert the result to a list
    unique_stations_list = [station[0] for station in unique_stations]

    session.close

    # Print the JSON list
    return jsonify(unique_stations_list)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #"""Return a list of weather data from the last year for USC00519281"""
    # Query the data
    # Calculate the date one year from the last date in data set.
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=366)
    results_temp = session.query(Measurement.date, Measurement.tobs, Measurement.station)\
        .filter(Measurement.station == 'USC00519281').filter(Measurement.date > query_date).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list of temperature
    all_tobs = []
    for date, tobs, station in results_temp:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_dict["station"] = station
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)

@app.route('/api/v1.0/stats/<start_date>', methods=['GET'])
def get_stats(start_date):
    # Create a session
    session = Session(engine)
    
    # Query the database for min, max, and average 'tobs' after the specified date
    results = session.query(
        func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)
    ).filter(Measurement.date >= start_date).all() 

    # Create a dictionary to hold the results
    stats = {
        "min": results[0][0],
        "max": results[0][1],
        "avg": results[0][2]
    }
    
    # Close the session
    session.close()
    
    # Return the stats as a JSON response
    return jsonify(stats)

@app.route('/api/v1.0/stats/<start_date>/<end_date>', methods=['GET'])
def get_stats2(start_date, end_date):
    # Create a session
    session = Session(engine)
    
    # Query the database for min, max, and average 'tobs' between the specified dates
    results = session.query(
        func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)
    ).filter(Measurement.date >= start_date, Measurement.date <= end_date).all()  

    # Create a dictionary to hold the results
    stats = {
        "min": results[0][0],
        "max": results[0][1],
        "avg": results[0][2]
    }
    
    # Close the session
    session.close()
    
    # Return the stats as a JSON response
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)

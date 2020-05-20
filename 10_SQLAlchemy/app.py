import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

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
        f"Welcome to Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"<br/>"
        f"Below route list Precipitaton Value for all dates from the Hawaii database <br/>"        
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"Below route list Station ID and names for from Hawaii database <br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"Below route list Temperature observations for most active Station for the last year of data <br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"Enter start date in YYYY-MM-DD format to get TMIN,TAVGand TMAX for dates greater than or equal to start date<br/>"
        f"/api/v1.0/<start_date><br/>"
        f"<br/>"
        f"Enter start and end date in YYYY-MM-DD format to get TMIN,TAVGand TMAX for dates between start and end date inclusive<br/>"
        f"/api/v1.0/<start_date>/<end_date>"

    )
@app.route("/api/v1.0/<start_date>")
def temp_start(start_date):
    """When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than 
    and equal to the start date"""
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    session.close()
    return jsonify(results)


@app.route("/api/v1.0/<start_date>/<end_date>")
def temp_start_end(start_date, end_date):
    """When given the start and the end date, calculate the TMIN, TAVG, and 
    TMAX for dates between the start and end date inclusive."""
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    session.close()
    
    return jsonify(results)

@app.route("/api/v1.0/precipitation")
def dates():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all date as the key and prcp as the value."""
    # Query all dates
    results = session.query(Measurement.date,Measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    all_dates = []
    for date, prcp in results:
        dates_dict = {}
        dates_dict["date"] = date
        dates_dict["prcp"] = prcp
        all_dates.append(dates_dict)


    return jsonify(all_dates)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations from the dataset."""
    # Query all passengers
    results = session.query(Station.station,Station.name).all()

    session.close()

    # Convert list of tuples into normal list    
    all_stations = []
    for station, name in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        all_stations.append(station_dict)
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def temperature():
    # Create our session (link) from Python to the DB
    session = Session(engine)    
    query_date = dt.date(2017,8,23) - dt.timedelta(days = 365)

    """Return a list of temperature observations (TOBS) for the previous year"""
    # Query all passengers
    results = session.query(Measurement.date,Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date > query_date).\
        group_by(Measurement.date).all()
    
    session.close()

    # Convert list of tuples into normal list
    #all_temperatures = list(np.ravel(results))
    all_temperatures = []
    for date, tobs in results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["temp"] = tobs
        all_temperatures.append(temp_dict) 
    return jsonify(all_temperatures)

if __name__ == '__main__':
    app.run(debug=True)
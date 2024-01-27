# import pytest

# from DSSATTools import (
#     Crop, SoilProfile, WeatherData, WeatherStation,
#     Management, DSSAT
#     )
# from DSSATTools.base.sections import TabularSubsection
# from datetime import datetime
# import pandas as pd
# import numpy as np
# import os
# import tempfile

# TMP = tempfile.gettempdir()

# DATES = pd.date_range('2000-01-01', '2002-12-31')
# N = len(DATES)
# df = pd.DataFrame(
#     {
#     'tn': np.random.gamma(24, 1, N),
#     'rad': np.random.gamma(15, 1.5, N),
#     'prec': np.round(np.random.gamma(.4, 10, N), 1),
#     'rh': 100 * np.random.beta(1.5, 1.15, N),
#     },
#     index=DATES,
# )
# df['TMAX'] = df.tn + np.random.gamma(5., .5, N)
# # Create a WeatherData instance
# WTH_DATA = WeatherData(
#     df,
#     variables={
#         'tn': 'TMIN', 'TMAX': 'TMAX',
#         'prec': 'RAIN', 'rad': 'SRAD',
#         'rh': 'RHUM'
#     }
# )
# # Create a WheaterStation instance
# wth = WeatherStation(
#     WTH_DATA, 
#     {'ELEV': 33, 'LAT': 0, 'LON': 0, 'INSI': 'dpoes'}
# )

# soil = SoilProfile(default_class='SIL')

# def test_run_maize():
#     crop = Crop('maize')
#     man = Management(
#         cultivar='IB0001',
#         planting_date=DATES[10],
#     )
#     man.simulation_controls['MESOM'] = 'P' # Set Soil Organic Method to Century
#     man.simulation_controls['CAOUT'] = 'Y' # Produce carbon output

#     dssat = DSSAT()
#     dssat.setup(cwd=os.path.join(TMP, 'test_mz'))
#     # Open CENTURY Static File
#     with open(os.path.join(dssat._RUN_PATH, 'static', 'StandardData', 'SOMFX048.SDA'), 'r') as f:
#         so_file = f.readlines()
#     # Made changes to the file
#     so_file_new = so_file
#     # Writes new CENTURY Static File (This will modify the file only for this simulation environtment)
#     with open(os.path.join(dssat._RUN_PATH, 'static', 'StandardData', 'SOMFX048.SDA'), 'w') as f:
#         f.writelines(so_file_new)
#     dssat.run(
#         soil=soil, weather=wth, crop=crop, management=man,
#     )
#     with open(os.path.join(dssat._RUN_PATH, 'SoilCBal.OUT')) as f:
#         soil_CBal = f.readlines()
    
#     assert os.path.exists(os.path.join(dssat._RUN_PATH, 'Summary.OUT'))
#     # dssat.close()
#     # assert not os.path.exists(dssat._RUN_PATH)

# def test_ibrahima():
#     # Random weather data
#     DATES = pd.date_range('2000-01-01', '2010-12-31')
#     N = len(DATES)
#     df = pd.DataFrame(
#         {
#         'tn': np.random.gamma(10, 1, N),
#         'rad': np.random.gamma(10, 1.5, N),
#         'prec': [0.0]* N,
#         'rh': 100 * np.random.beta(1.5, 1.15, N),
#         },
#         index=DATES,
#     )
#     df['TMAX'] = df.tn + np.random.gamma(5., .5, N)

#     # Create a WeatherData instance
#     WTH_DATA = WeatherData(
#         df,
#         variables={
#             'tn': 'TMIN', 'TMAX': 'TMAX',
#             'prec': 'RAIN', 'rad': 'SRAD',
#             'rh': 'RHUM'
#         }
#     )
#     # Create a WheaterStation instance
#     wth = WeatherStation(
#         WTH_DATA,
#         {'ELEV': 33, 'LAT': 0, 'LON': 0, 'INSI': 'dpoes'}
#     )

#     # Soil instance from default soil profile
#     soil = SoilProfile(default_class='SIL')

#     # Crop
#     crop = Crop('maize')
#     # Check how the cultivar looks like
#     crop.cultivar['IB0001']

#     man = Management(
#         cultivar='IB0001',
#         planting_date=datetime(2000, 2, 1),
#     )
#     # man.simulation_controls['MESOM'] = 'P' # Set Soil Organic Method to Century
#     # man.simulation_controls['CAOUT'] = 'Y' # Produce carbon output

#     dssat = DSSAT()
#     dssat.setup(cwd=os.path.join(os.getcwd(), 'test_mz'))
#     # Open CENTURY Static File
#     with open(os.path.join(dssat._RUN_PATH, 'static', 'StandardData', 'SOMFX048.SDA'), 'r') as f:
#         so_file = f.readlines()
#     # Made changes to the file
#     so_file_new = so_file

#     # Writes new CENTURY Static File (This will modify the file only for this simulation environtment)
#     with open(os.path.join(dssat._RUN_PATH, 'static', 'StandardData', 'SOMFX048.SDA'), 'w') as f:
#         f.writelines(so_file_new)
#     dssat.run(
#         soil=soil, weather=wth, crop=crop, management=man,
#     )
#     # Open the Carbon Balance file
#     with open(os.path.join(dssat._RUN_PATH, 'SoilCBal.OUT')) as f:
#         soil_CBal = f.readlines()
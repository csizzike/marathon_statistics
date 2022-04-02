import pandas as pd
import numpy as np

def calculate(bszm): 

    bszm['1.day/1.length'] = np.where(bszm['event_year'] == 2015, 14.2, bszm['1.day/1.length'])
    bszm['1.day/2.length'] = np.where(bszm['event_year'] == 2015, 16.1, bszm['1.day/2.length'])
    bszm['1.day/3.length'] = np.where(bszm['event_year'] == 2015, 16.2, bszm['1.day/3.length'])
    bszm['1.day/length'] = np.where(bszm['event_year'] == 2015, 46.5, bszm['1.day/length'])
    bszm['2.day/1.length'] = np.where(bszm['event_year'] == 2015, 16.1, bszm['2.day/1.length'])
    bszm['2.day/2.length'] = np.where(bszm['event_year'] == 2015, 15.3, bszm['2.day/2.length'])
    bszm['2.day/3.length'] = np.where(bszm['event_year'] == 2015, 21.3, bszm['2.day/3.length'])
    bszm['2.day/length'] = np.where(bszm['event_year'] == 2015, 52.7, bszm['2.day/length'])
    bszm['3.day/1.length'] = np.where(bszm['event_year'] == 2015, 13.2, bszm['3.day/1.length'])
    bszm['3.day/2.length'] = np.where(bszm['event_year'] == 2015, 17.1, bszm['3.day/2.length'])
    bszm['3.day/3.length'] = np.where(bszm['event_year'] == 2015, 13.1, bszm['3.day/3.length'])
    bszm['3.day/length'] = np.where(bszm['event_year'] == 2015, 43.4, bszm['3.day/length'])
    bszm['4.day/1.length'] = np.where(bszm['event_year'] == 2015, 16.5, bszm['4.day/1.length'])
    bszm['4.day/2.length'] = np.where(bszm['event_year'] == 2015, 18.1, bszm['4.day/2.length'])
    bszm['4.day/3.length'] = np.where(bszm['event_year'] == 2015, 17.1, bszm['4.day/3.length'])
    bszm['4.day/length'] = np.where(bszm['event_year'] == 2015, 51.7, bszm['4.day/length'])

    bszm['1.day/1.length'] = np.where(bszm['event_year'] == 2017, 14.1, bszm['1.day/1.length'])
    bszm['1.day/2.length'] = np.where(bszm['event_year'] == 2017, 16, bszm['1.day/2.length'])
    bszm['1.day/3.length'] = np.where(bszm['event_year'] == 2017, 16.1, bszm['1.day/3.length'])
    bszm['1.day/length'] = np.where(bszm['event_year'] == 2017, 46.2, bszm['1.day/length'])
    bszm['2.day/1.length'] = np.where(bszm['event_year'] == 2017, 16, bszm['2.day/1.length'])
    bszm['2.day/2.length'] = np.where(bszm['event_year'] == 2017, 15.2, bszm['2.day/2.length'])
    bszm['2.day/3.length'] = np.where(bszm['event_year'] == 2017, 21.2, bszm['2.day/3.length'])
    bszm['2.day/length'] = np.where(bszm['event_year'] == 2017, 52.4, bszm['2.day/length'])
    bszm['3.day/1.length'] = np.where(bszm['event_year'] == 2017, 13.1, bszm['3.day/1.length'])
    bszm['3.day/2.length'] = np.where(bszm['event_year'] == 2017, 17, bszm['3.day/2.length'])
    bszm['3.day/3.length'] = np.where(bszm['event_year'] == 2017, 13, bszm['3.day/3.length'])
    bszm['3.day/length'] = np.where(bszm['event_year'] == 2017, 43.1, bszm['3.day/length'])
    bszm['4.day/1.length'] = np.where(bszm['event_year'] == 2017, 16.3, bszm['4.day/1.length'])
    bszm['4.day/2.length'] = np.where(bszm['event_year'] == 2017, 18, bszm['4.day/2.length'])
    bszm['4.day/3.length'] = np.where(bszm['event_year'] == 2017, 17, bszm['4.day/3.length'])
    bszm['4.day/length'] = np.where(bszm['event_year'] == 2017, 51.3, bszm['4.day/length'])
    return bszm

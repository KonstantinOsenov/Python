import numpy as np
import pandas as pd

import requests

import re
import csv

import datetime
from datetime import timedelta

import configparser

from io import StringIO

rs = requests.Session()

from_date = '2023-11-09'
to_date   = '2023-11-10'

def get_disp(rs, from_date, to_date):
    _stopdate = datetime.datetime.strptime(to_date, '%Y-%m-%d').date()
    _startdate = datetime.datetime.strptime(from_date, '%Y-%m-%d').date() #now we need to know the last report downloaded

    finalDF = pd.DataFrame()
    
    while _startdate < _stopdate:
        
        _fname = str(_startdate + timedelta(days=1)) + ".csv" #we already have report for date _startdate...now we add +1 day and get the nex avail report
        _fname2 = _fname.replace("-", "_") #need to change - to _
        print(_fname2)
     
        #Dispute DL from adyen downloads CSV data as bytes;
        #needs to be converted to string via StringIO before loading into a DF
        csvbytes = str(rs.get("https://ca-live.adyen.com/reports/download/Company/<company_id>/dispute_report_" + _fname2
                              ,auth=('<user_id>', '<password>')).content,'utf-8')
        
        csvobject = StringIO(csvbytes)
        
        df = pd.read_csv(csvobject, index_col=False,)      
        df.columns = df.columns.str.replace(' ', '_')
        df.columns = df.columns.str.lower()

        finalDF = pd.concat([df,finalDF],ignore_index=True)
               
        _startdate = _startdate + timedelta(days=1) #this contorls the WHILE loop...increase by one day

    return finalDF

df = get_disp(rs, from_date, to_date)

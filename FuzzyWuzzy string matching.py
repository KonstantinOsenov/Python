# to test
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import pandas as pd
import random

import re

import numpy as np
import threading

data = pd.read_csv("data.csv")

no_dup = data['Email'].drop_duplicates().to_list()

def fuzzy(no_dup):

    results = []
        
    for i in no_dup:

        for x in no_dup:

            ratio = int(fuzz.ratio(i.lower(), x.lower()))

            if ratio > 90 and i != x:

                print(i,x)
                                
        no_dup.remove(i)

    print(results)


def e_structure(no_dup):

    compre = pd.read_csv("compre.csv", delimiter=";",dtype="str")

    print(compre)

    alpha = compre['alpha'].drop_duplicates().to_list()
    num = compre['num'].drop_duplicates().to_list()
    sym = compre['sym'].drop_duplicates().to_list()
    
    for i in no_dup:

        build_struc = ""

        for letter in i.lower().split("@")[0]:

            if letter in alpha:

                build_struc = build_struc + "alpha"
                
            if letter in num:

                build_struc = build_struc + "num"

            if letter in sym:

                build_struc = build_struc + "sym"
        no_dup.remove(i)

        if len(build_struc) > 0:
            print(build_struc, i)

#e_structure(no_dup)
fuzzy(no_dup)

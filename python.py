# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 00:15:33 2021

@author: asus
"""
"les librairies utilisées"
# pandas : panel data , pour une facile manipulation des données.
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# importer les données de notre fichier dataset demo.
demographic_data = pd.read_csv("C:/Users/asus/Desktop/p/nndb_flat_version2.csv")



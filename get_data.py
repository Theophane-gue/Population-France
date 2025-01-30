#This file contain a script getting data from data.gouv.fr via API



# 1. Import the package
import requests as re
import json
import os
import pandas as pd






# 2.

requete_dataset = "https://www.data.gouv.fr/fr/datasets/r/d2a15598-9573-4082-bacd-7c73504e7839"

get_data = re.get(requete_dataset , verify= False)
data_from_net = get_data.content
print(data_from_net)
#data = da(data_from_net )

#This file contain a script getting data from data.gouv.fr via API



# 1. Import the package
import requests as re
import json
import os
import pandas as pd
import tarfile


def get_data():
    url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz'
    
    response = re.get(url, stream=True)
    if response.status_code == 200:
        with open('tolldata.tgz', 'wb') as f:
            f.write(response.raw.read())
    return None




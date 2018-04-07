# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:25:00 2018 by Apoorva Karn """
import requests #for calling
from bs4 import BeautifulSoup #converts the text into structured form
url="https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2017"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
soup
tables=soup.find_all("table")
rows=list()
for table in tables:
    if(table.get("id")=="data"):
        for row in table.find_all("tr"):
            rows.append(row)
            for col in row.find_all("td"):
                print(col.contents[0])
                    
                    
        

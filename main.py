import logging
import os
import requests

BASE_URL="https://webservices.ignou.ac.in/Pre-Question/"
DEC="Question Paper December"
JUNE="Question Paper June"

YEARS=["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]

CURRENT_DATE=os.date

print(CURRENT_DATE)
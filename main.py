'''
File: main.py
File Created: Wednesday, 25th January 2023 9:58:16 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from easy_parse import EasyParser
with open("test.html", 'r') as html_file:
    data_parser = EasyParser(html=html_file.read())


@data_parser.get_all("time_of_day", xpath="body/div/section/@id")
def timeofday(element):
    return element


print(data_parser.data_mapping)

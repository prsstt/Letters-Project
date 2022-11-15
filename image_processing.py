#######GUI#######
import PySimpleGUI as sg

sg.change_look_and_feel('Dark')

layout = [[sg.T("")], [sg.Text("Choose a folder: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FolderBrowse(key="-IN-")],[sg.Button("Submit")]]
#layout = [
 #           [[sg.T("")], sg.Text("Choose a file: ")],
  #          [sg.FolderBrowse(key="-IN-"), sg.Button('Sumbit')]
   #          
    #        ]

window = sg.Window('Letters Project by.parasite', layout, size=(600,150))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        #print(values["-IN-"])
        folder_path = (values["-IN-"])
        print(folder_path)
        window.close()
########################


import os

###########OCR################
import pytesseract as pt
from PIL import Image

pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
def main():
    path = folder_path
  
    fullTempPath ="C:\\Users\\sh0cky\\Desktop\\Desktop\\PROJEKTY\\PROJEKT LISTY\\Post\\PostoutputFile.csv"
  
    for imageName in os.listdir(path):
        inputPath = os.path.join(path, imageName)
        img = Image.open(inputPath)
  
        text = pt.image_to_string(img, lang ="pol")
        file1 = open(fullTempPath, "a+")
  
        
        file1.write("\n")
  
        
        file1.write(text+"\n"+'Tczew')
        file1.close() 
  
    
    file2 = open(fullTempPath, 'r')
    print(file2.read())
    file2.close()        
  
  
if __name__ == '__main__':
    main()
############################ADRES FILTERING###################

import locationtagger
import nltk
locations_path = "C:\\Users\\sh0cky\\Desktop\\Desktop\\PROJEKTY\\PROJEKT LISTY\\Post\\PostoutputFile.csv"
f = open("C:\\Users\\sh0cky\\Desktop\\Desktop\\PROJEKTY\\PROJEKT LISTY\\Post\\PostoutputFile.csv", 'r')
place_entity = locationtagger.find_locations(text = f.read())
 
# getting all country regions
print("The countries regions in text : ")
print(place_entity.country_regions)
 
# getting all country cities
print("The countries cities in text : ")
print(place_entity.country_cities)
 
# getting all other countries
print("All other countries in text : ")
print(place_entity.other_countries)
 
# getting all region cities
print("The region cities in text : ")
print(place_entity.region_cities)
 
# getting all other regions
print("All other regions in text : ")
print(place_entity.other_regions)
 
# getting all other entities
print("All other entities in text : ")
print(place_entity.other)
f.close()
#################################DISTANCE MATRIX######################
# from encodings import utf_8
# import json

# import requests

# payload={}
# headers = {}
# #wprowadzanie input adresów z csv/json
# origins = r'C:\Users\sh0cky\Desktop\Desktop\PROJEKTY\PROJEKT LISTY\Post\PostoutputFile.csv'
# destinations = r'C:\Users\sh0cky\Desktop\Desktop\PROJEKTY\PROJEKT LISTY\Post\PostoutputFile.csv'


# url = "https://api.distancematrix.ai/maps/api/distancematrix/json?origins={}&destinations={}&key=YAfIULoihwLRkGyzZAjiOGsbPtsZV"
# r = requests.get(url)
 
# response = requests.request("GET", url, headers=headers, data=payload)


# DictData = response.json()
# json_formatted_str = json.dumps(DictData, indent = 4, ensure_ascii = False)
# print(json_formatted_str)

# with open(r"C:\Users\sh0cky\Desktop\PROJEKTY\PROJEKT LISTY\adresses.json", "a") as outfile:
#     outfile.write(json_formatted_str)
#####################################

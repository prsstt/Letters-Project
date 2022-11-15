import locationtagger
import nltk
locations_path = "C:\\Users\\sh0cky\\Desktop\\Desktop\\PROJEKTY\\PROJEKT LISTY\\Post\\PostoutputFile.csv"
f = open("C:\\Users\\sh0cky\\Desktop\\Desktop\\PROJEKTY\\PROJEKT LISTY\\Post\\PostoutputFile.csv", 'r')
content = f.read()
print(content)
place_entity = locationtagger.find_locations(text = f)
 
# getting all countries 
print("The countries in text : ")
print(place_entity.countries)
 
# getting all states
print("The states in text : ")
print(place_entity.regions)
 
# getting all cities
print("The cities in text : ")
print(place_entity.cities)
f.close()
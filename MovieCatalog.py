from algoliasearch import algoliasearch
import json

client = algoliasearch.Client("Your ApplicationID","Your API key")

indexEx = client.init_index("movie")
indexEx.clear_index()

batch = json.load(open('DataFiles/data.json')) + json.load(open('DataFiles/data2.json')) + json.load(open('DataFiles/data3.json')) + json.load(open('DataFiles/data4.json'))
batch2 = json.load(open('DataFiles/data5.json')) + json.load(open('DataFiles/data6.json')) + json.load(open('DataFiles/data7.json')) + json.load(open('DataFiles/data8.json'))
batch3 = json.load(open('DataFiles/data9.json')) + json.load(open('DataFiles/data10.json')) + json.load(open('DataFiles/data11.json')) + json.load(open('DataFiles/data12.json'))
batch4 = json.load(open('DataFiles/data13.json')) + json.load(open('DataFiles/data14.json')) + json.load(open('DataFiles/data15.json')) + json.load(open('DataFiles/data16.json'))

indexEx.add_objects(batch)
indexEx.add_objects(batch2)
indexEx.add_objects(batch3)
indexEx.add_objects(batch4)

indexEx.set_settings({"customRanking": ["desc(title)"]})
indexEx.set_settings({"searchableAttributes": ["title","cast"]})

print(indexEx.search("happy valley"))

print(indexEx.search("Lilian gish"))
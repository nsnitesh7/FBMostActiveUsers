import facebook

import requests


access_token = 'CAACEdEose0cBALG8g4bbP97jAFNvxuxGNdLP2F1LUoZC2BTqpkzM9ZBDO5174KBJUJbUw1F8eSrcUyyesfq5kYWNZBhw0kMPEz80LSr1SmERlEjP0BThS1F3Hte3xD52Ca9DMWoGwDvRxw0bMdv29iZC7GmWvAoqC1w7Ag21AU98v2bxI4xHPk6DQbyVLYZCX5DSdxKQktQZDZD'
graph = facebook.GraphAPI(access_token)

data=[]

with open('djsathiya_agarathi_friends.txt') as fp:
    for line in fp:
        data.append(line)

for d in data:
    try:
        user= d[0:len(d)-1]
        profile = graph.get_object(user)
        print profile['id']
    except:
        pass

'''
user = 'RasputinSG'
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'feed')
print profile['id']
'''
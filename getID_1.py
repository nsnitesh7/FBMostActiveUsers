import facebook

import requests

from sets import Set

personIDs = Set([])

access_token = 'CAACEdEose0cBAFw672LPKNRSM2y5ochwrmRNGllxLdS9PxiROrounr67vWnqSXYSfXwfI4m9JahLoBH81gAb7HyJJhxJVgtGvLjhyTXI0wZA6XngSUYKwSuhQdhsmFTYVGYeb6sB0xseVNg8mBFYFZBieQtFiugH60lgI6LWkq6jaZAOWX0jdllLF7clkbfZAdRtyanHjQZDZD'
graph = facebook.GraphAPI(access_token)

with open('DjKiLLaWiLL_friends.txt') as fp:
    for line in fp:
        try:
            user= line[0:len(line)-1]
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
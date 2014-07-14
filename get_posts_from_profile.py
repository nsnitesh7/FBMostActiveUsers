"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""
import facebook
import requests

from sets import Set

personIDs = Set([])

access_token = 'CAACEdEose0cBANA1YJ1ACJCiXXvZCX6BXqaAuDONxLEZBBaAeYbTHUAfSzpqQFs7kiZCUyoNZB2inKcaZBZB9oXSB9NZA1a8qS1ZBaHRvf1mibiubiZAoMpv4ru7xeZCQfgPHhZBRnOTejOAZAVfj9TRZBZCbUoGqZBbGeimczkk0VhHZBMZB8LIZB8A0mZBaVyYyrLMehvCtDzVHwZAE7x2OQZDZD'
graph = facebook.GraphAPI(access_token)

def printF(ID):
    personIDs.add(ID)

def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
#    print post['message']
    #    print post
    if 'likes' in post:
        pl= post['likes']
        while True:
            try:
                # Perform some action on each post in the collection we receive from
                # Facebook.
#                print pl
                [printF(liker['id']) for liker in pl['data']]
#                [some_action(post=post) for post in posts['data']]
                # Attempt to make a request to the next page of data, if it exists.
                pl = requests.get(pl['paging']['next']).json()
            except KeyError:
                # When there are no more pages (['paging']['next']), break from the
                # loop and end the script.
                break

    if 'comments' in post:
        pc= post['comments']
        while True:
            try:
                # Perform some action on each post in the collection we receive from
                # Facebook.
#                print pl
                [printF(commenter['from']['id']) for commenter in pc['data']]
#                [some_action(post=post) for post in posts['data']]
                # Attempt to make a request to the next page of data, if it exists.
                pc = requests.get(pc['paging']['next']).json()
            except KeyError:
                # When there are no more pages (['paging']['next']), break from the
                # loop and end the script.
                break


#    p = graph.get_object(post['id'])
#    print p['likes']['data']
# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/

# Look at Bill Gates's profile for this example by using his Facebook id.

'''
#for facebook pages:
user = 'RasputinSG'
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'feed')
'''

#for facebook user profile:
user = 'dejavubq'
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'feed')
# Wrap this block in a while loop so we can keep paginating requests until
# finished.
while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [some_action(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break

for p in personIDs:
    print p
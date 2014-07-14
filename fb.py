import facebook

token = 'CAACEdEose0cBAP2KLWJPXpbgoI62uO03F8ZBPCQF78y4SyKVZBdEZAUkcbbmDemVJQZBjNRZAZBnmbgbFHAIEVSuzLLiCZBVJmAyMMd8AutwuNIWFx4e8qSbxJpkLeS3GJPrBpLhSSF30PsXlhodtS1UoWQs6mTv3BGfojcCsj95KuNAQ3a29rtIKn4kbWxETu4T4kndo51RAZDZD'

user = 'Rumourscq'

graph = facebook.GraphAPI(token)
profile = graph.get_object(user)
#user = graph.get_object("me")
print profile["id"]

friends = graph.get_connections(profile['id'], "friends")

print len(friends['data'])

'''
friend_list = [friend['name'] for friend in friends['data']]

print friend_list
'''
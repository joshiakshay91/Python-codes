#Author: Akshay Joshi
#Desc: Sample script in python to like all the posts from a user
#not for spamming but for understanding the SDK
import facebook
token = "token grabbed from facebook"
#use the token
graph=facebook.GraphAPI(token)
#username get_object
profile=graph.get_object("robertdowneyjr")
posts=graph.get_connections(profile['id'],"posts")
#for all the posts from the user
#try exceptions for posts that are not likable
for post in posts['data']:
    try:
        graph.put_object(post['id'],"likes")
        print "Liking--> " + post['message']
    except:
        continue

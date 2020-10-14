from InstagramAPI import InstagramAPI
import random
from time import sleep
import pprint

users_list = []
following_users = []
follower_users = []

class instaBot:
    def __init__(self):
        self.api = InstagramAPI("username",'password')
        
    def get_likes_list(self,username):
        api = self.api
        api.login()
        api.searchUsername(username)
        result = api.LastJson
        username_id = result['user']['pk']
        user_posts = api.getUserFeed(username_id)
        result = api.LastJson
        media_id = result['items'][0]['id']
        api.getMediaLikers(media_id)
        users = api.LastJson['users']
        for user in users:
            users_list.append({'pk':user['pk'], 'username':user['username']})
        pprint.pprint(users_list)

    def follow(self,users_list):
        api = self.api
        api.login()
        api.getSelfUsersFollowing()
        result = api.LastJson

        count = 0

        for user in result['users']:
            following_users.append(user['pk'])
        for user in users_list:
            if(user['pk'] in following_users):
                print("already following @"+user['username'])
            else:
                print("now following @"+user['username'])
                api.follow(user['pk'])
                randomNo = random.randint(20, 35)
                count  = count + 1
                sleep(randomNo)
                print("total number of people followed :" + str(count))
                print("interval time :" + str(randomNo))
                
    # def get_likes_list(self,username):
    #     api = self.api
    #     api.login()
    #     api.searchUsername(username)
    #     result = api.LastJson
    #     username_id = result['user']['pk']
    #     user_posts = api.getUserFeed(username_id)
    #     result = api.LastJson 
    #     media_id = result['items'][0]['id']
        
    #     api.getMediaLikers(media_id)
    #     users = api.LastJson['users']
    #     for user in users:
    #         users_list.append({'pk':users[0],'username':users['username']})
    #     pprint.pprint(users_list)


    def unfollow(self):
        api = self.api
        api.login()
        api.getSelfUsersFollowers()
        result = api.LastJson
        for user in result['users']:
            follower_users.append({'pk':user['pk'],'username':user['username']})

        api.getSelfUsersFollowing()
        result = api.LastJson

        for user in result['users']:
            following_users.append({'pk':user['pk'],'username':user['username']})

        for user in following_users:
            if not user['pk'] in follower_users:
                print("unfolowing @"+user['username'])
                api.unfollow(user['pk'])
                sleep(20)



bot = instaBot()
# get likes of below user
bot.get_likes_list("target")
bot.follow(users_list)
# bot.unfollow()
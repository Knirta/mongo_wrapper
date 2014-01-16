# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:38:33 2014

@author: localadmin
"""

from pprint import pprint
from wrapperdb import WrapperDB
from user import Users
from backlog import BackLog
from counter import Counter


def wrapper_test():
    wrapperdb = WrapperDB()
    wrapperdb.choose_database("bugtracker")
    wrapperdb.choose_collection("users")
    wrapperdb.find_and_modify(query={"fname": "Katya"},
                               update={"$inc": {"id": 1}},
                               new=True)
    #wrapperdb.insert_data({"id": _id, "email": email, 
                          # "password": password, "fname": fname,
                           #"lname": lname, "role": role,
                           #"avatar": avatar, "status": status})
    #cursor = wrapperdb.get_data({"status":"active"}, {"_id": 0, "email": 1, "role": 1} )
    #for row in cursor:
     #   pprint(row)   
    #wrapperdb.remove_data({"fname":"Katya"})
    #print wrapperdb.check_data({"status": "active"}, "email", "some@com")
    
def users_test():
    users = Users()
    users.add_user(1, "milo@com", "tratata", "Katya", "Korolchuk",
                   "developer", "picture", "active")
    #users.add_user(2, "croco@com", "tutu", "Nadya", "Illyuk",
                   #"qc", "picture2", "active")
    #users.add_user(3, "some@com", "gavgav", "Dima", "Sych",
                   #"admin", "picture3", "active")
    #users.get_user({"status": "active"},)    
    #users.remove_user({"email": "milo@com"})
    
def backlog_test():
    backlog = BackLog()
    #backlog.add_backlog("sprint3", [], [])  #will write when ready 
    backlog.create_story({"name": "name1111", "description": "lalala",
                          "status": "active", "sprint": 1});
    backlog.create_story({"name": "name2222", "description": "tralalala",
                          "status": "banned", "sprint": 1});
    backlog.add_story(1)
    
    
def counter_test():
    counter = Counter()
    counter.create_counter()
    pprint(counter.get_next_sequence("userid"))
    
if __name__ == '__main__':
    #wrapper_test()
    #users_test()
    backlog_test()
    #counter_test()


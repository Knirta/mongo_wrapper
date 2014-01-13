# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:35:00 2014

@author: localadmin
"""

from wrapper import WrapperDB
from user import Users
from pprint import pprint
from counter import Counter

class BackLog(WrapperDB):
    def __init__(self):
        super(BackLog, self).__init__()
        self.choose_database("bugtracker")
        self.choose_collection("backlog")
              
    def add_backlog(self, name, members, stories):
               
        counter = Counter()
        self.insert_data({"backlog_id": counter.get_next_sequence("backlogid"),
                          "name": name, "members": members,
                          "stories": stories})
                          
    def create_story(self, name, description, status, comments, tasks, sprint):
        stories = []
        counter = Counter()        
        story ={"story_id": counter.get_next_sequence("storyid"), 
                "name": name,
                "description": description,
                "status": status,
                "comments": comments,
                "tasks": tasks,
                "sprint": sprint  
                }
        stories.append(story)
        return stories
    
    def add_story(self, backlog_id, name):
        self.update_data({"backlog_id": backlog_id}, {"$set": {"stories": name}})
        
        
    
  
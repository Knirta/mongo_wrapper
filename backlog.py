# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:35:00 2014

@author: localadmin
"""

from wrapperdb import WrapperDB
from user import Users
from pprint import pprint
from counter import Counter

class BackLog(WrapperDB):
    _stories = []
    def __init__(self):
        super(BackLog, self).__init__()
        self.choose_database("bugtracker")
        self.choose_collection("backlog")
              
    def add_backlog(self, name):
               
        counter = Counter()
        self.insert_data({"_id": counter.get_next_sequence("backlogid"),
                          "name": name, "members": [],
                          "stories": []})
                          
    def create_story(self, dictionary ):
        counter = Counter()        
        story ={"story_id": counter.get_next_sequence("storyid"), 
                "name": dictionary.get("name"),
                "description": dictionary.get("description"),
                "status": dictionary.get("status"),
                "comments": dictionary.get("comments",""),
                "tasks": dictionary.get("tasks", ""),
                "sprint": dictionary.get("sprint") 
                }
        self._stories.append(story)
        return self._stories
    
    def add_story(self, backlog_id):
        self.update_data({"backlog_id": backlog_id}, {"$set": {"stories": self._stories}})
        
        
    
  
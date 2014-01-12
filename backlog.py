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
                          
    def get_backlog_by_id(self, backlog_id):
        return self.get_one_document({"backlog_id": backlog_id})
        
    

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:28:10 2014

@author: localadmin
"""

class BackLog(WrapperDB):


    def create_comment(self, comment_id, author_id, text):
        comment = {"comment_id": comment_id,
                   "author_id": author_id,
                   "text": text                   
                   }
        self.comments.append(comment)
        #return self.comments
    
    def create_task(self, task_id, name, description, assign_to, task_type, state,
                    estimate):
        task = {"task_id": task_id,
                "name": name,
                "description": description,
                "assign_to": assign_to,
                "task_type": task_type,
                "state": state,
                "estimate": estimate,
                "comments": self.comments
                }
        self.tasks.append(task)
                
    
       
 """   def add_json_backlog(self, backlog_id, name, members, stories):
        members = []
        for :
        stories = []
        for :
            story = create_story(story_id, name, description, status, comments, tasks, sprint)
            stories.append(story)
            """
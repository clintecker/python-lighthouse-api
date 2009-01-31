# 
#  lighthouse.py
#  Python Lighthouse API
#
#  Lighthouse simple hosted issue tracking, bug tracking, and project
#   management software.
#
#  They also have an XML-based API for working with your projects
#  
#  Created by Clinton Ecker on 2009-01-31.
#  Copyright 2009 Clint Ecker. All rights reserved.
# 

class Lighthouse(object):
    """The main lighthouse object for managing the connection"""
    def __init__(self, arg):
        super(Lighthouse, self).__init__()
        self.arg = arg

class Ticket(object):
    """Tickets are individual issues or bugs"""
    def __init__(self, arg):
        super(Ticket, self).__init__()
        self.arg = arg

class Project(object):
    """Projects contain milestones, tickets, messages, and changesets"""
    def __init__(self, arg):
        super(Project, self).__init__()
        self.arg = arg

class Milestone(object):
    """Milestones reference tickets"""
    def __init__(self, arg):
        super(Milestone, self).__init__()
        self.arg = arg
        
class Message(object):
    """Messages are notes"""
    def __init__(self, arg):
        super(Message, self).__init__()
        self.arg = arg
        
class User(object):
    """A user"""
    def __init__(self, arg):
        super(User, self).__init__()
        self.arg = arg
         
        
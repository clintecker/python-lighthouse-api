# 
#  lighthouse.py
#  Python Lighthouse API
#
#  Lighthouse simple hosted issue tracking, bug tracking, and project
#	management software.
#
#  They also have an XML-based API for working with your projects
#  
#  http://lighthouseapp.com
#  http://lighthouseapp.com/api
#
#  Created by Clinton Ecker on 2009-01-31.
#  Copyright 2009 Clint Ecker. All rights reserved.
# 
import urllib
import os.path
import pprint
from xmltodict import xmltodict
from dateutil.parser import *
from dateutil.tz import *


class Lighthouse(object):
	"""The main lighthouse object for managing the connection"""
	
	def __init__(self, token=None, url=None):
		super(Lighthouse, self).__init__()
		self.token = token
		self.url = url
	
	def _datetime(self, data):
		return parse(data)
	
	def _integer(self, data):
		if data:
			return int(data,10)
		else:
			return None
	
	def _boolean(self, data):
		if data == 'true' or data == '1' or data == 1:
			return True
		else:
			return False
	
	def _string(self, data):
		return data
	
	def _nil(self):
		return None
	
	def _get_data(self, path):
		if self.token != None and self.url != None:
			endpoint = os.path.join(self.url, path)
			rh = urllib.urlopen(endpoint)
			data = rh.read()
			return self._parse_xml(data)
		else:
			print "Error: Please set token and url properly"

	def _parse_xml(self, xmldata):
		return xmltodict(xmldata)
	
	def _parse_field(self, field):
		field_type = None
		field_name = None
		field_attributes = None
		converter = None
		
		attributes = field.get('attributes', {})
		field_value = field.get('cdata', None)
		field_name = field.get('name', None)
		
		if attributes:
			field_type = attributes.get('type', None)

		if field_type:
			converter = getattr(self,'_'+field_type)
			field_value = converter(field_value)
		
		return (field_name, field_value, field_type)
		
	@property	
	def projects(self):
		path = 'projects.xml'
		project_list = self._get_data(path)
		#pprint.pprint(project_list['children'][0]['children'])
		projects = []
		for project in project_list['children']:
			p_obj = Project()
			for field in project['children']:
				field_name, field_value, field_type = self._parse_field(field)
				p_obj.__setattr__(field_name, field_value)
			projects.append(p_obj)
		return projects
				
class Ticket(object):
	"""Tickets are individual issues or bugs"""
	def __init__(self, arg):
		super(Ticket, self).__init__()
		self.arg = arg

class Project(object):
	"""Projects contain milestones, tickets, messages, and changesets"""
	def __init__(self, archived=None, created_at=None,
	description=None, p_id=None, name=None, open_tickets_count=None,
	permalink=None, public=None, updated_at=None, open_states=None,
	closed_states=None, open_states_list=None, closed_states_list=None):
		
		super(Project, self).__init__()
		
		self.archived 		= archived
		self.created_at 	= created_at
		self.description 	= description
		self.id 			= p_id
		self.name 			= name
		self.permalink 		= permalink
		self.public			= public
		self.updated_at		= updated_at
		self.open_states	= open_states
		self.closed_states	= closed_states
		self.open_states_list = open_states_list
		self.closed_states_list = closed_states_list
		self.open_tickets_count = open_tickets_count
	
	def __repr__(self):
		if self.name:
			return "Project: %s" % (self.name,)
		else:
			return "Project: Unnamed"

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
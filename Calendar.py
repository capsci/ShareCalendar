'''
	file Calendar.py
	Manipulates categories.json, which maps emails to corrosponding tags
	Available functions =>
		getCategories(): returns list of all available categories from JSON
		getList(category): returns list of all calendarID's listed under given category
		addCalendar(calendarID, category): adds new calendar to given category
		addCategory(category): Adds new category to JSON
		removeCategory(category): Removes existing category to JSON

'''
__author__ = "Kapil Somani"
__email__ = "kmsomani@ncsu.edu"
__status__ = "Prototype"

import json

# manipulate custom data structure storing details about multiple categories and list of accounts associated with it
class CalendarStructure(object):

	data = None;
	fileName = "categories.json";
	
	"""docstring for CalendarStructure"""
	def __init__(self, inpFile = fileName):
		super(CalendarStructure, self).__init__();
		self.fileName = inpFile;
		# read the file and populate data
		try:
			with open(self.fileName) as data_file:
				self.data = json.load(data_file);
		except:
			print "File NOT found", 
		
	# returns list of categories available
	def getCategories(self):
		return self.data.keys();

	# returns all listed email IDs under given category
	def getList(self, key):
		return self.data[key]["calendarList"];

	# adds email to an existing category
	def addCalendar(self, calendarID, category):
		self.data[category]["calendarList"].append(calendarID);

	# adds new category to existing list
	def addCategory(self, name, description):
		self.data[name] = {'description': description, 'calendarList': []}
		self.updateJSON();

	# removes category from existing list
	def removeCategory(self, name):
		try:
			del self.data[name];
			self.updateJSON();
		except:
			print "Category ", name," does not exist";

	# save the changes made on categories.json
	def updateJSON(self):
		try:
			json.dump(self.data, open(self.fileName, 'w'));
		except:
			print "Error in updating Calendar Structure"




if __name__ == "__main__":
	cs = CalendarStructure();
	categories = cs.getCategories();
	print(categories);
	for category in categories:
		print category, " -> ", cs.getList(category);
	cs.addCategory("dummy","dummy category");
	categories = cs.getCategories();
	print(categories);
	cs.removeCategory("dummy");
	categories = cs.getCategories();
	print(categories);
	cs.addCalendar('newCal', 'seminars');
	for category in categories:
		print category, " -> ", cs.getList(category);

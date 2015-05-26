import json

# manipulate custom data structure storing details about multiple categories and list of accounts associated with it
class CalendarStructure(object):

	data = None;
	fileName = "categories.json";
	
	"""docstring for CalendarStructure"""
	def __init__(self, inpFile = fileName):
		super(CalendarStructure, self).__init__();
		#print "Contructor";
		self.fileName = inpFile;
		try:
			with open(self.fileName) as data_file:
				self.data = json.load(data_file);
		except:
			print "File", 
		
	# returns list of categories available
	def getCategories(self):
		return self.data.keys();

	# returns all listed email IDs under given category
	def getList(self, key):
		return self.data[key]["list"];

	# adds new category to existing list
	def addCategory(self, name, description):
		self.data[name] = {'description': description, 'list': []}
		try:
			json.dump(self.data, open(self.fileName, 'w'));
		except:
			print "Error in saving modified Calendar Structure"

	# removes category from existing list
	def removeCategory(self, name):
		try:
			del self.data[name];
			try:
				json.dump(self.data, open(self.fileName, 'w'));
			except:
				print "Error in saving modified Calendar Structure"
		except:
			print "Category ", name," does not exist";



if __name__ == "__main__":
	cs = CalendarStructure();
	categories = cs.getCategories();
	print(categories);
#	for category in categories:
#		print category, " -> ", cs.getList(category);
	cs.addCategory("dummy","dummy category");
	categories = cs.getCategories();
	print(categories);
	cs.removeCategory("dummy");
	categories = cs.getCategories();
	print(categories);

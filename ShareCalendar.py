'''
	file: ShareCalendar.py 
	Starter file for Share Calendar Applciation
'''
__author__ = "Kapil Somani"
__email__ = "kmsomani@ncsu.edu"
__status__ = "Prototype"

import Credentials
import Calendar

from datetime import datetime
from apiclient.discovery import build
from httplib2 import Http

creds = None

# complete list of paramters can be found at https://developers.google.com/google-apps/calendar/v3/reference/events/list
def generate_query(calId, maxResults = None, timeFrom = None, timeTo = None, noResults = None, queryText = None):
	timeNow = datetime.utcnow().isoformat() + 'Z'
	if timeFrom == None:
		timeFrom = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	if timeTo == None:
		timeTo = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	calendarId = calId;
	if noResults == None:
		noResults = 10;

	return service.events().list(calendarId = calId,
		timeMin = timeNow,
		maxResults = noResults,
		singleEvents = True,
		q = queryText,
		orderBy = 'startTime').execute()
	
def fetch_events():

	calIds = calendar.getList('seminars');
	events = [];
	for item in calIds:
		print "For calendarId: ", item;
		q = generate_query(calId = item, queryText='Test');
		events.extend(q.get('items', []));

	if not events:
		print 'No upcoming events found.';
	for event in events:
		start = event['start'].get('dateTime', event['start'].get('date'));
		print start, event['summary'];	

calendar = Calendar.Calendar();
credentials = Credentials.get_credentials();
service = build('calendar', 'v3', http=credentials.authorize(Http()))
print 'Getting the upcoming 10 events'
fetch_events()

    
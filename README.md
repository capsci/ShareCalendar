# ShareCalendar
Categorize google calendar events from multiple communities

###Steps

1.  Register for Google Developers Console and ontain an API key for your application. [Follow these steps](https://developers.google.com/google-apps/calendar/quickstart/python).

2.  Download the client_secret file to application directory and rename it as ***client_secret.json***

3.  In step 1, we have set Redirect URI to [https://localhost](https://localhost). The URI states where should the Google redirect the resource to complete authetication(good explanation can be found [here](http://architecture-soa-bpm-eai.blogspot.com/2012/08/oauth-20-for-my-ninth-grader.html)). If you have [node](https://nodejs.org/) installed, you can start local web-server using following command 
		```
		http-server
		```

4.  Update ***categories.json*** with appropriate data based on calendar IDs shared with you before running the code. Updates can be performed using ***Calendar.py***

5.  Execute ***ShareCalendar.py*** which will redirect you to webpage requesting authorization of your app. On confirmation, credentials for all future request will be stored at location ***./.credentials/***

6.  ***Calendar.py*** also enables to search based on particular category, calendarID, search query, time frames, number of results, etc. By supplying appropriate paramters, required results can be fetched.


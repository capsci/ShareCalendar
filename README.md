# ShareCalendar
Categorize google calendar events from multiple communities

###Steps

1.  Register for Google Developers Console and ontain an API key for your application. [Follow these steps](https://developers.google.com/google-apps/calendar/quickstart/python).

2.  Download the client_secret file to application directory and rename it as ***client_secret.json***

3.  In step 1, we have set Redirect URI to ***localhost***. The URI states where should the Google redirect the resource to complete authetication(good explanation can be found [here](http://architecture-soa-bpm-eai.blogspot.com/2012/08/oauth-20-for-my-ninth-grader.html)). If you have ***node*** installed, you can start local web-server using following command
```javascript
http-server
```

4.  Execute ***ShareCalendar.py*** which will redirect you to webpage requesting authorization of your app. On confirmation, credentials for all future request will be stored at location ***./.credentials/***
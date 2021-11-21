# Medico
A web service to remind you to take your medicine with a phone call!

## About

This is a simple web app that can help schedule phone calls to remind you to take a particular medicine. You input your phone number and timings and it will call you and a robotic voice will remind you to take it on time.
This is done using the Twilio phone call API and Cronjobs.

## Why?

The usecase is for elders who might not own smartphones so they cannot use the regular apps. A descendant can visit our website and schedule the medicine for them without the elder having to fiddle with technology.



## Installation Process
	
	-> Install Python 3.9 
	
	$ pip install -r requirements.txt
	optional: $ python manage.py createsuperuser
	$ python manage.py migrate
	$ python manage.py runserver
	
	-> open localhost:8000 on browser

## Screenshots


![alt text](https://github.com/A-S-A-P/Medico/blob/master/medico/Project%20Images/main.png?raw=true)



![alt text](https://github.com/A-S-A-P/Medico/blob/master/medico/Project%20Images/Screenshot_2.png?raw=true)



	Note: Twilio key is invalid so project will not work unless you replace it with your own.

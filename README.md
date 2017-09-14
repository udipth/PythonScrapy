# PythonScrapy
Scrapy framework to fetch data from website using Python

Prerequisites
=================================
1.Scrapy should be installed. 
Install Scrapy:
	pip install Scrapy
2.Install Dropbox module:
	pip install dropbox
3.Create a Dropbox App
	Create an app under your own dropbox account in the "App Console". (https://www.dropbox.com/developers/apps)
	Click the "generate access token" button and get access_token and paste it in the python codefile named ctrip.py.
	
How to Run the Code
======================
After pasting the Access Token in the source code, run the python code:
 	python ctrip.py
Alternatively, you can also run it in IDLE (Run module/ F5).
It will fetch the data from all pages of website using Scrapy, save the file as csv in the current directory and upload the file to dropbox automatically.

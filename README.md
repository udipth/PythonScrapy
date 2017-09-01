# PythonScrapy
Scrapy framework to fetch data from website using Python

Steps to Fetch Data From Website
=================================
1. Install Scrapy:
	pip install Scrapy
2. Start a Scrapy project using the code:
	scrapy startproject ctrip
3. Copy the python file myspider.py to ctrip/spiders folder
4. From the project's top level directory, run the spider and save it to a csv file named ctrip_data:
	scrapy crawl ctrip -o ctrip_data.csv

Steps to Upload the Data to Dropbox
====================================
1. Install Dropbox module:
	pip install dropbox
2. Create an app under your own dropbox account in the "App Console". (https://www.dropbox.com/developers/apps)
3. Click the "generate access token" button and get access_token and paste it in the python code named dropbox_code.py.
4. Run dropbox_code.py.

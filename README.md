# PythonScrapy
Scrapy framework to fetch data from website using Python

Steps
1. Install Scrapy
2. Start a Scrapy project using the code:
	scrapy startproject ctrip
3. Copy the python file myspider.py to ctrip/spiders folder
4. From the project's top level directory, run the spider and save it to a csv file named ctrip_list:
	scrapy crawl ctrip -o ctrip_list.csv

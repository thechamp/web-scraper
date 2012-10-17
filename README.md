web-scraper
===========

This scrapes two big e-commerce websites for particular brand of laptops.

Description
===========

I started with web links of Dell laptops on Flipkart and Snapdeal. With the help of BeautifulSoup, parsed the pages to find links of all the laptops on the page. Further parsed each page to find Processor, RAM, OS, Hard Disk, Screen of each laptop and saved in MySQL database. With the help of a very basic HTML interface, user can retrieve laptops matching his choice of configuration.

Installation
============

Run following command to populate database
	python3 scraper.py install
	
Known Issue
====

Link: http://www.snapdeal.com/product/dell-inspiron-15r-laptop-2nd/425942?pos=16;26 has two totally different type of description of same product on same page. Above it says it is a Ci5/Win7/1TB laptop, while scrolling down to technical specification section it says it is Ci3/Linux/320GB laptop. I have used technical specification for each laptop.

Note
====

Currently password of MySQL database is assumed to be 'pwd' in this application.
If your password is different, change in scraper.py and connections.php both
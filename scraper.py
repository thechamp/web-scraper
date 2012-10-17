## Author : Abhay
## Language : Python 3.2
## Description : Basic web scraper which scrapes all Dell laptops
##  from Flipkart and Snapdeal and stores them in MySQL database.

import pymysql
import urllib.request

from bs4 import BeautifulSoup
from bs4 import NavigableString


def generate_soup(url):
    """ Function takes as input a web url, opens it
        convert it into HTML format and beautifies
        using BeautifulSoup libraries """
    
    socket = urllib.request.urlopen(url)
    html_page = socket.read()
    return BeautifulSoup(html_page)

def get_info(tags, info):
    """ The function takes as an input the HTML tags of
        a web page source, retrieves their values from them and
        appends them to info and fnally returns info """
    
    for tag in tags:
        if tag.__class__ == NavigableString:
            if tag != '\n':
                info.append(tag)
        else:
            get_info(tag, info)
    return info


def format_processor(Processor):
    """ This is a helper function which takes as input the processor
        of laptop, and formats it uniformly in a unique fashion before
        saving into database """
    
    i = Processor.find('Generation') - 4
    Generation = '(' + Processor[i] + Processor[i+1] + Processor[i+2] + ' Generation)'
    if Processor.find('i3') >= 0:
        return 'Core i3 ' + Generation
    elif Processor.find('i5') >= 0:
        return 'Core i5 ' + Generation
    elif Processor.find('i7') >= 0:
        return 'Core i7 ' + Generation
    else:
        return Processor

def format_os(OS):
    """ This is a helper function which takes as input the Operating system
        of laptop, and formats it uniformly in a unique fashion before
        saving into database """
    
    if OS.find('Linux') >= 0 or OS.find('Ubuntu') >= 0 or OS.find('Free DOS') >= 0:
        # If Operating system is Linux/Ubuntu/Free Dos, consider it DOS
        return 'DOS'
    elif OS.find('Home Basic') >=0:
        return 'Windows 7 Home Basic'
    elif OS.find('Home Premium') >= 0:
        return 'Windows 7 Home Premium'
    else:
        # Remove all unnecessary whitespaces from the OS
        return ' '.join(OS.split())

def format_and_store_info(info, Seller):
    """ This function retrieves all required information of a laptop
        from info and Seller, formats them properly in uniform format
        and stores in MySQL table """
    
    # Web url of this laptop
    Link = info[0]

    # On web pages, 'RAM' and 'System Memory' are used interchangeably
    try:
        Memory = info[info.index('System Memory')+1].split()[0]
    except ValueError:
        Memory = info[info.index('RAM')+1].split()[0]

    # On web pages, 'HDD Capacity' and 'Hard Disk Capacity' are used interchangeably
    try:
        HDD = info[info.index('HDD Capacity')+1].split()[0]
    except ValueError:
        HDD = info[info.index('Hard Disk Capacity')+1].split()[0]
    
    OS = info[info.index('Operating System')+1]
    OS = format_os(OS)
    
    Screen = ' '.join(info[info.index('Screen Size')+1].split())
    Price = ' '.join(info[info.index('Rs.')+2].split())

    # On web pages, 'Processor' and 'Processor Name' are used interchangeably
    try:
        ProcessorIndex = info.index('Processor')
    except ValueError:
        ProcessorIndex = info.index('Processor Name')

    if info[ProcessorIndex+1] == 'Processor':
        Processor = info[ProcessorIndex+2]
    else:
        Processor = info[ProcessorIndex+1]
    Processor = format_processor(Processor)

    # Save entire information in MySQL
    Query = """INSERT INTO laptop_database (Processor, Memory, HDD, OS, Screen, Price, Seller, Link) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"""
    cursor.execute(Query % (Processor, Memory, HDD, OS, Screen, Price, Seller, Link))
    connection.commit()
    

## Connect to MySQL database and get cursor
connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='pwd', db='mysql')
cursor = connection.cursor()

## Extract all Dell Laptops on Flipkart
flipkart_url = 'http://www.flipkart.com/computers/laptops/dell'
laptop_soup = generate_soup(flipkart_url)
laptop_divs = laptop_soup.findAll("div", {"class" : "fk-product-thumb fkp-medium"})

for laptop in laptop_divs:
    laptop_link = "http://www.flipkart.com" + laptop.a['href']
    link_soup = generate_soup(laptop_link)
    info = get_info(link_soup.findAll(["th", {"class" : "specs-key"}, "td", {"class" : "specs-value"}, "span", {"id" : "fk-mprod-our-id"}]), [laptop_link])
    format_and_store_info(info, 'flipkart')


## Extract all Dell Laptops on Snapdeal
snapdeal_url = 'http://www.snapdeal.com/products/computers-laptops/?q=Brand%3ADell&FID=Brand%20%3A%20Dell'
laptop_soup = generate_soup(snapdeal_url)
laptop_divs = laptop_soup.findAll("div", {"class" : "product_listing_cont"})

for laptop in laptop_divs:
    laptop_link = laptop.a['href']
    link_soup = generate_soup(laptop_link)
    initial_info = [laptop_link, 'Rs.', ' ']
    spans = link_soup('span')
    for s in spans:
        if s.get('id') == 'selling-price-id':
            initial_info.append(s.get_text())
            break
    info = get_info(link_soup.findAll(["td"]), initial_info)
    format_and_store_info(info, 'snapdeal')

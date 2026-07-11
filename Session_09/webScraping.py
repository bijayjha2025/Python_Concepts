'''
Web Scraping: It is a technique used to extract data from websites. It involves making HTTP requests to a website, retrieving the HTML content, and then parsing the HTML to extract the desired information. Web scraping can be done using various programming languages and libraries, such as Python with BeautifulSoup or Scrapy.

To start web scraping, we need to have a basic understanding of HTML and CSS, as well as how to navigate the structure of a webpage. We can use tools like browser developer tools to inspect the elements of a webpage and identify the data we want to scrape. We need requests, BeautifulSoup, and a website to scrape. We can use the requests library to make HTTP requests to a website and retrieve the HTML content. Then, we can use BeautifulSoup to parse the HTML and extract the desired information.


'''
import requests #requests is a library that allows us to send HTTP requests using Python. It provides a simple way to interact with web services and APIs, making it easy to retrieve data from websites and other online sources.
from bs4 import BeautifulSoup #bs4 is a library that allows us to parse HTML and XML documents. It provides a simple way to navigate and search the parse tree, making it easy to extract the data we need.


url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

response = requests.get(url) #The requests.get() function is used to send a GET request to the specified URL. It retrieves the content of the webpage and returns a response object that contains the server's response to the request.
status = response.status_code #The status_code attribute of the response object contains the HTTP status code returned by the server. A status code of 200 indicates that the request was successful and the server returned the requested content.
print(f"Status code: {status}") #output: 403 means forbidden, 404 means not found, 500 means internal server error, 200 means OK


#Using BeautifulSoup to parse the HTML content of the webpage
soup = BeautifulSoup(response.content, 'html.parser') #The BeautifulSoup constructor takes the HTML content of the webpage and a parser as arguments. In this case, we are using the 'html.parser' parser to parse the HTML content.
print(soup.prettify()) #The prettify() method of the BeautifulSoup object returns a nicely formatted string representation of the parse tree. It adds indentation and line breaks to make the HTML more readable.
print(soup.title) #The title attribute of the BeautifulSoup object returns the title tag of the HTML document. It contains the text within the <title> tag, which is typically displayed in the browser's title bar or tab.
print(soup.get_text()) #The get_text() method of the BeautifulSoup object returns all the text content of the HTML document, with all the HTML tags removed. It is a convenient way to extract the text content of a webpage without having to navigate the parse tree.

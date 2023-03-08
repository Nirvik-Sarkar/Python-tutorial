"""What is HTTP?
HTTP stands for the 'Hypertext Transfer Protocol,'. It is a set of protocols that are designed 
to enable communication between clients and servers. Between clients and servers, it works as a 
request-response protocol. To request a response from the server, we can request data from the 
server or submit data to be processed to the server.

What Is Requests Module?
The response data depends on our type of request. The requests module is not a built-in Python
 module; instead, we have to download it manually. Requests module is used to send all kinds of 
 HTTP requests. It is also one of the most downloaded modules in Python because all the web-related 
software and programs must have it in them."""

"""get():
From the name, we can detect that the get function returns us some information about the site 
we requested. All the information is stored in the object we used to send the request. We can
access different kinds of information through it, such as status, header, cookies, etc. To 
make a GET request, invoke"""
import requests
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)

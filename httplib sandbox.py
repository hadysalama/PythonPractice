import http.client

print()
print()

connection: object = http.client.HTTPSConnection("www.python.org")
connection.request("GET", "/")
r1 = connection.getresponse()
print(r1.status, r1.reason)

data1 = r1.read()
connection.request("GET", "/")
r2 = connection.getresponse()
print(r2.status, r2.reason)
data2 = r2.read()
connection.close()
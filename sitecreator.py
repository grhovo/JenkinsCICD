def add_function(a,b):
	return a+b
def min_function(a,b):
	return a-b


a = 5
b = 3
myhtmlcode = "<h1>This is site header </h1>"

myhtmlcode = myhtmlcode + "<p> The sum of " + str(a) + " and " + str(b) + " equals " + str(add_function(a,b)) + "</p>"
myhtmlcode = myhtmlcode + "<p> The sub of " + str(a) + " and " + str(b) + " equals " + str(min_function(a,b)) + "</p>"


with open('index.html', 'w') as file:
	file.write(myhtmlcode)

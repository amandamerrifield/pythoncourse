# the built-in open function is used to read and write files 
# this function is good for csv or excel but there are better tools available for the purposes of .json or xml or xmlx 
# the open function requires a filename/path at a min
# the default behavior is to assume you want to read the file
# open() creates a text.io data type which has its own set of methods that you can see thanks to dot notation
# passenger_file. will bring up a list of methods. 
# read will bring up the whole file. Don't use that lol 
# readline will bring up one line so will require a loop and is a lot of effort
# readlines will bring up the file into a list of strings which isn't bad to start (one string/line of the file)
#-- this is okay for small to medium files but not a big file

passenger_file = open("passengers.csv")

# don't forget you've got to assign it to a variable so you can  use it later
lines = passenger_file.readlines()
# we're going to write to the london-passengers file with w. "w" will always overwrite anything that doesn't exist
london_passengers_file = open("london-passengers.csv", "w")

for line in lines:
    if "LHR" in line or "LGW" in line:
        #print(line)
        london_passengers_file.writelines(line)
passenger_file.close()
# ---

#TODO 
# contain first name initial, last name in upper case, email 
# ONLY passengers going through London
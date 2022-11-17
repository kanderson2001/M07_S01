#initialise results list
results = [] 

#initalise target - what information searching for?
target = ""

# Initialise file
f = open("FILENAME.txt", "r")

#Read in information from file
for x in f:
  results.append(x.replace("\n", ""))
  #Can print contents of what is being read in if wanted
  #print(x)

#close file
f.close()

#Linear search algorithm - To Complete


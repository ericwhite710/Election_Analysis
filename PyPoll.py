#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#5. The winner of the election based on popular vote.

#import datetime as dt
#now = dt.datetime.now()
#print("the time right now is", now)

#to do: perform analysis
#    print(election_data)

#to close th file
#election_data.close()

#using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

#use the open stment to open the file as a text file
#with open(file_to_save, "w") as txt_file:

#write some data to the file
    #txt_file.write("Counties in the Election\n______________________\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")


#close the file
#txt_file.close()

#add our dependencies
import csv
from email import header
import os

#assign a variable for the file to load and thee path
#with open("election_results.csv", "r") as election_data:
file_to_load = os.path.join("Resources", "election_results.csv")

#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:

#to do: read and analyze the data here
    file_reader = csv.reader(election_data)

#print each row in the csv file
#    for row in file_reader:
#        print (row)

#print the header row
    headers = next(file_reader)
    print(headers)






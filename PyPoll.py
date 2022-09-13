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
import os

#assign a variable for the file to load and thee path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable for the file to save to the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0
#candidate options
candidate_options = []
#candidate votes dictionary
candidate_votes = {}


#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)

    #print each row in the csv file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        
        #add the candidate name to the candidate list
        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #2. track candidate vote count
            candidate_votes[candidate_name] = 0
        #add a vote to candidate count
        candidate_votes[candidate_name] += 1

#print the candidate vote dictionary
print (candidate_votes)







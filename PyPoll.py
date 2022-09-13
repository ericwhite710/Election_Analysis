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
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
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

#save the results to our text file
with open(file_to_save,"w") as txt_file:
    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        print(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    
    #print winning candidate results to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #save the winning candidate results to the text file
    txt_file.write(winning_candidate_summary)




#Dependencies
import os
import csv

#Path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_results.txt")

#Dictionary
county_name = ()
county_summary = ()
county_options = []
county_votes = {}
total_count = 0
total_votes = 0
max_votes = 0
max_county_name =""
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
CANDIDATE_COL = 2
COUNTY_COL = 1

#county and candidate
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        total_count += 1
        county_name = row[COUNTY_COL]
        if county_name not in county_votes:
            county_votes[county_name] = 0
        county_votes[county_name] += 1
        if max_votes < county_votes[county_name]:
            max_votes = county_votes[county_name]
            max_county_name = county_name
    for county_name in county_votes:
        percent = county_votes[county_name]/ total_count*100
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        total_votes += 1
        candidate_name = row[CANDIDATE_COL]
        county_name = row[CANDIDATE_COL]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"Largest County Turnout: {max_county_name, max_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    for county_name in county_votes:
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (f"{county_name}:{vote_percentage:.1f}%({votes:,})\n")
        print(county_results)
        txt_file.write(county_results),
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}:{vote_percentage:.1f}%")
        if votes > winning_count:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
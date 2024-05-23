import os
import csv

#Path to collect data from the resources folder
election_csv = 'PyPoll/resources/election_data.csv'

#Set variables
Total_Cast_Votes = []
List_Candidates = []
total_votes = {}
Percentage_of_Votes = []

#Read in the CSV file
with open(election_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Read the header row first & skip it
    csv_header = next(csv_reader)

    #Read each row of data after the header
    for row in (csv_reader):
        
        #Add values in Ballot ID (row [0]) & candidate (row[2]) columns to corresponding variable lists  
        Total_Cast_Votes.append(row[0])
        List_Candidates.append(row[2])

    #Iterate thru list to aggregate # of votes per candidate    
    for Candidate in List_Candidates:
         if Candidate in total_votes:
            total_votes[Candidate] += 1
         else:
            total_votes[Candidate] = 1
        
    # % of votes for each candidate 
    Percentage_of_Votes_C = "{:.3f}".format(float(total_votes["Charles Casper Stockham"]) / float(len(Total_Cast_Votes)) * 100)
    Percentage_of_Votes_D = "{:.3f}".format(float(total_votes["Diana DeGette"]) / float(len(Total_Cast_Votes)) * 100)
    Percentage_of_Votes_R = "{:.3f}".format(float(total_votes["Raymon Anthony Doane"]) / float(len(Total_Cast_Votes)) * 100)

    #Calculate max & min # of votes to list winner & loser 
    max_key = max(total_votes, key=lambda k: total_votes[k])
    max_value = total_votes[max_key]
    min_key = min(total_votes, key=lambda k: total_votes[k] )
    min_value = total_votes[min_key]

#Print all results 
print("Election Results")
print("________________________")
print(f'Total Votes:  {str(len(Total_Cast_Votes))}')
print("________________________")
print(f'{(List_Candidates[0])}: {Percentage_of_Votes_C}% ({total_votes["Charles Casper Stockham"]})')
print(f'{max_key}: {Percentage_of_Votes_D}% ({total_votes["Diana DeGette"]})')
print(f'{min_key}: {Percentage_of_Votes_R}% ({total_votes["Raymon Anthony Doane"]})')
print("________________________")
print(f'Winner: {max_key}')
print("________________________")

#Set variable for output file
output_file = os.path.join("PyPoll/analysis/election_data_final.csv")

#Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the first row (header)
    writer.writerow(['Election Results'])
    # Write the remaining rows
    writer.writerow(['________________________'])
    writer.writerow([f'Total Votes: {str(len(Total_Cast_Votes))}'])
    writer.writerow(['________________________'])
    writer.writerow([f'{(List_Candidates[0])}: {Percentage_of_Votes_C}% ({total_votes["Charles Casper Stockham"]})'])
    writer.writerow([f'{max_key}: {Percentage_of_Votes_D}% ({total_votes["Diana DeGette"]})'])
    writer.writerow([f'{min_key}: {Percentage_of_Votes_R}% ({total_votes["Raymon Anthony Doane"]})'])
    writer.writerow(['________________________'])
    writer.writerow([f'Winner: {max_key}'])
    writer.writerow(['________________________'])
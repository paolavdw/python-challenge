import os
import csv

#Path to collect data from the Resources folder
budget_csv = 'PyBank/Resources/budget_data.csv'

#Set variables 
total_months = []
Changes_P_L = []
changes = 0 
P_L = []

#Read in the CSV file 
with open(budget_csv, 'r') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #read the header row first & skip it
    csv_header = next(csv_reader)

    #read each row of data after the header 
    for row in (csv_reader):
        
        #add values in "date" column [row 0] to total_months variable list to then calculate the lenght of the list  
        total_months.append(row[0])
        #add values in "profit/losses" column [row 1] to P_L variable list to then sum of all values 
        P_L.append(int(row[1]))

    #Adding the differences between profit months to Changes_P_L variable list to then do an average
    for x in range(len(P_L) - 1):
        changes = P_L[x+1] - P_L[x]
        Changes_P_L.append(int(changes))
    
    #Calculation to get max & min amounts in profits
    Greatest_Increase = max(Changes_P_L)
    Greatest_Decrease = min(Changes_P_L)

    #Average of changes over the entire period of "profit/losses"     
    Changes_P_L = sum(Changes_P_L) / len(Changes_P_L)
 
 
    #Print out text "Financial Analysis"
    print("Financial Analysis")
    print("____________________________")

    #Print total # of months & total profits
    print("Total Months: " + str(len(total_months))) 
    print("Total: " + "$" + str(sum(P_L)))

    #Print results of average change, greatest increase & decrease in profits 
    print(f'Average change: ${Changes_P_L: .2f}')    
    print(f'Greatest Increase in Profits: {str(list(total_months)[79])} (${Greatest_Increase})')
    print(f'Greatest Decrease in Profits: {str(list(total_months)[49])} (${Greatest_Decrease})')


#Set variable for output file
output_file = os.path.join("PyBank/analysis/budget_data_final.csv")

#Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the first row (header)
    writer.writerow(['Financial Analysis'])
    # Write the remaining rows
    writer.writerow(['_____________________'])
    writer.writerow([f'Total Months: {str(len(total_months))}'])
    writer.writerow([f'Total: ${str(sum(P_L))}'])
    writer.writerow([f'Average change: ${Changes_P_L: .2f}'])
    writer.writerow([f'Greatest Increase in Profits: {str(list(total_months)[79])} (${Greatest_Increase})'])
    writer.writerow([f'Greatest Decrease in Profits: {str(list(total_months)[49])} (${Greatest_Decrease})'])


 




 
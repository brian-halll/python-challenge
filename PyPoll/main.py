#import modules
import os 
import csv

# create path for csv
resource_csv = os.path.join("Resources", "election_data.csv")

totalVotes = 0
StockhamVotes = 0
DegetteVotes = 0
DoaneVotes = 0
winnerVotes = 0
winner = ""

with open(resource_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # grab header
    header = next(csv_reader)

    

    for row in csv_reader:
        totalVotes = totalVotes + 1

        if row[2] == "Charles Casper Stockham":
            StockhamVotes += 1

        elif row[2] == "Diana DeGette":
            DegetteVotes += 1


        elif row[2] == "Raymon Anthony Doane" :
            DoaneVotes += 1

        
    if StockhamVotes > DegetteVotes and StockhamVotes > DoaneVotes :
        winner = "Charles Casper Stockham"
    elif DegetteVotes > DoaneVotes :
        winner = "Diana DeGette"
    else:
         winner = "Raymon Anthony Doane"    

        
output_path = os.path.join("analysis", "results.csv")


with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow([f'\n\tElection Results \n\n \t-------------------- \n'])

    csvwriter.writerow([f'\tTotal Votes : {totalVotes: ,}\n\n \t-------------------- \n'])

    csvwriter.writerow([f'\tCharles Casper Stockham : {(StockhamVotes/totalVotes) * 100 : .2f}% ({StockhamVotes:,})\n'])

    csvwriter.writerow([f'\tDiana DeGette : {(DegetteVotes/totalVotes) * 100: .2f}% ({DegetteVotes:,})\n'])

    csvwriter.writerow([f'\tRaymon Anthony Doane : {(DoaneVotes/totalVotes) * 100 : .2f}% ({DoaneVotes:,})\n\n \t-------------------- \n'])

    csvwriter.writerow([f'\tWinner : {winner}\n\n \t-------------------- \n'])            


    


print(f"\n\tElection Results \n\n \t-------------------- \n")
print(f"\tTotal Votes : {totalVotes : ,}\n\n \t-------------------- \n")
print(f"\tCharles Casper Stockham : {(StockhamVotes/totalVotes) * 100 : .2f}% ({StockhamVotes :,})\n")
print(f"\tDiana DeGette : {(DegetteVotes/totalVotes) * 100 : .2f}% ({DegetteVotes : ,})\n")
print(f"\tRaymon Anthony Doane : {(DoaneVotes/totalVotes) * 100 :.2f}% ({DoaneVotes : ,})\n\n \t-------------------- \n")

print(f"\tWinner : {winner}\n\n \t-------------------- \n")








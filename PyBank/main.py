#import modules
import os 
import csv

# create path for csv
resource_csv = os.path.join("Resources", "budget_data.csv")

totalMonths = 0
netTotal = 0
avgChange = 0.00
netChange = 0.00
lastProfit = 0
greatestIncrease = 0
dateI = ""
greatestDecrease = 0
dateD = ""
change = 0


with open(resource_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # grab header
    header = next(csv_reader)

    # iterates through every line of csv (indexes of rows are columns)
    for row in csv_reader:
        # increment total months every row
        totalMonths = totalMonths + 1

        # running sum of profit/loss column
        netTotal = netTotal + int(row[1])

        #calculate differences in current profit/loss from previous
        if netChange == 0.00 :
            netChange = int(row[1])
        else:
            change = (int(row[1]) - lastProfit)
             # running sum of differences in profit/loss to calculate average
            netChange = netChange + change



        if change > greatestIncrease :
            greatestIncrease = change
            dateI = row[0]
        elif change < greatestDecrease :
            greatestDecrease = change
            dateD = row[0]

       
       
        # keep track of profit/loss for calculating difference in next iteration
        lastProfit = int(row[1])
        
output_path = os.path.join("analysis", "results.csv")


with open(output_path, 'w') as csvfile:
     
     # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow([f'\tTotal Months : {totalMonths} \n \tTotal : ${netTotal} \n \tNet Change : {netChange} \n \tAverage Change : {netChange / totalMonths}'])

    csvwriter.writerow([f'\tGreatest Increase in Profits : {dateI} ${greatestIncrease}\n \tGreatest Decrease in Profits : {dateD} ${greatestDecrease}\n'])

print(f"\tTotal Months : {totalMonths} \n \tTotal : ${netTotal} \n \tNet Change : {netChange} \n \tAverage Change : {netChange / totalMonths}")
print(f"\tGreatest Increase in Profits : {dateI} ${greatestIncrease}\n \tGreatest Decrease in Profits : {dateD} ${greatestDecrease}\n") 






import csv
import os

budgetdata_csv = os.path.join("budget_data.csv")

TotalMonths = 0
Total = 0
Change = []
Dates = []
Profits =[]
Value = 0

with open(budgetdata_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)

    #AverageChange = []
    First_Row = next(csvreader)
    TotalMonths += 1
    Value = int(First_Row[1])
    Total += int(First_Row[1])

    GreatestIncrease = {"Date": First_Row[0],"Value": 0}


    for row in csvreader:
        TotalMonths += 1
        Total = Total + int(row[1])

    #for x in range (1, len(Profits)):
        #AverageChange.append((int(Profits[x] - int(Profits[x-1]))))

    #AverageChange = sum(AverageChange) / len(AverageChange)

    #GreatestIncrease = max(AverageChange)
    #GreatestDecrease = min(AverageChange)

        Change = int(row[1])-Value
        if len(Profits)> 0 :
            if Change > max(Profits):
                GreatestIncrease["Value"] = Change
                GreatestIncrease["Date"] = row[0]
            elif Change < min(Profits):
                pass
        Profits.append(Change)
        Value = int(row[1])   
 
    AverageChange = sum(Profits)/len(Profits)       

    GreatestIncreaseAmount = max(Profits)
    #GreatestDecreaseAmount = min(Profits)

    #GreatestIncreaseIndex = Profits.index(GreatestIncreaseAmount)
    #GreatestIncreaseDate = Dates[GreatestIncreaseIndex]
    #GreatestDecreaseDate = Profits.index(min(Profits))

    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Total : $ {str(Total)}")
    print(f"Average Change: $ {str(round(AverageChange,2))}")
    print(f"Greatest Increase in Profits: {GreatestIncrease['Date']} ({GreatestIncrease['Value']})")
#print(f"Greatest Decrease in Profits:  (${str(GreatestDecreaseAmount)})")

#Budget_Summary_File = os.path.join("Budget_Summary.csv")

#with open(Budget_Summary_File, "w") as file:
    #file.write("Financial Analysis")
    #file.write("\n")
    #file.write("-----------------------------------")
    #file.write("\n")
    #file.write(f"Total Months: {str(TotalMonths)}")
    #file.write("\n")
    #file.write(f"Total : $ {str(Total)}")
    #file.write("\n")
    #file.write(f"Average Change: $ {str(round(AverageChange,2))}")
    #file.write("\n")
    #file.write(f"Greatest Increase in Profits: {TotalMonths[GreatestIncreaseDate]} (${str(GreatestIncreaseAmount)})")   
    #file.write("\n")
    #file.write(f"Greatest Decrease in Profits: {TotalMonths[GreatestDecreaseDate]} (${str(GreatestDecreaseAmount)})")

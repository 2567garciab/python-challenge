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
    GreatestDecrease = {"Date": First_Row[0],"Value": 0}

    for row in csvreader:
        TotalMonths += 1
        Total = Total + int(row[1])

        Change = int(row[1])-Value
        if len(Profits)> 0 :
            if Change > max(Profits):
                GreatestIncrease["Value"] = Change
                GreatestIncrease["Date"] = row[0]
            elif Change < min(Profits):
                GreatestDecrease["Value"] = Change
                GreatestDecrease["Date"] = row[0]
        Profits.append(Change)
        Value = int(row[1])   
 
    AverageChange = sum(Profits)/len(Profits)       

    GreatestIncreaseAmount = max(Profits)
    GreatestDecreaseAmount = min(Profits)

    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {TotalMonths}")
    print(f"Total : $ {str(Total)}")
    print(f"Average Change: $ {str(round(AverageChange,2))}")
    print(f"Greatest Increase in Profits: {GreatestIncrease['Date']} ({GreatestIncrease['Value']})")
    print(f"Greatest Decrease in Profits: {GreatestDecrease['Date']} ({GreatestDecrease['Value']})")

Budget_Summary_File = os.path.join("Budget_Summary.csv")

with open(Budget_Summary_File, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-----------------------------------")
    file.write("\n")
    file.write(f"Total Months: {str(TotalMonths)}")
    file.write("\n")
    file.write(f"Total : $ {str(Total)}")
    file.write("\n")
    file.write(f"Average Change: $ {str(round(AverageChange,2))}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {GreatestIncrease['Date']} ({GreatestIncrease['Value']})")   
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {GreatestDecrease['Date']} ({GreatestDecrease['Value']})")

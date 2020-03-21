import csv
import os

election_data_csv = os.path.join("election_data.csv")

TotalVotes = 0
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OtooleyVotes = 0

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvfile)
    for row in csvreader:
        TotalVotes += 1

        if row[2] == "Khan":
             KhanVotes +=1
        elif row[2] =="Correy":
            CorreyVotes += 1
        elif row[2] =="Li":
            LiVotes += 1
        elif row[2] =="O'Tooley":
            OtooleyVotes += 1    

KhanVotes_Percent = (KhanVotes/TotalVotes)*100
CorreyVotes_Percent = (CorreyVotes/TotalVotes)*100
LiVotes_Percent = (LiVotes/TotalVotes)*100
OtooleyVotes_Percent = (LiVotes/TotalVotes)*100

Canidates = ["Khan","Correy", "Li", "O'Tooley"]
Votes = [KhanVotes, CorreyVotes, LiVotes, OtooleyVotes]

Dictionary_of_Canidates_and_Votes = dict(zip(Canidates,Votes))
key = max(Dictionary_of_Canidates_and_Votes, key=Dictionary_of_Canidates_and_Votes.get)

print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {TotalVotes}")
print("-----------------------------------")
print(f"Khan : {KhanVotes_Percent:.3F} % ({KhanVotes})")
print(f"Correy : {CorreyVotes_Percent:.3F} % ({CorreyVotes})")
print(f"Li : {LiVotes_Percent:.3F} % ({LiVotes})")
print(f"O'Tooley : {OtooleyVotes_Percent:.3F} % ({OtooleyVotes})")
print("-----------------------------------")
print(f"Winner: {key}")
print("-----------------------------------")

Election_File = os.path.join("Election_Results.csv")

with open(Election_File, "w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("-----------------------------------")
    file.write("\n")
    file.write(f"Total Votes: {TotalVotes}")
    file.write("\n")
    file.write("-----------------------------------")
    file.write("\n")
    file.write(f"Khan : {KhanVotes_Percent:.3F} % ({KhanVotes})")
    file.write("\n")
    file.write(f"Correy : {CorreyVotes_Percent:.3F} % ({CorreyVotes})")  
    file.write("\n")
    file.write(f"Li : {LiVotes_Percent:.3F} % ({LiVotes})")
    file.write("\n")
    file.write(f"O'Tooley : {OtooleyVotes_Percent:.3F} % ({OtooleyVotes})")
    file.write("\n")
    file.write("-----------------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write("-----------------------------------")


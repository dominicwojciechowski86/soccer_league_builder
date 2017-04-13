import csv

# this function groups players by experience
def experience_sorter(r):

    for row in r:
        if row["Soccer Experience"] == "YES":
            played_before.append(row)

        else:
            not_played_before.append(row)

# this function first assigns the experienced players to a group and then assigns the non-experienced players
def team_selector(a):
    x=0
    for group in a:

        for row in group:
            if  x == len(team_names):
                x=0
            team_names_dict[team_names[x]].append(row)
            x+=1

# this function writes the roster.
def roster_writer(dictionary):
    file = open("teams.txt", "w")

    for team in dictionary:
        file.write(team+"\n"+"\n")
        for row in dictionary[team]:
            file.write(row["Name"]+" "+row["Soccer Experience"]+" "+ row["Guardian Name(s)"]+"\n")
        file.write("\n")

# guess what this letter_writer function does.
def letter_writer(dictionary):
    for team in dictionary:
        for row in dictionary[team]:
            a = (row["Name"].replace(" ","_")+".txt").lower()
            letter=open(a,"w")
            letter.write("Dear " + row["Guardian Name(s)"]+", \n \nYour child, "+row["Name"]+", has been selected to play in the " + team +".\n\nThe first practice will be at 1pm on the 7/10/17 at the park.\n\nYours sincerely,\nDominic Wojciechowski")


if __name__=="__main__":

    with open("soccer_players.csv", newline="\n") as csvfile:
        soccer_list = csv.DictReader(csvfile, delimiter=",")
        rows_of_players = list(soccer_list)

        # create two blank lists for different level of player to be passed into then.
    played_before = []
    not_played_before = []

    experience_sorter(rows_of_players)

    all_players = [played_before, not_played_before]

    team_names = ["Sharks", "Dragons", "Raptors"]
    team_names_dict = {}
    for name in team_names:
        team_names_dict[name] = []

    team_selector(all_players)

    roster_writer(team_names_dict)

    letter_writer(team_names_dict)

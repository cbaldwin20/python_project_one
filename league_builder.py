import csv
import sys

  
#open up the soccer_players.csv and turn the info into a big list with lists inside
if __name__ == "__main__":
  sys.stdout = open('teams.txt', 'w')
  with open('soccer_players.csv', newline='') as csvfile: 
    artreader = csv.reader(csvfile, delimiter=',')
    rows = list(artreader)
    
  header = rows.pop(0) #seperating the keys ex: "Name" from the values ex: "John"
  
  for playerInfo in rows:
    del playerInfo[1] #deleting the height from the lists as we don't need it.
  
  experience = [] #a list of players with soccer experience
  noExperience = [] #a list of players with no soccer experience
  
  #putting the players into either the experience or noExperience lists
  for row in rows:
    if row[1] == "YES":
      experience.append(row)
    else:
      noExperience.append(row) 
  
  teamSharks = []
  teamDragons = []
  teamRaptors = []
  teams = [teamSharks, teamDragons, teamRaptors]
  teamName = ["Sharks", "Dragons", "Raptors"]
  
  #function combining 1/3 of the experienced/inexperienced into one of the three teams
  def sortingIfPlayed(ifPlayed):
    teamSharks.extend(ifPlayed[:int(len(ifPlayed)/3)])
    teamDragons.extend(ifPlayed[int(len(ifPlayed)/3):int(len(ifPlayed)/(3/2))])
    teamRaptors.extend(ifPlayed[int(len(ifPlayed)/(3/2)):])
    
  sortingIfPlayed(experience)
  sortingIfPlayed(noExperience)
   
  #a function to take a list of players info by team, turn it into a string, and print it out 
  def printTeam(team):
    for playerInfoList in team:
      playerInfoString = ", ".join(playerInfoList)
      
      print(playerInfoString)
    print("")
  
  x = 0
  for team in teams:
    print(teamName[x])  #prints the team's name above the list of players info
    x += 1
    printTeam(team) #calls the function to print the players info below the team name

  sys.stdout.close()

  #creates a letter for each player letting them know what team they're on
  x = -1
  for t in teams:
    x += 1
    for n in t:
      sys.stdout = open(n[0].replace(" ", "_") + '.txt', 'w')
      print("Dear " + n[2] + ",")
      print("Congratulations! " + n[0] + " is on team " + teamName[x] + ". The first practice will be on Saturday May 6th. See you there!" )
      sys.stdout.close()

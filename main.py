class FlightTable:
    def _init_(self):
        self.matches = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]

    def search_by_team(self, team_name):
        matches = [match for match in self.matches if team_name in (match["Team 01"], match["Team 02"])]
        return matches

    def search_by_location(self, location):
        matches = [match for match in self.matches if match["Location"] == location]
        return matches

    def search_by_timing(self, timing):
        matches = [match for match in self.matches if match["Timing"] == timing]
        return matches

def main():
  flight_table = FlightTable()

  while True:
        print("Search options:")
        print("1. List of all matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            team_name = input("Enter the team name: ")
            matches = flight_table.search_by_team(team_name)
        elif choice == "2":
            location = input("Enter the location: ")
            matches = flight_table.search_by_location(location)
        elif choice == "3":
            timing = input("Enter the timing: ")
            matches = flight_table.search_by_timing(timing)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            continue
        
        if matches:
            print("Match Details:")
            for match in matches:
                print(f"Location: {match['Location']}, Team 01: {match['Team 01']}, Team 02: {match['Team 02']}, Timing: {match['Timing']}")

        else:
            print("No matches found.")

if __name__ == "__main__":
    main()  
 


  


import time
import os
import random
from logging import DEBUG

from LinkedList import DLinkedList

def initialize_teams():
    """
    Initialize 32 unique teams with names and return them in a list.


    Example: ["Team A", "Team B", ..., "Team Z"]
    """

    # Initialize Empty DoubleLinked List for Teams from CSV file.
    teams = DLinkedList()

    # Load team data from teams.csv.
    with open('teams.csv') as file: # Open CSV file.
        lines = file.readlines()    # Read line by line from the file.

    for line in lines[1:]:  # Ignore the title for each column.
        parsedLine = line.strip()   # Remove spacing before and after each string.
        group, team, power = parsedLine.split(",")  # Parse data based on column it is found under.

        teams.insert(team.strip()) # Insert teams into their respective DoubleLinkedLists.

    return teams # Returns a list of teams.

# GROUP STAGE
# Divide 32 teams into 8 groups of 4 teams each.

# Each team plays a mathc against every other team in its groups.

# Points are awarded. Win = 3 points, Draw = 1 point and Loss = 0 points.

# After each match, update the linked list for each group.
# Teams are ranked by points, and the top 2 teams from each group advance.

def initialize_team_groups():
    '''
    Initialize DLinkedList groupings based off Group A through H found in CSV file.
    :return: groups (Dct) : A dictionary holding teams based on their respective groups.
    '''
    # Initialize Empty DoubleLinked List for Rankings based on Groupings from CSV file.
    groups = {}
    for group in "ABCDEFGH": # Create A DLinkedList for each group A through H.
        groups[group] = DLinkedList()

    # Load team data from teams.csv.
    with open('teams.csv') as file: # Open CSV file.
        lines = file.readlines()    # Read line by line from the file.

    for line in lines[1:]:  # Ignore the title for each column.
        parsedLine = line.strip()   # Remove spacing before and after each string.
        group, team, power = parsedLine.split(",")  # Parse data based on column it is found under.

        groups[group].insert(team.strip()) # Insert teams into their respective DoubleLinkedLists.

    return groups # Return a dictionary of teams based on groupings.


def group_stage_matches(groups, linked_lists):
    """
    Conduct the group stage matches where teams within each group play against each other.

    Each match should assign points to the teams and update their rankings in the linked list.
    """

    # Each Team plays a math against every other team in its group.
    # Options are Win, Draw, Loss.


    # Skeleton Code #
    # Group A
    #

    # Win = 3, Draw = 1, Loss = 0
    numbers = [3, 1, 0]

    random_number = random.choice(numbers) # Random Integer chosen from the list 3, 1, 0.

    print(random_number) # Testing



    # Update their respective scores.



#     TODO: Implement match results with random outcomes.
#     For each match, update the linked list to reflect the new rankings.
    pass


def promote_teams(groups, linked_lists):
    """
    Identify the top two teams from each group to move on to the knockout stage.

    Remove teams ranked 3rd and 4th in each group from the linked list.
    """


#   TODO: Implement logic to promote top teams and eliminate others.
    pass

# KNOCKOUT STAGE
# Conduct single-elimination rounds for the top 16 teams
# (winners from the group stage)

# Randomly pair teams for each knockout round in linked list, where each pair
# is put in the list.

# After each match, update the linked list by removing the losing team.

# Continue rounds until one team emerges as the champion.

def knockout_stage(teams, linked_list):
    """
    Conduct the knockout stage where teams are paired randomly.

    The losing team is removed from the linked list, and the winner moves on to the next round.
    """

#  TODO: Implement single-elimination logic until one team remains.

    pass

# Implement randomized match results to simulate real game outcomes.
# Track each team's wins, draws and losses. Store wins, losses, and draws directly.

def knockout_competition(teams):
    # Function to simulate knockout matches and find the champion with a fixed bracket structure
    # Define bracket for Round of 16 based on group winners and runners-up

    # Round of 16

    # Quarterfinals

    # Semifinals

    # Final

    #return champion
    pass


def main():
    """
    Run the World Cup simulation.

    This function should:
    1. Initialize the teams and groups.
    2. Conduct the group stage, updating rankings with each match.
    3. Promote teams and set up the knockout stage.
    4. Continue until a winner is determined.
    """
    # Initialize teams and linked list for rankings
    teams = initialize_teams()

    print("All Teams:", teams.display_rankings()) # Test to see if all teams were initialized into teams DLinkedList

    groupings = initialize_team_groups()
    print("Group A Teams:", groupings['A'].display_rankings()) # Testing to see if data has been loaded in.

    group_stage_matches(None, None)


    

    # TODO: Assign teams to groups and start group stage

    # TODO: Promote teams to knockout stage

    # Initialize new linked list for knockout stage

    # TODO: Run knockout stage and determine the winner


if __name__ == "__main__":
    main()


# Run the group stage matches.

# User Command: The users should be able to enter commands "S" to
# see group rankings, or "C" to continue.

# Run group and knockout stages sequentially by calling the appropriate functions.

# User Command: The users should be able to enter commands "S" or "C" again.
# This should print all the possible tables to give the user a complete picture
# of all the games.

# Display final tournament results, including the champion.
# (If the games include a rematch to determine the winner due an
# initial draw, format like: Croatia 1 - 1 Brazil (Croatia won 4-2
# on penalties).

# Output for group stage and knockout stage looks like the following.

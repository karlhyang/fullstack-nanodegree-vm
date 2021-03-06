#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM matches;")
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM players;")
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute(
        "SELECT COUNT(*) from players;")
    val = c.fetchone()[0]
    return val
    conn.close()


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)"""
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO players (name) values (%s);",(name,))
    conn.commit()
    conn.close() 
    """ Args:
      name: the player's full name (need not be unique).
    """


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie."""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT players.id, players.name, (select count(*) from matches where winner = players.id) as wins, (select count(*) from matches where winner = players.id or loser = players.id) as matches_played from players order by wins;")
    result = c.fetchall()
    return result
    conn.close() 
    """
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players."""
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO matches (winner,loser) values (%s, %s);",(winner,loser))
    conn.commit()
    conn.close()
    """
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings."""

    standings = playerStandings()
    thepairings = [] 
    y = 0
    while y < len(standings): #iterating until we have connected every pair
        pairing = []
        id1 = standings[0+y][0] # Pulling out the relevant information we want
        name1 = standings [0+y][1]
        id2 = standings[1+y][0]
        name2 = standings[1+y][1]
        pairing.append(id1) #we add to the tuple the info we want
        pairing.append(name1)
        pairing.append(id2)
        pairing.append(name2)
        thepairings.append(pairing) #
        y += 2 #iterating through pairs
    return thepairings





    """
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """



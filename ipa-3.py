'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    status_a = False
    status_b = False
    
    if to_member in social_graph[from_member]['following']:
        status_b = True
    if from_member in social_graph[to_member]['following']:
        status_a = True

        
    if (status_a == True) and (status_b == True):
        return(f'friends')
    elif (status_a == False) and (status_b == False):
        return(f'no relationship')
    elif (status_a == True) and (status_b == False):
        return(f'followed by')
    elif (status_a == False) and (status_b == True):
        return(f'follower')
    
    # end of code


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    s = len(board)
    empty_cells = 0 

    for i, r in enumerate(board):
        if len(set(r)) == 1 and r[0] != '':
            return r[0]
    
    for j, c in enumerate(range(s)):
        if board[0][c] != '' and len(set(r[c] for r in board)) == 1:
            return board[0][c]
        
    if len(set(board[z][s-1-z] for z in range(s))) == 1 and board[0][s-1] != '':
        return board[0][s-1]
    
    if len(set(board[z][z] for z in range(s))) == 1 and board[0][0] != '':
        return board[0][0]
    
    for r in board:
        empty_cells += r.count('')  
    
    if empty_cells == 0:
        return 'NO WINNER'  
    
    return 'NO WINNER'  
    # end of code #return comment: 'type bool has no len()'
    
    
def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    time_counter = 0
    list_items = list(route_map.items())

    for i, x in enumerate(list_items):
        if first_stop in x[0][0]:
            for j, y in enumerate(list_items):
                if second_stop in y[0][1]:
                    new_list = list_items[i:j+1]
                    for k in new_list:
                        time_counter += int(k[1]['travel_time_mins'])

    return (f'{time_counter}')
    # end of code

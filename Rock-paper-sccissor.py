import random

def player(prev_play, opponent_history=[]):
    # Add the opponent's previous move to the history
    if prev_play:
        opponent_history.append(prev_play)

    # Counter the opponent's most frequent move in their history
    if len(opponent_history) >= 2:
        # Simple frequency analysis
        most_common_move = max(set(opponent_history), key=opponent_history.count)

        # Choose the counter move
        if most_common_move == 'R':
            return 'P'
        elif most_common_move == 'P':
            return 'S'
        else:
            return 'R'
    else:
        # If there's not enough history, choose randomly
        return random.choice(['R', 'P', 'S'])


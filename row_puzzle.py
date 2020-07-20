# Author: Erika Tharp
# Date: 07/20/2020
# Description: This program contains a recursive function named row_puzzle that takes a list of non-negative integers as a parameter
#              and returns True if the puzzle is solvable for that row, but returns False otherwise.
#              A puzzle consisting of a row of squares that contain non-negative integers, with a zero in the rightmost square.
#              The user has a token that starts on the leftmost square.
#              On each turn, the token can shift left or right a number of squares equal to the value in its current square, but is not allowed to move off either end.


def row_puzzle(numbers, index=0):
    """
    Takes a list of non-negative integers as a parameter and returns True if the puzzle is solvable for that row, but returns False otherwise.
    """
    if index == len(numbers) - 1:
        return True
    elif index > len(numbers) - 1 or index < 0:
        return False
    # Check if we already have visited the value. If we have, returns False.
    elif numbers[index] == -1:
        return False
    else:
        # Store the current value in numbers[index] in temp.
        temp = numbers[index]
        # Set the current value to -1 so that we can keep track of values we have visited.
        numbers[index] = -1
        # Determine both moving the index to the right and left
        return row_puzzle(numbers, (index + temp)) or row_puzzle(numbers, (index - temp))

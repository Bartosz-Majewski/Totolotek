"""When you win the lottery"""
import random
from datetime import timedelta, date

"""Aby zobaczyć działanie bloku try zmniejsz zasięg liczb losowanych naprzykład do 20
   -> all_possible_numbers = range(1, 20)"""

COST_OF_SINGLE_DRAW = 3
all_possible_numbers = range(1, 50)
my_numbers = set(random.sample(all_possible_numbers, k=6))


def draw_numbers():
    """Draw 6 lotto numbers

    Returns:
        set: collection with 6 different totek numbers from range 1 to 49
    """
    return set(random.sample(all_possible_numbers, k=6))


def play_until_you_win(bet_numbers, drawing_numbers_algorithm):
    """Keep drawing nre numbers until you win

    Args:
        bet_numbers (set): user choice numbers
        drawing_numbers_algorithm (function): algorithm for drawing numbers

    Returns:
       counter (int): number of attempts to win
    """
    random_numbers = {}
    counter = 0
    points = 0
    three = 0
    four = 0
    five = 0

    while bet_numbers != random_numbers:
        random_numbers = drawing_numbers_algorithm()
        counter += 1
        for number in bet_numbers:
            if number in random_numbers:
                points += 1
        if points == 3:
            three += 1
        elif points == 4:
            four += 1
        elif points == 5:
            five += 1
        points = 0

    return counter, three, four, five


def count_a_date(total_cost):

    d_today = date.today()
    user_old = input('Kiedy się urodziłeś? YYYY-MM-DD ').split('-')
    year, month, day = [int(item) for item in user_old]
    user_old_date = date(year, month, day)
    plus_week = timedelta(weeks=COUNTER / 3)
    try:
        date_of_winning = d_today + plus_week
        user_winner_days_old = date_of_winning.year - user_old_date.year
    except:
        how_year_to_play = round((total_cost / 3 / 3 / 4.5 / 12), 0)
        date_of_winning = int(date.today().year) + int(how_year_to_play)
        user_winner_days_old = date_of_winning - user_old_date.year
        # return 'Wartość poza dostępnym zakresem. Rok wygrania jest  dalszy niż 9999 rok!'

    return [user_winner_days_old, date_of_winning]


if __name__ == '__main__':
    COUNTER, THREE, FOUR, FIVE = play_until_you_win(my_numbers, draw_numbers)
    TOTAL_COST = COST_OF_SINGLE_DRAW * COUNTER
    USER_WINNER_OLD, DATE_OF_WINNING = count_a_date(TOTAL_COST)

    print(f'Wygrałeś za {COUNTER:,} próbą!')
    print(f'Koszt inwestycji wynosi {TOTAL_COST:,} zł')
    print('Data wygrania:', DATE_OF_WINNING)

    print(f'W momencie wygranej będziesz miał {USER_WINNER_OLD} lat!')
    print(f'Trafiłeś trójkę {THREE:,} razy')
    print(f'Trafiłeś czwórkę {FOUR:,} razy')
    print(f'Trafiłeś piątke {FIVE:,} razy')

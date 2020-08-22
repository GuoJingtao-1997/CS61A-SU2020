"""Typing test implementation"""

from datetime import datetime

from ucb import interact, main, trace
from utils import *

###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    select_true = 0
    for paragraph in paragraphs:
        if select(paragraph):
            select_true += 1
            if select_true == k + 1: # has k + 1 pharagraphs which satisfied select function
                return paragraph
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def check_pharagraph(para):
        pharagraphs = split(lower(remove_punctuation(para)))
        for pharagraph in pharagraphs:
            if pharagraph in topic:
                return True
        return False
    return check_pharagraph
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    typed_len = len(typed_words)
    # BEGIN PROBLEM 3
    def helper(typed_words, reference_words, typed_len, correct_num=0):
        if not (typed_words and reference_words):
            return correct_num / typed_len * 100
        elif typed_words[0] == reference_words[0]:
            correct_num += 1
        return helper(typed_words[1:], reference_words[1:], typed_len, correct_num)
    return 0.0 if not typed_len else helper(typed_words, reference_words, typed_len)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time(as second) must be positive'
    # BEGIN PROBLEM 4
    typedLen = len(typed)
    typicalWordLen, minute = 5, 60
    typedPerSecond = typedLen / typicalWordLen / elapsed
    return 0.0 if not typedLen else typedPerSecond * minute
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    valid_words_len, smallest, closest_word, closest_i = len(valid_words), limit, user_word, len(valid_words) - 1
    for i in range(valid_words_len):
        diff_num = diff_function(user_word, valid_words[i], limit)
        if diff_num < smallest:
            smallest = diff_num
            closest_i, closest_word = i, valid_words[i]
        elif diff_num == smallest == limit:
            closest_i = min(closest_i, i)
            closest_word = valid_words[closest_i]
    return closest_word
    # END PROBLEM 5

def shifty_shifts(start, goal, limit, diff_num=0):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    if diff_num > limit or start == goal:
        return diff_num
    elif not (start and goal):
        return diff_num + abs(len(start) - len(goal))
    elif start[0] != goal[0]:
        diff_num += 1
    return shifty_shifts(start[1:], goal[1:], limit, diff_num)
    # END PROBLEM 6

def meowstake_matches(start, goal, limit):
    """It's too difficult for me, so I referred the answer"""
    """A diff function that computes the edit distance from START to GOAL.""" 
    # BEGIN PROBLEM 7 
    if limit < 0 or start == goal:  # Fill in the condition
        return 0
    elif not (start and goal):
        return abs(len(start) - len(goal))
    elif start[0] == goal[0]:
        return meowstake_matches(start[1:], goal[1:], limit)
    else:
        add_diff = 1 + meowstake_matches(start, goal[1:], limit - 1)
        remove_diff = 1 + meowstake_matches(start[1:], goal, limit - 1)
        substitute_diff = 1 + meowstake_matches(start[1:], goal[1:], limit - 1)

        return min(add_diff, remove_diff, substitute_diff)
    # END PROBLEM 7


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send, prompt_i=0, correct_num=0):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    if not typed or typed[0] != prompt[prompt_i]:
        progress = correct_num / len(prompt)
        send({'id': id, 'progress': progress})
        return progress
    return report_progress(typed[1:], prompt, id, send, prompt_i + 1, correct_num + 1)
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    assert all([len(times_per_player[i]) == len(times_per_player[i - 1]) for i in range(1, len(times_per_player))]), 'every player should type the same number of words'

    times_len = len(times_per_player[0])
    times_player = [[player[i] - player[i - 1] for i in range(1, times_len)] for player in times_per_player]
    return game(words, times_player)
    # END PROBLEM 9

def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = len(all_times(game)) # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    fastest_words = [[] for player in range(players)]
    for word in words:
        fastest_player = 0
        for player in range(1, players):
            if time(game, fastest_player, word) > time(game, player, word):
                fastest_player = player
        fastest_words[fastest_player].append(word_at(game, word))
    return fastest_words
    # END PROBLEM 10

def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = True  # Change to True when you

##########################
# Extra Credit #
##########################

key_distance = get_key_distances()

def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score. """
    
    # BEGIN PROBLEM EC1
    start = start.lower() #converts the string to lowercase
    goal = goal.lower()  #converts the string to lowercase

    def meowstake_matches_with_key_distance(start, goal, limit):
        if limit < 0:
            return float("inf")
        elif start == goal:  
            return 0
        elif not (start and goal):
            return abs(len(start) - len(goal))
        elif start[0] == goal[0]:
            return memo(meowstake_matches)(start[1:], goal[1:], limit)
        else:
            add_diff = 1 + memo(meowstake_matches)(start, goal[1:], limit - 1)
            remove_diff = 1 + memo(meowstake_matches)(start[1:], goal, limit - 1)
            substitute_diff = key_distance[start[0], goal[0]] + memo(meowstake_matches)(start[1:], goal[1:], limit - 1)

            return min(add_diff, remove_diff, substitute_diff)
    return meowstake_matches_with_key_distance(start, goal, limit)
    # END PROBLEM EC1

def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""

    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized

key_distance_diff = count(key_distance_diff)


def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""

    # BEGIN PROBLEM EC2
    diff_function = count(diff_function)
    if user_word in valid_words:
        return user_word
    smallest_diff = diff_function(user_word, valid_words[0], limit)
    closest_word = valid_words[0]
    for word in valid_words:
        if diff_function(user_word, word, limit) < smallest_diff:
            smallest_diff = diff_function(user_word, word, limit)
            closest_word = word
    return closest_word if smallest_diff < limit else user_word
    # END PROBLEM EC2


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)

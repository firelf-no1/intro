##############################################################
# FILE : ex4.py
# WRITER : itai shopen , firelf , 021982038
# EXERCISE : intro2cs ex3 2017-2018
# DESCRIPTION: a game of hangman
#############################################################
import hangman_helper


def main():
    """main function"""
    words_list = hangman_helper.load_words(file='words.txt')
    run_single_game(words_list)
    options, letter = hangman_helper.get_input()
    while options == hangman_helper.PLAY_AGAIN and letter == True:
        """runs another turn"""
        run_single_game(words_list)



def update_word_pattern(word, pattern, letter):
    """A program that's update the pattern"""
    word_lst = list(word)
    pattern_lst = list(pattern)
    for i in range(0, len(word)):
        if letter in word_lst[i]:
            pattern_lst[i] = letter
        pattern = ''.join(pattern_lst)
    return pattern


def letter_check(letter):
    """A program that's checks if an input is a lowercase single letter"""
    letter_check2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'
                     , 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'
                     , 'v', 'w', 'x', 'y', 'z']
    if letter not in letter_check2:
        return False
    else:
        return True


def letter_to_index(letter):
    """ Return the index of the given letter in an alphabet list. """
    CHAR_A = 97
    return ord(letter.lower()) - CHAR_A


def index_to_letter(index):
    """ Return the letter corresponding to the given index. """
    CHAR_A = 97
    return chr(index + CHAR_A)

def matching_len_word(words_list, pattern):
    pattern_lst = list(pattern)
    same_len_words = list()
    for i in range(0, len(words_list)):
        if len(pattern_lst) == len(words_list[i]):
            same_len_words.append(words_list[i])
    return same_len_words


def filter_words_list(words_list, pattern, wrong_guess_lst):
    """A program that's guts a list and checks if they are the right len
    and that they have the same order as the pattern"""
    error_count = len(wrong_guess_lst)
    pattern_lst = list(pattern)
    hint_list = list()
    words = matching_len_word(words_list, pattern)
    for i in range(0, len(words)):
        wrong_letter_counter = 0
        for m in range(0, error_count):
            if wrong_guess_lst[m] in words[i]:
                wrong_letter_counter += 1
        if wrong_letter_counter == 0:
            word_list = list(words[i])
            true_counter = 0
            letter_counter = 0
            for k in range(0, len(pattern_lst)):
                if pattern_lst[k] != '_':
                    true_counter += 1
                    if pattern_lst[k] == word_list[k]:
                        letter_counter += 1
            if true_counter == letter_counter:
                hint_list.append(words[i])
    return hint_list


def choose_letter(words, pattern):
    """A program that take's a list of words and checks whats the most
    frequent letter"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'
               , 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'
               , 'v', 'w', 'x', 'y', 'z']
    words_j = ''.join(words)
    pattern_lst = list(pattern)
    letter_hint = list()
    for l in range(0, len(letters)):
        place_counter = 0
        if letters[l] in pattern_lst:
            letter_hint.append(0)
        else:
            for c in range(0, len(words_j)):
                if words_j[c] == letters[l]:
                    place_counter += 1
            letter_hint.append(place_counter)
    hint = index_to_letter(letter_hint.index(max(letter_hint)))
    return hint


def run_single_game(words_list):
    """A function that runs the game of hangman"""
    word = hangman_helper.get_random_word(words_list)
    wrong_guess_lst = list()
    error_count = 0
    pattern = '_' * len(word)
    msg = hangman_helper.DEFAULT_MSG
    words = words_list
    while word != pattern and error_count < hangman_helper.MAX_ERRORS:
        hangman_helper.display_state(pattern, error_count,
                                     wrong_guess_lst, msg, False)
        options, letter = hangman_helper.get_input()
        word_lst = list(word)
        pattern_lst = list(pattern)
        if options == hangman_helper.HINT: # user asks for a hint
            words = filter_words_list(words, pattern,
                                      wrong_guess_lst)
            hint_letter = choose_letter(words, pattern)
            msg = hangman_helper.HINT_MSG + hint_letter
        elif options == hangman_helper.LETTER: # normel game play
            if letter_check (letter) == False:
                msg = hangman_helper.NON_VALID_MSG
            elif letter in pattern_lst or letter in wrong_guess_lst:
                msg = hangman_helper.ALREADY_CHOSEN_MSG + letter
            elif letter in word_lst:
                pattern = update_word_pattern(word, pattern, letter)
                msg = hangman_helper.DEFAULT_MSG
            else:
                wrong_guess_lst.append(letter)
                error_count += 1
                msg = hangman_helper.DEFAULT_MSG

    if word == pattern:
        msg = hangman_helper.WIN_MSG
        hangman_helper.display_state(pattern, error_count,
                                     wrong_guess_lst, msg, True)
    else:
        msg = hangman_helper.LOSS_MSG + word
        hangman_helper.display_state(pattern, error_count,
                                     wrong_guess_lst, msg, True)






if __name__ == "__main__":
    """A program that's run main"""
    hangman_helper.start_gui_and_call_main(main)
    hangman_helper.close_gui()

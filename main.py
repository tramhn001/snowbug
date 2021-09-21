from snowman.snowman import snowman, SNOWMAN_MIN_WORD_LENGTH, SNOWMAN_MAX_WORD_LENGTH
from wonderwords import RandomWord


def main():
    # Get a random word 5-8 letters long
    random_word_generator = RandomWord()
    snowman_word = random_word_generator.word(
        word_min_length=SNOWMAN_MIN_WORD_LENGTH, word_max_length=SNOWMAN_MAX_WORD_LENGTH)

    # snowman_word = "need to test a particular word during game play? try setting snowman_word"

    # play the game
    snowman(snowman_word)


if __name__ == '__main__':
    main()

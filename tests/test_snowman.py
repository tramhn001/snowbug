import sys
import io

from snowman.snowman import (
    snowman, add_wrong_letter, build_word_dict, is_word_guessed,
    build_game_board, build_snowman_graphic
)

# Helper method ################################################################


def make_std_input(guesses):
    guesses_with_newlines = "\n".join(guesses)
    return io.StringIO(f"{guesses_with_newlines}\n")


# Tests ########################################################################

def test_build_word_dict_builds_guessed_letter_data():
    # Arrange
    word = "snowman"

    # Act
    letters_guessed = build_word_dict(word)

    # Assert
    assert letters_guessed == {
        "s": False,
        "n": False,
        "o": False,
        "w": False,
        "m": False,
        "a": False,
    }


def test_build_word_dict_builds_guessed_letter_data_excluding_non_letter_characters():
    # Arrange
    word = "ad hoc"

    # Act
    letters_guessed = build_word_dict(word)

    # Assert
    assert letters_guessed == {
        "a": False,
        "d": False,
        "h": False,
        "o": False,
        "c": False,
    }


def test_is_word_guessed_detects_not_guessed_word():
    # Arrange
    word_dict = {
        "s": False,
        "n": False,
        "o": False,
        "w": False,
        "m": False,
        "a": False,
    }

    # Act
    is_guessed = is_word_guessed(word_dict)

    # Assert
    assert not is_guessed


def test_is_word_guessed_detects_guessed_word():
    # Arrange
    word_dict = {
        "s": True,
        "n": True,
        "o": True,
        "w": True,
        "m": True,
        "a": True,
    }

    # Act
    is_guessed = is_word_guessed(word_dict)

    # Assert
    assert is_guessed


def test_build_game_board_builds_empty_word_with_only_alpha():
    # Arrange
    word = "snowman"
    word_dict = {
        "s": False,
        "n": False,
        "o": False,
        "w": False,
        "m": False,
        "a": False,
    }

    # Act
    board = build_game_board(word, word_dict)

    # Assert
    assert board == "_ _ _ _ _ _ _"


def test_build_game_board_builds_complete_word_with_only_alpha():
    # Arrange
    word = "snowman"
    word_dict = {
        "s": True,
        "n": True,
        "o": True,
        "w": True,
        "m": True,
        "a": True,
    }

    # Act
    board = build_game_board(word, word_dict)

    # Assert
    assert board == "s n o w m a n"


def test_build_game_board_builds_empty_word_with_non_alpha():
    # Arrange
    word = "ad hoc"
    word_dict = {
        "a": False,
        "d": False,
        "h": False,
        "o": False,
        "c": False,
    }

    # Act
    board = build_game_board(word, word_dict)

    # Assert
    assert board == "_ _   _ _ _"


def test_build_game_board_builds_complete_word_with_non_alpha():
    # Arrange
    word = "ad hoc"
    word_dict = {
        "a": True,
        "d": True,
        "h": True,
        "o": True,
        "c": True,
    }

    # Act
    board = build_game_board(word, word_dict)

    # Assert
    assert board == "a d   h o c"


def test_build_snowman_graphic_builds_empty_snowman():
    # Arrange
    wrong_guesses = 0

    # Act
    snowman_image = build_snowman_graphic(wrong_guesses)

    # Assert
    assert snowman_image == ""


def test_build_snowman_graphic_builds_full_snowman():
    # Arrange
    wrong_guesses = 7

    # Act
    snowman_image = build_snowman_graphic(wrong_guesses)

    # Assert
    assert snowman_image == (
        "*   *   *  \n"
        " *   _ *   \n"
        "   _[_]_ * \n"
        '  * (")    \n'
        "  \\( : )/ *\n"
        "* (_ : _)  \n"
        "-----------"
    )


def test_wrong_guesses_are_in_alphabetical_order_when_guessed_in_order():
    # Arrange
    wrong_letters = []

    # Act
    add_wrong_letter(wrong_letters, "a")
    add_wrong_letter(wrong_letters, "b")
    add_wrong_letter(wrong_letters, "c")
    add_wrong_letter(wrong_letters, "d")
    add_wrong_letter(wrong_letters, "e")
    add_wrong_letter(wrong_letters, "f")

    # Assert
    assert wrong_letters == ["a", "b", "c", "d", "e", "f"]


def test_wrong_guesses_are_in_alphabetical_order_when_guessed_out_of_order():
    # Arrange
    wrong_letters = []

    # Act
    add_wrong_letter(wrong_letters, "f")
    add_wrong_letter(wrong_letters, "e")
    add_wrong_letter(wrong_letters, "d")
    add_wrong_letter(wrong_letters, "c")
    add_wrong_letter(wrong_letters, "b")
    add_wrong_letter(wrong_letters, "a")

    # Assert
    assert wrong_letters == ["a", "b", "c", "d", "e", "f"]


# The following four tests are equivalent to the tests from the replit version #

def test_prints_success_message_if_all_letters_guessed(capsys, monkeypatch):
    # Arrange (prepare to simulate user input)
    input_letters = "namwons"
    monkeypatch.setattr("sys.stdin", make_std_input(input_letters))

    # Act
    snowman("snowman")

    # Assert (capture the printed output)
    captured = capsys.readouterr()
    assert "you win" in captured.out.lower()


def test_prints_success_message_with_3_wrong_guesses_and_the_rest_right(capsys, monkeypatch):
    # Arrange (prepare to simulate user input)
    input_letters = "snbowmaqvn"
    monkeypatch.setattr("sys.stdin", make_std_input(input_letters))

    # Act
    snowman("snowman")

    # Assert (capture the printed output)
    captured = capsys.readouterr()
    assert "you win" in captured.out.lower()
    assert "sorry, you lose!" not in captured.out.lower()


def test_prints_failure_message_with_7_straight_wrong_guesses(capsys, monkeypatch):
    # Arrange (prepare to simulate user input)
    input_letters = "bcpzqvx"
    monkeypatch.setattr("sys.stdin", make_std_input(input_letters))

    # Act
    snowman("snowman")

    # Assert (capture the printed output)
    captured = capsys.readouterr()
    assert "you win" not in captured.out.lower()
    assert "sorry, you lose!" in captured.out.lower()
    assert "the word was snowman" in captured.out.lower()


def test_prints_failure_message_with_7_wrong_guesses_and_two_right(capsys, monkeypatch):
    # Arrange (prepare to simulate user input)
    input_letters = "sbcpnzqvx"
    monkeypatch.setattr("sys.stdin", make_std_input(input_letters))

    # Act
    snowman("snowman")

    # Assert (capture the printed output)
    captured = capsys.readouterr()
    assert "you win" not in captured.out.lower()
    assert "sorry, you lose!" in captured.out.lower()
    assert "the word was snowman" in captured.out.lower()


# A new simulated game scenario ################################################

def test_prints_success_message_if_all_letters_with_non_alpha_symbols_guessed(capsys, monkeypatch):
    # Arrange (prepare to simulate user input)
    input_letters = "nibtul"
    monkeypatch.setattr("sys.stdin", make_std_input(input_letters))

    # Act
    snowman("built-in")

    # Assert (capture the printed output)
    captured = capsys.readouterr()
    assert "you win" in captured.out.lower()

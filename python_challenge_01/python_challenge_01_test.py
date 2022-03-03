import pytest
import io
import math
import random
import python_challenge_01


def test_guess_number_format_exception_as_first_step(monkeypatch, capfd):
    monkeypatch.setattr('sys.stdin', io.StringIO("not_number"))
    with pytest.raises(ValueError):
        python_challenge_01.fun_guess_number()
    out, err = capfd.readouterr()
    assert "It is not a number!" in out


def test_guess_number_format_exception_during_guessing(monkeypatch, capfd):
    python_challenge_01.drawn_number = random.randrange(0, 100)
    monkeypatch.setattr('sys.stdin', io.StringIO(str(python_challenge_01.drawn_number - 5)))
    python_challenge_01.fun_guess_number()
    monkeypatch.setattr('sys.stdin', io.StringIO("not_number"))
    with pytest.raises(ValueError):
        python_challenge_01.fun_guess_number()
    out, err = capfd.readouterr()
    assert "It is not a number!" in out


def test_prompting_messages_during_guessing(capfd):
    python_challenge_01.drawn_number = 49
    python_challenge_01.fun_validation(50)
    out, err = capfd.readouterr()
    assert "Your number is too high!" in out
    python_challenge_01.drawn_number = 51
    python_challenge_01.fun_validation(50)
    out, err = capfd.readouterr()
    assert "Your number is too small!" in out


def test_guess_number_range_min(capfd):
    min_guess_number = -2
    python_challenge_01.fun_validation(min_guess_number)
    out, err = capfd.readouterr()
    assert f"Your value {min_guess_number} is out of range!" in out


def test_guess_number_range_max(capfd):
    max_guess_number = 101
    python_challenge_01.fun_validation(max_guess_number)
    out, err = capfd.readouterr()
    assert f"Your value {max_guess_number} is out of range!" in out


def test_exit_function_as_first_step(capfd):
    with pytest.raises(SystemExit) as error:
        python_challenge_01.guess_number = -1
        python_challenge_01.fun_exit()
    out, err = capfd.readouterr()
    assert "The user has terminated the program." in out
    assert error.value.code == -1


def test_exit_function_during_guessing(capfd):
    python_challenge_01.drawn_number = random.randrange(0, 100)
    python_challenge_01.fun_validation(math.fabs(python_challenge_01.drawn_number - 5))
    out, err = capfd.readouterr()
    assert "Your number is" in out
    with pytest.raises(SystemExit) as error:
        python_challenge_01.guess_number = -1
        python_challenge_01.fun_exit()
    out, err = capfd.readouterr()
    assert "The user has terminated the program." in out
    assert error.value.code == -1


def test_success_message_during_guessing(capfd):
    counter = 1
    python_challenge_01.drawn_number = random.randrange(0, 100)
    python_challenge_01.guess_number = python_challenge_01.drawn_number
    python_challenge_01.fun_exit()
    out, err = capfd.readouterr()
    assert f"You guessed! That's the number {python_challenge_01.drawn_number}! You hit in {counter} shots." in out

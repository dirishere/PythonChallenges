import pytest
import io
import random
import python_challenge_01


def test_guess_number_format_exception_as_first_step(monkeypatch, capfd):
    monkeypatch.setattr('sys.stdin', io.StringIO("A"))
    with pytest.raises(ValueError):
        python_challenge_01.fun_guess_number()
    out, err = capfd.readouterr()
    assert "It is not a number!" in out


def test_guess_number_format_exception_during_guessing(monkeypatch, capfd):
    drawn_number = random.randrange(0, 100)
    monkeypatch.setattr('sys.stdin', io.StringIO(str(drawn_number - 5)))
    python_challenge_01.fun_guess_number()
    monkeypatch.setattr('sys.stdin', io.StringIO("A"))
    with pytest.raises(ValueError):
        python_challenge_01.fun_guess_number()
    out, err = capfd.readouterr()
    assert "It is not a number!" in out


def test_prompting_messages_during_guessing(capfd):
    drawn_number = random.randrange(0, 100)
    python_challenge_01.fun_validation(50)
    out, err = capfd.readouterr()

    if drawn_number < 50:
        assert "Your number is too small!" in out
    else:
        assert "Your number is too high!" in out


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


def test_exit_function_as_first_step():
    pass


def test_exit_function_during_guessing():
    pass


def test_e2e_scenario_happy_path():
    pass

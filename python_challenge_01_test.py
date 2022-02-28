import pytest
import io
import python_challenge_01


def test_guess_number_format_exception_as_first_step(monkeypatch, capfd):
    monkeypatch.setattr('sys.stdin', io.StringIO("A"))
    with pytest.raises(ValueError):
        python_challenge_01.fun_guess_number()
    out, err = capfd.readouterr()
    assert "It is not a number!" in out


def test_guess_number_format_exception_during_guessing():
    pass


def test_guess_number_range_min():
    pass


def test_guess_number_range_max():
    pass


def test_exit_function_as_first_step():
    pass


def test_exit_function_during_guessing():
    pass


def test_e2e_scenario_happy_path():
    pass

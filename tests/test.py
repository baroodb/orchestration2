from app.main import get_home, greating
import pytest


def test_get_home():
    assert get_home() == {'Response': 'Hello World...'}


def test_greating():
    name = 'Oumar'
    assert greating(name) == {'Response': 'Welcome {}'.format(name)}

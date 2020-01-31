import pytest
from src.phonebook.phonebook import Phonebook


def test_lookup_by_name():
    phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_phonebook_contains_all_names():
    phonebook = Phonebook()
    phonebook.add("Bob", "1234")
    assert "Bob" in phonebook.names()


def test_missing_name_raises_error():
    phonebook = Phonebook()
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")

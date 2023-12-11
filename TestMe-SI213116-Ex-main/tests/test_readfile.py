from codetestdemo.namecounter import NameCounter
import pytest


def test_read_single_file():
    nmcnt = NameCounter(
        "C:\Users\mades\OneDrive\Documents\Malto\!\TestMe-SI213116-Ex-main\data\TEST\single_file.txt"
    )
    assert nmcnt.fnames == ["Dharma"]


def test_read_double_file():
    nmcnt = NameCounter(
        "C:\Users\mades\OneDrive\Documents\Malto\!\TestMe-SI213116-Ex-main\data\TEST\double_file.txt"
    )
    assert nmcnt.fnames == ["Dharma", "Diarta"]


def test_read_emptyfile_value():
    nmcnt = NameCounter(
        "C:\Users\mades\OneDrive\Documents\Malto\!\TestMe-SI213116-Ex-main\data\TEST\zero_file.txt"
    )
    assert nmcnt.fnames == []


def test_read_wrongspacings_file():
        nmcnt = NameCounter(
            "C:\Users\mades\OneDrive\Documents\Malto\!\TestMe-SI213116-Ex-main\data\TEST\wrong_spacings.txt"
        )
        assert nmcnt.fnames == ["Dh  arma"]

def test_read_special_characters():
    nmcnt = NameCounter(
        "C:\Users\mades\OneDrive\Documents\Malto\!\TestMe-SI213116-Ex-main\data\TEST\special_characters.txt"
    )
    assert nmcnt.fnames == ["Dharma", "dharma", "123", "!@#"]

def test_read_consecutive_special_characters():
    nmcnt = NameCounter(
        "C:\Users\mades\OneDrive\Documents\Malto\!\TestMe-SI213116-Ex-main\data\TEST\consecutive_special_characters.txt"
    )
    assert nmcnt.fnames == ["Dharma", "!!", "###", "$$"]

def test_read_special_characters_within_words():
    nmcnt = NameCounter(
        "C:\Users\mades\OneDrive\Documents\Malto\!\TestMe-SI213116-Ex-main\data\TEST\special_characters_within_words.txt"
    )
    assert nmcnt.fnames == ["Dharma", "test@123", "hello!world"]


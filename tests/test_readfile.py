from codetestdemo.namecounter import NameCounter
import pytest


def test_read_single_file():
    nmcnt = NameCounter(
        "C:\\Users\\Edward\\Downloads\\220030601\\TestMe-SI213116-Ex\\data\\TEST\\single_file.txt"
    )
    assert nmcnt.fnames == ["Dharma"]


def test_read_double_file():
    nmcnt = NameCounter(
        "C:\\Users\\Edward\\Downloads\\220030601\\TestMe-SI213116-Ex\\data\\TEST\\double_file.txt"
    )
    assert nmcnt.fnames == ["Dharma", "Diarta"]


def test_read_wrong_spacings():
    nmcnt = NameCounter(
        "C:\\Users\\Edward\\Downloads\\220030601\\TestMe-SI213116-Ex\\data\\TEST\\wrong_spacings.txt"
    )
    assert nmcnt.fnames == ["Dh  arma"]


def test_read_emptyfile():
    with pytest.raises(SystemExit):
        nmcnt = NameCounter(
            "/home/teguhsatya/lab/CodeTestingDemo/codetestdemo/data/TEST/zeros.txt"
        )

from codetestdemo.namecounter import NameCounter
import pytest


def test_read_single_file():
    nmcnt = NameCounter(
        "/home/teguhsatya/lab/CodeTestingDemo/codetestdemo/data/TEST/single_file.txt"
    )
    assert nmcnt.fnames == ["Dharma"]


def test_read_double_file():
    nmcnt = NameCounter(
        "/home/teguhsatya/lab/CodeTestingDemo/codetestdemo/data/TEST/double_file.txt"
    )
    assert nmcnt.fnames == ["Dharma", "Diarta"]


def test_read_emptyfile_value():
    nmcnt = NameCounter(
        "/home/teguhsatya/lab/CodeTestingDemo/codetestdemo/data/TEST/zero_file.txt"
    )
    assert nmcnt.fnames == []


def test_read_emptyfile():
    with pytest.raises(SystemExit):
        nmcnt = NameCounter(
            "/home/teguhsatya/lab/CodeTestingDemo/codetestdemo/data/TEST/zeros.txt"
        )

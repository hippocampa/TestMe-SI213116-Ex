from codetestdemo.namecounter import NameCounter
import pytest


def test_read_single_file():
    nmcnt = NameCounter(
        "C:/Git_RPL/TestMe-SI213116-Ex/data/TEST/single_file.txt"
    )
    assert nmcnt.fnames == ["Ananta"]


def test_read_double_file():
    nmcnt = NameCounter(
        "C:/Git_RPL/TestMe-SI213116-Ex/data/TEST/double_file.txt"
    )
    assert nmcnt.fnames == ["Ananta", "Putra"]


def test_read_emptyfile_value():
    nmcnt = NameCounter(
        "C:/Git_RPL/TestMe-SI213116-Ex/data/TEST/zero_file.txt"
    )
    assert nmcnt.fnames == []

#tambah wrong spacing
def test_read_wrong_spacings_file():
    nmcnt = NameCounter(
        "C:/Git_RPL/TestMe-SI213116-Ex/data/TEST/wrong_spacings.txt"
    )
    assert nmcnt.fnames == ["Ananta"]


# def test_read_emptyfile():
#     with pytest.raises(SystemExit):
#         nmcnt = NameCounter(
#             "/home/teguhsatya/lab/CodeTestingDemo/codetestdemo/data/TEST/zeros.txt"
#         )

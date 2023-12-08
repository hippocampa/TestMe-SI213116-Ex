from codetestdemo.namecounter import NameCounter
from codetestdemo.similarityenum import Sim
import pytest

def test_read_single_file():
    nmcnt = NameCounter(
        "C:/Users/asusv/OneDrive/Documents/TestMe-SI213116-Ex-1/data/TEST/single_file.txt"
    )
    assert nmcnt.fnames == ["Dharma"]



def test_read_double_file():
    nmcnt = NameCounter(
        "C:/Users/asusv/OneDrive/Documents/TestMe-SI213116-Ex-1/data/TEST/double_file.txt"
    )
    assert nmcnt.fnames == ["Dharma", "Diarta"]


def test_read_emptyfile_value():
    nmcnt = NameCounter(
        "C:/Users/asusv/OneDrive/Documents/TestMe-SI213116-Ex-1/data/TEST/zero_file.txt"
    )
    assert nmcnt.fnames == []


def test_read_emptyfile():
    with pytest.raises(SystemExit):
        nmcnt = NameCounter(
         "C:/Users/asusv/OneDrive/Documents/TestMe-SI213116-Ex-1/data/TEST/zeros_file.txt"
        )
        
def test_find_single_not_found():
    nmcnt = NameCounter("C:/Users/asusv/OneDrive/Documents/TestMe-SI213116-Ex-1/data/TEST/test_file.txt")
    result = nmcnt.find_single("NotExistingName")  # Nama tidak ada dalam daftar
    assert result == 0

def test_count_occurrences():
    nmcnt = NameCounter(
        "C:/Users/asusv/OneDrive/Documents/TestMe-SI213116-Ex-1/data/TEST/multiple_occurrences.txt"
    )
    result_jane = nmcnt.find_single("Jane")
    result_jim = nmcnt.find_single("Jim")
    assert result_jane == 2  # Jane muncul 2 kali dalam file
    assert result_jim == 1   # Jim muncul 1 kali dalam file

def test_find_single_empty_file():
    nmcnt = NameCounter(
        "C:/Users/asusv/OneDrive/Documents/TestMe-SI213116-Ex-1/data/TEST/empty_file.txt"
    )
    result = nmcnt.find_single("Hendra")
    assert result == 0


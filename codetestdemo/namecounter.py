from similarityenum import Sim
#from codetestdemo.similarityenum import Sim
from typing import List, Union, Any
import jellyfish as jf


class NameCounter:
    """NameCounter

    A class that is designed to count the occurence of names in a .txt file

    Methods:
        __init__(self) -> None
        find_single(self, name:str) -> int

    Attributes:
        fdir: a string of .txt file dir
    """

    def __init__(self, txtfile: str) -> None:
        """
        Initialize NameCounter class.

        Args:
            txtfile: .txt file directory

        """
        self.fnames: List[str] = self._read_file(txtf=txtfile)
        print(self.fnames)

    def find_single(
        self, name: str, sim: Sim = Sim.JARO_WRINKLER, sim_thresh: float = 0.9
    ) -> int:
        """Count the occurence of a single name from a txtfile.

        Args:
            name (str): Person's name
            sim (Sim): An Enumerator of similarities methods. Such enumerator exists: [Sim.JARO_WRINKLER, Sim.LEVENSHTEIN]
            sim_thresh (float): Similarity threshold, configured by user. The default value is 90%

        Returns:
            counter (int): Occurence counter
        """
        outnames = list(
            filter(
                lambda x: self._calc_similarities(x, name, sim) >= sim_thresh,
                self.fnames,
            )
        )
        return len(outnames)

    def _calc_similarities(
        self, name1: Union[str, Any], name2: str, method: Sim = Sim.JARO_WRINKLER
    ) -> float:
        """
        Calculating similarities between 2 strings

        Args:
            name1 (Union[str, Any]): first string name,
            name2 (str): second string name,
            methods (Sim): Sim's enumeration's method, default is Sim.COSINE

        Returns:
            Similarity's value (float)
        """
        if method == Sim.JARO_WRINKLER:
            return jf.jaro_winkler_similarity(name1.lower(), name2.lower())
        elif method == Sim.LEVENSHTEIN:
            return jf.levenshtein_distance(s1=name1.lower(), s2=name2.lower())
        else:
            raise NotImplementedError(f"Unsupported similarity method: {method}")

    def _read_file(self, txtf: str) -> List[str]:
        """
        Read a .txt file

        Args:
            textf (str): .txt file dir

        Returns:
            List of name
        """
        try:
            list_of_names = list()
            with open(txtf, "r") as f:
                list_of_names = [line.strip() for line in f]
            return list_of_names
        except Exception as e:
            print(e)
            exit(1)

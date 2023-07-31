import pytest

from utils import unpacking_data
from utils import get_date


#def test_unpacking_data():

    #data = unpacking_data()
   # assert isinstance(data, list)

def test_get_date():
    assert get_date("2018-06-30T02:08:58.425572") == 3
    2018

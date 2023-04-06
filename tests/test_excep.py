
import pytest
from src.phone import Item
from src.excep import InstantiateCSVError

def test_item_py_one():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../src/itemsФ.csv')
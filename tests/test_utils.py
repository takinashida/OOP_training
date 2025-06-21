from unittest.mock import patch

from config import ROOT_DIR
from src.utils import get_classes, json_load

path_to_json = ROOT_DIR.joinpath("data", "products.json")


@patch("src.utils.json.load")
def test_json_load(mock_data):
    fake_data = [{"a": 1}]
    mock_data.return_value = fake_data
    assert json_load(path_to_json) == [{"a": 1}]


def test_get_classes():
    fake_list = [
        {
            "name": "cat1",
            "description": "be",
            "products": [
                {"name": "name1", "description": "be", "price": 1.0, "quantity": 1},
                {"name": "name2", "description": "be", "price": 2.0, "quantity": 2},
                {"name": "name3", "description": "be", "price": 3.0, "quantity": 3},
            ],
        },
        {
            "name": "cat1",
            "description": "be",
            "products": [{"name": "name1", "description": "be", "price": 1.0, "quantity": 1}],
        },
    ]
    categories, products = get_classes(fake_list)
    assert categories[0].name == "cat1"

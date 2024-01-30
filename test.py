import unittest
import json
from typing import Dict, Any
from main import sniff_schema, set_data_type 



class TestSchemaSniffer(unittest.TestCase):

    def test_set_data_type_string(self):
        self.assertEqual(set_data_type("Hello World"), "STRING")

    def test_set_data_type_integer(self):
        self.assertEqual(set_data_type(10), "INTEGER")

    def test_set_data_type_enum(self):
        self.assertEqual(set_data_type(["apple", "banana","garri"]), "ENUM")

    def test_set_data_type_array(self):
        self.assertEqual(set_data_type([{"name": "Bola"}, {"name": "Atiku"}]), "ARRAY")

    def test_sniff_schema(self):
        json_data = {
            "message": {
                "name": "John",
                "age": 45,
                "fruits": ["apple", "banana","garri"],
                "people": [{"name": "Bola"}, {"name": "Atiku"}]
            }
        }
        expected_schema = {
            "name": {"type": "STRING", "tag": "", "description": "", "required": False},
            "age": {"type": "INTEGER", "tag": "", "description": "", "required": False},
            "fruits": {"type": "ENUM", "tag": "", "description": "", "required": False},
            "people": {"type": "ARRAY", "tag": "", "description": "", "required": False},
        }
        self.assertEqual(sniff_schema(json_data), expected_schema)



if __name__ == '__main__':
    unittest.main()

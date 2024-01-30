import unittest
import json
from typing import Dict, Any
from main import sniff_schema, set_data_type 



class TestSchemaSniffer(unittest.TestCase):
    
    def test_padding(self):
        """This function checks if the JSON schema are padded with the 'tag' and 'description'
        attributes as given in our problem description"""

        with open('data/data_1.json','r') as f:
            json_data = json.load(f)
        
        schema = sniff_schema(json_data)

        for key, value in schema.items():
            with self.subTest(key=key):
                # So we can know that the "tag" and "description" keys 
                #     exist in all attributes in the schema
                self.assertIn("tag", value)
                self.assertIn("description", value)
    
    def test_schema_output(self):
        pass

    def test_required(self):
        pass
    
    def test_sniff_schema(self):
        """
        This function checks to see if the data types in the schema are mapped properly, using a mock
        expected schema
        """

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

import unittest
import json
from typing import Dict, Any
from main import sniff_schema, set_data_type 



class TestSchemaSniffer(unittest.TestCase):
    
    def test_padding(self):
        """This function checks if the JSON schema are padded with the 'tag' and 'description'
        attributes as given in our problem description in PROBLEM.md"""

        for key, value in schema.items():
            with self.subTest(key=key):
                # So we can know that the "tag" and "description" keys 
                #     exist in all attributes in the schema
                self.assertIn("tag", value)
                self.assertIn("description", value)
    
    def test_exclude_attributes_key(self):
        """
        This test makes sure that the values in the "attributes" key 
        (appName, eventType, subEventtype & sensitive)  are not found in the generated schema
        """

        for key, value in schema.items():
            with self.subTest(key=key):
                self.assertNotIn("appName", value)
                self.assertNotIn("eventType", value)
                self.assertNotIn("subEventType", value)
                self.assertNotIn("sensitive", value)



    def test_required(self):
        """
        This checks if all the required attributes in the schema are set to False.
        """
        for key, value in schema.items():
            with self.subTest(key=key):
                self.assertFalse(value["required"]) # helps us to check if required = False for every value
    

    def test_sniff_schema(self):
        """
        This function checks to see if all of the 4 data types in the schema are mapped properly, using a mock
        expected schema
        """

        mock_json_data = {
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
        self.assertEqual(sniff_schema(mock_json_data), expected_schema)
    



if __name__ == '__main__':
    with open('data/data_2.json','r') as f:
        json_data = json.load(f)
            
    schema = sniff_schema(json_data)
    unittest.main() # run our unittest

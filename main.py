import json
from typing import Dict, Any


def set_data_type(value: Any) -> str:
    if type(value) is str:
        return "STRING"

    elif type(value) is int:
        return "INTEGER"

    elif value and type(value) is list and all(type(item) is str for item in value):
        return "ENUM" 

    elif  value and  (type(value) is list and all(type(item) is dict for item in value)):
        return "ARRAY"


def sniff_schema(json_data: Dict[str, Any]) -> Dict:
    output_schema = {}
    message_data = json_data.get("message", {})
    
    for key, value in message_data.items():
        output_schema[key] = {
            "type": set_data_type(value),
            "tag": "",
            "description": "",
            "required": False,
        }

    return output_schema


def main(input_file_path: str, output_file_path: str) -> None:
    with open(input_file_path, "r") as input_file:
        json_data = json.load(input_file)

    schema = sniff_schema(json_data)

    with open(output_file_path, "w") as output_file:
        json.dump(schema, output_file, indent=2)


if __name__ == "__main__":
    main('data/data_1.json', 'schema/schema_1.json')
    main('data/data_2.json', 'schema/schema_2.json')

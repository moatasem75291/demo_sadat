import json
from .score_calculator import *
import os

# Helper function to load reference data
def load_json(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# Load all reference data once (Improves efficiency)


# Generic processing function
def process_age_range(input_path, output_path, age_group,REFERENCE_DATA):
    user_data = load_json(input_path)

    if age_group == "5-8":
        processor = Age5to8(user_data, REFERENCE_DATA["plate"], REFERENCE_DATA["balance"])
    elif age_group == "9-18":
        processor = Age9to18(
            user_data, 
            REFERENCE_DATA["curl_up"], 
            REFERENCE_DATA["push_up"], 
            REFERENCE_DATA["run"], 
            REFERENCE_DATA["speed"]
        )
    else:
        raise ValueError("Invalid age group. Choose '5-8' or '9-18'.")

    processor.process_tests()
    with open(os.path.join(output_path , f'{age_group}_score_result.json' ), "w") as f:
        json.dump(processor.results, f, indent=4)


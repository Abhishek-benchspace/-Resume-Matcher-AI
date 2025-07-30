import os
import json

def load_job_roles():
    current_dir = os.path.dirname(__file__)  # this is the 'skills' folder
    json_path = os.path.join(current_dir, 'job_roles.json')

    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

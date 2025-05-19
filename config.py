"""
config.py
"""

import os

from helpers import parse_json_file, write_json

# set section names
QUALIFICATIONS = "qualifications"
EDUCATION = "education"
EXPERIENCES = "experiences"
PROJECTS = "projects"
PUBLICATIONS = "publications"
RESEARCH_EXPERIENCES = "research_experiences"
CONFERENCES = "conferences"
section_names = [
    QUALIFICATIONS,
    EDUCATION,
    EXPERIENCES,
    PROJECTS,
    PUBLICATIONS,
    RESEARCH_EXPERIENCES,
    CONFERENCES,
]

# set filenames
content_filepaths = dict()
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
for section in section_names:
    filename = f"{section}.json"
    filepath = os.path.join(_BASE_DIR, "content", filename)
    content_filepaths[section] = filepath
_personal_filename = os.path.join(_BASE_DIR, "content", "personal.json")
_configs_filename = os.path.join(_BASE_DIR, "content", "configs.json")

# get personal_data
personal_data = parse_json_file(_personal_filename)

# get configs
configs = parse_json_file(_configs_filename)

# set resume_filepath
resume_filepath = ''
def _set_resume_filepath(filepath):
    global resume_filepath
    resume_filepath = filepath

    # update configs.json
    if filepath != configs['resume_filepath']:
        configs['resume_filepath'] = filepath
        write_json(filename=_configs_filename, data=configs)
_set_resume_filepath(configs['resume_filepath'])

def update_configs(
    new_name: str | None = None,
    new_phone_number: str | None = None,
    new_github_url: str | None = None,
    new_linkedin_url: str | None = None,
    new_email: str | None = None,
    new_project_url: str | None = None,
    new_filepath: str | None = None,
):
    # update personal data
    personal_data['name']         = new_name or personal_data['name']
    personal_data['phone_number'] = new_phone_number or personal_data['phone_number']
    personal_data['github_url']   = new_github_url or personal_data['github_url']
    personal_data['linkedin_url'] = new_linkedin_url or personal_data['linkedin_url'] 
    personal_data['email']        = new_email or personal_data['email'] 
    personal_data['project_url']  = new_project_url or personal_data['project_url']
    write_json(filename=_personal_filename, data=personal_data)

    # update config data
    if new_filepath:
        _set_resume_filepath(new_filepath)

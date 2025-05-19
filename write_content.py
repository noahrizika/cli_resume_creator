"""
write_content.py
"""

from typing import Dict, List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle
from itertools import chain

from config import content_filepaths, personal_data, QUALIFICATIONS, EDUCATION, EXPERIENCES, PROJECTS
from styles import title_style, newline_sub_chunk, body_style_c, bullet_style, newline_chunk
from helpers import parse_json_file

from classes.generic_section import GenericSection
from classes.header import Header
from classes.experience import Experience
from classes.project import Project
from classes.education import Education


def write_section(
    section_name: str,
    selected_contents: Optional[List[int]] = [],
):
    # set constants
    filename = content_filepaths[section_name]
    content_type = section_name.lower()
    
    # write content for all selected
    contents = []
    all_content = parse_json_file(filename)
    get_everything = not selected_contents
    for chunk in all_content:
        if get_everything or ('id' not in chunk) or (chunk['id'] in selected_contents):
            content = _write_content(
                chunk=chunk, content_type=content_type
            )
            # content type varies based on section, which determines how to add to contents
            contents.extend(content) if isinstance(content, tuple) else contents.append(content)
            contents.extend(newline_sub_chunk)

    # combine all parts into a single list. include a title
    section = _join_section(content_type=content_type, contents=contents)
    return section


def _write_content(chunk: Dict[str, str], content_type: str):
    content = None
    if content_type == EDUCATION:
        edu = Education(chunk)
        content = edu.write_education()

    elif content_type == EXPERIENCES:
        exp = Experience(chunk)
        content = exp.write_experience()

    elif content_type == PROJECTS:
        project = Project(chunk)
        content = project.write_project()

    else:
        generic = GenericSection(chunk['details'])
        content = generic.write_bullets()

    return content

def _join_section(content_type: str, contents):
    title = content_type.upper()
    if content_type == PROJECTS:
        title = f'PROJECTS (<a href="{personal_data["project_url"]}">{personal_data["project_url"]}</a>)'
    title_p = Paragraph(title, title_style)

    section = list(chain([title_p], contents, newline_chunk))
    return section

def write_qualifications_section(
    skill_type: str,
    have_fullstack: bool,
    have_syseng: bool,
    have_ml: bool,
):
    all_content = parse_json_file(content_filepaths[QUALIFICATIONS])
    data = []

    data.append(all_content[skill_type])
    data.append(all_content['git'])

    if have_fullstack:
        data.append(all_content['fullstack_exp'])
    if have_syseng:
        data.append(all_content['syseng_exp'])
    if have_ml:
        data.append(all_content['ml_exp'])

    quals = GenericSection(data)
    contents = quals.write_bullets()
    section = _join_section(content_type=QUALIFICATIONS, contents=[contents])
    return section


def write_clearance_eligible():
    text = f"<b>Eligible for TS w/ Polygraph Security Clearance</b>"
    section = Paragraph(text, title_style)
    return section

"""
build_resume.py
"""

from typing import Dict, List, Optional
from reportlab.platypus import PageBreak

from config import (
    QUALIFICATIONS,
    EDUCATION,
    EXPERIENCES,
    PROJECTS,
    PUBLICATIONS,
    RESEARCH_EXPERIENCES,
    CONFERENCES,
    section_names,
)
from styles import line_break, newline_chunk
from write_content import write_section, write_qualifications_section, write_clearance_eligible
from classes.header import Header
from classes.qualifications import Qualifications


def build_resume(
    skill_type: str,
    have_fullstack: bool,
    have_syseng: bool,
    have_ml: bool,
    have_clearance: bool,
    included_sections: List[str],
    selected_experiences: Optional[List[int]] = [],
    selected_projects: Optional[List[int]] = [],
    selected_educations: Optional[List[int]] = [],
):
    header = Header()
    content = header.write_header()

    qualifications_section = write_qualifications_section(
        skill_type=skill_type,
        have_fullstack=have_fullstack,
        have_syseng=have_syseng,
        have_ml=have_ml,
    )
    content.extend(qualifications_section)

    sections_and_topics = merge_sections_and_topics(
        included_sections=included_sections,
        selected_experiences=selected_experiences,
        selected_projects=selected_projects,
        selected_educations=selected_educations,
    )

    for section_name, selected_contents in sections_and_topics:
        section = write_section(
            section_name=section_name,
            selected_contents=selected_contents,
        )

        # add a page break before projects if including all sections
        if not included_sections and section_name == PROJECTS:
            content.append(PageBreak())
        content.extend(section)

    if have_clearance:
        clearance_eligible = write_clearance_eligible()
        content.extend(newline_chunk)
        content.extend(newline_chunk)
        content.append(clearance_eligible)
    
    return content

def merge_sections_and_topics(
    included_sections: List[str],
    selected_experiences: Optional[List[int]] = [],
    selected_projects: Optional[List[int]] = [],
    selected_educations: Optional[List[int]] = [],
):
    # edge case: set to all sections
    if not included_sections:
        return [[name, []] for name in section_names if name != QUALIFICATIONS]
        
    sections_and_topics = []
    for section_name in included_sections:
        selected_topics = []
        if section_name == EDUCATION:
            selected_topics = selected_educations
        elif section_name == EXPERIENCES:
            selected_topics = selected_experiences
        elif section_name == PROJECTS:
            selected_topics = selected_projects
        sections_and_topics.append([section_name, selected_topics])
    return sections_and_topics

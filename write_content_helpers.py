from typing import List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle

from styles import newline_sub_chunk
from classes.header import Header
from classes.qualifications import Qualifications
from classes.experience import Experience
from classes.project import Project
from classes.education import Education

# def _parse_file(filename: str, metadata: dict{str:str}, selected_components: List[int], body_keyword: str, title_style, body_style, sub_body_style):


def write_experiences(
    filename,
    selected_experiences: List[int],
    title_style,
    body_style_l,
    body_style_r,
    sub_body_style_l,
    sub_body_style_r,
    bullet_style,
    table_style,
):
    experience_metadata = {
        "POSITION": "",
        "COMPANY": "",
        "LOCATION": "",
        "DURATION": "",
    }

    experiences = []
    this_experience = False
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line.isdigit() and int(line) in selected_experiences:
                this_experience = True
            elif this_experience:

                for field in experience_metadata:
                    if line.startswith(field):
                        experience_metadata[field] = line.split(" ", 1)[1].strip()

                # get duties, create experience block, append to experiences list
                if line.startswith("DETAILS"):
                    duties = []
                    for line in file:
                        line = line.strip()
                        if line == "":
                            break
                        duties.append(line)

                    exp = Experience(
                        position=experience_metadata["POSITION"],
                        company=experience_metadata["COMPANY"],
                        location=experience_metadata["LOCATION"],
                        duration=experience_metadata["DURATION"],
                        duties=duties,
                    )

                    exp_content = exp.write_experience(
                        body_style_l,
                        body_style_r,
                        sub_body_style_l,
                        sub_body_style_r,
                        bullet_style,
                        table_style,
                    )
                    experiences.extend(exp_content)
                    experiences.extend(newline_sub_chunk)

                    this_experience = False

    title_p = Paragraph("EXPERIENCES", title_style)
    return title_p, experiences


def write_projects(
    filename: str,
    project_url: str,
    selected_projects: list[int],
    title_style,
    body_style,
    bullet_style,
    table_style,
):

    project_name = ""
    projects = []
    this_project = False
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line.isdigit() and int(line) in selected_projects:
                this_project = True
                project_name = ""
                descriptions = []

            elif this_project:
                project_name = line
                for line in file:
                    line = line.strip()
                    if line == "":
                        break
                    else:
                        descriptions.append(line)

                # create project
                project = Project(project_name=project_name, descriptions=descriptions)
                project_content = project.write_project(
                    body_style, bullet_style, table_style
                )
                projects.extend(project_content)
                projects.extend(newline_sub_chunk)

                this_project = False
                first_line = True

    title = f'PROJECTS (<a href="{project_url}">{project_url}</a>)'
    title_p = Paragraph(title, title_style)

    return title_p, projects


def write_educations(
    filename,
    selected_educations,
    title_style,
    body_style_l,
    body_style_r,
    sub_body_style_l,
    sub_body_style_r,
    sub_bullet_style,
    table_style,
):
    education_metadata = {
        "NAME": "",
        "DURATION": "",
        "PROGRAM": "",
        "LOCATION": "",
    }

    educations = []
    this_education = False
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line.isdigit() and int(line) in selected_educations:
                education_metadata = education_metadata.fromkeys(
                    education_metadata, ""
                )  # reset values to empty strings
                this_education = True
            elif this_education:

                for field in education_metadata:
                    if line.startswith(field):
                        education_metadata[field] = line.split(" ", 1)[1].strip()

                # get details, create education block, append to education list
                if line.startswith("DETAILS"):
                    details = []
                    for line in file:
                        line = line.strip()
                        if line == "":
                            break
                        details.append(line)

                    edu = Education(metadata=education_metadata, details=details)

                    edu_content = edu.write_education(
                        body_style_l,
                        body_style_r,
                        sub_body_style_l,
                        sub_body_style_r,
                        sub_bullet_style,
                        table_style,
                    )
                    educations.extend(edu_content)
                    educations.extend(newline_sub_chunk)

                    this_education = False

    title_p = Paragraph("EDUCATION", title_style)

    return title_p, educations


class Generic_Section:
    def __init__(
        self, header: str, bullet_header: str, duration: str, bullet_points: list[str]
    ) -> None:
        self.header = header
        self.bullet_header = bullet_header
        self.duration = duration
        self.bullet_points = bullet_points.copy()

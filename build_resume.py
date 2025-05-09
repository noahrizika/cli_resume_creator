from styles import *
from write_content_helpers import *
from config import *

def build_resume(
        name: str,
        skill_type: str,
        have_fullstack: bool,
        have_syseng: bool,
        have_ml: bool,
        project_url: str,
        selected_experiences: Optional[List[int]],
        selected_projects: Optional[List[int]],
        selected_educations: Optional[List[int]],
    ):

    header = Header(name, '', '', '', '')
    header_section = header.write_header(body_style=body_style_c, main_title_style=main_title_style)

    quals = Qualifications(
        skill_type=skill_type,
        have_fullstack=have_fullstack,
        have_syseng=have_syseng,
        have_ml=have_ml,
    )
    quals_section = quals.write_qualifications(
        bullet_style=bullet_style, title_style=title_style
    )

    experiences_title, experiences_section = write_experiences(
        filename=experiences_filename,
        selected_experiences=selected_experiences,
        title_style=title_style,
        body_style_l=body_style_l,
        body_style_r=body_style_r,
        sub_body_style_l=sub_body_style_l,
        sub_body_style_r=sub_body_style_r,
        bullet_style=bullet_style,
        table_style=table_style
    )

    projects_title, projects_section = write_projects(
        filename=projects_filename,
        project_url=project_url,
        selected_projects=selected_projects,
        title_style=title_style,
        body_style=body_style_l,
        bullet_style=bullet_style,
        table_style=table_style
    )

    education_title, education_section = write_educations(
        filename=education_filename,
        selected_educations=selected_educations,
        title_style=title_style,
        body_style_l=body_style_l,
        body_style_r=body_style_r,
        sub_body_style_l=sub_body_style_l,
        sub_body_style_r=sub_body_style_r,
        sub_bullet_style=sub_bullet_style,
        table_style=table_style
    )

    content = (
        header_section
        + line_break
        + newline_chunk
        + quals_section
        + newline_chunk
        + [education_title]
        + education_section
        + newline_chunk
        + [experiences_title]
        + experiences_section
        + newline_chunk
        + [projects_title]
        + projects_section
    )

    return content

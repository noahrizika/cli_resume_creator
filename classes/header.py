'''
classes/header.py
'''

from typing import List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle

from config import personal_data
from styles import main_title_style, body_style_c, line_break, newline_chunk

class Header:

    def __init__(
        self,
    ) -> None:
        self.name = personal_data['name']
        self.phone_number = personal_data['phone_number']
        self.github_url = personal_data['github_url']
        self.linkedin_url = personal_data['linkedin_url']
        self.email = personal_data['email']

    def write_header(self):
        title_p = Paragraph(self.name, main_title_style)
        text = f"""
            {self.phone_number} •
            <a href="https://{self.github_url}">{self.github_url}</a> •
            <a href="https://www.{self.linkedin_url}">{self.linkedin_url}</a> •
            <a href="mailto:{self.email}">{self.email}</a>
            """
        body = Paragraph(text, body_style_c)

        section = [title_p, body]
        section.extend(line_break)
        section.extend(newline_chunk)
        return section

from typing import List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle

class Header:

    def __init__(
        self,
        name: str,
        phone_number: str,
        github_url: str,
        linkedin_url: str,
        email: str,
    ) -> None:
        self.name = name
        self.A_phone_number = phone_number
        self.B_github_url = github_url
        self.C_linkedin_url = linkedin_url
        self.D_email = email

    def write_header(self, body_style, main_title_style):
        title_p = Paragraph(self.name, main_title_style)
        text = """
            +1 (310) 720-7415 •
            <a href="https://noahrizika.github.io">noahrizika.github.io</a> •
            <a href="https://linkedin.com/in/noah-rizika">linkedin.com/in/noah-rizika</a> •
            <a href="mailto:noahrizika@gmail.com">noahrizika@gmail.com</a>
            """
        body = Paragraph(text, body_style)
        return [title_p, body]




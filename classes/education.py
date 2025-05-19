"""
classes/education.py
"""

from typing import Dict, List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle

from styles import body_style_l, body_style_r, sub_body_style_l, sub_body_style_r, sub_bullet_style, table_style
from classes.generic_section import GenericSection

class Education(GenericSection):
    def __init__(self, content: Dict[str, str]):
        self.name = content.get("name", "")
        self.duration = content.get("duration", "")
        self.program = content.get("program", "")
        self.location = content.get("location", "")

        # extract and reformat details
        data = []
        for k, v in content['details'].items():
            head = k.title()
            if k == 'GPA': # edge case: all letters in GPA should be capitalized
                head = k
            line = f"{head}: {v}"
            data.append(line)

        super().__init__(data)  # Call the parent constructor to initialize details

    def write_education(
        self,
        table_widths: Optional[list[float]] = [350.0, 150.0],
    ):
        # make a table for 1st and 2nd lines to have L and R alignment
        # write position in bold
        name_bold = f"<b>{self.name}</b>"
        name_p = Paragraph(name_bold, body_style_l) if self.name else ""

        # write company in italics
        program_italics = f"<i>{self.program}</i>"
        program_p = Paragraph(program_italics, sub_body_style_l) if self.program else ""

        duration_p = Paragraph(self.duration, body_style_r) if self.duration else ""
        location_p = Paragraph(self.location, sub_body_style_r) if self.location else ""

        # build table differently depending on empty values
        if self.name and self.duration and not self.program and not self.location: # assume education is a certification
            table_data = [[name_p, duration_p]]
        else:
            table_data = [[name_p, duration_p], [program_p, location_p]]

        edu_table = Table(table_data, colWidths=table_widths)
        edu_table.setStyle(
            table_style
        )
       
        details_list = self.write_bullets(b_style=sub_bullet_style)

        return edu_table, details_list

from typing import List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle

class Education:
    def __init__(self, metadata: dict[str, str], details: list[str]):
        self.name = metadata.get("NAME", "")
        self.duration = metadata.get("DURATION", "")
        self.program = metadata.get("PROGRAM", "")
        self.location = metadata.get("LOCATION", "")
        self.details = details

    def write_education(
        self,
        body_style_l,
        body_style_r,
        sub_body_style_l,
        sub_body_style_r,
        sub_bullet_style,
        table_style,
        bold_words: Optional[list[str]] = None,
        reg_words: Optional[list[str]] = None,
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
       
        # details
        details = [
            (ListItem(Paragraph(detail, sub_bullet_style))) for detail in self.details
        ]
        details_list = ListFlowable(details, bulletType='bullet')

        return edu_table, details_list

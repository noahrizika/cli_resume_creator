'''
classes/experience.py
'''

from typing import Dict, List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle

from styles import body_style_l, body_style_r, sub_body_style_l, sub_body_style_r, table_style, bullet_style
from classes.generic_section import GenericSection

class Experience(GenericSection):
    def __init__(
        self,
        content: Dict[str, str],
    ) -> None:
        super().__init__(content['details'])  # Call the parent constructor to initialize details

        self.position = content.get('position', '')
        self.company = content.get('company', '')
        self.location = content.get('location', '')
        self.duration = content.get('duration', '')

    def write_experience(
        self,
        table_widths: Optional[list[float]] = [350.0, 150.0],
    ):
        # make a table for 1st and 2nd lines to have L and R alignment
        # write position in bold
        position_bold = f'<b>{self.position}</b>'
        position_p = Paragraph(position_bold, body_style_l)

        # write company in italics
        company_italics = f'<i>{self.company}</i>'
        company_p = Paragraph(company_italics, sub_body_style_l)

        location_p = Paragraph(self.location, body_style_r)
        duration_p = Paragraph(self.duration, sub_body_style_r)

        table_data = [[position_p, location_p], [company_p, duration_p]]
        exp_table = Table(table_data, colWidths=table_widths)
        exp_table.setStyle(table_style)

        # 3rd p - duties
        details_list = self.write_bullets()

        return exp_table, details_list



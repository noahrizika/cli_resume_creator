"""
classes/project.py
"""

from typing import Dict, List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle

from styles import body_style_l, table_style
from classes.generic_section import GenericSection

class Project(GenericSection):
    def __init__(
        self,
        content: Dict[str, str],
    ) -> None:
        super().__init__(content['details'])  # Call the parent constructor to initialize details

        self.project_name = content.get("project_name")

    def write_project(
        self,
        table_widths: Optional[list[float]] = [350.0, 150.0],
    ):
        project_name_bold = f'<b>{self.project_name}</b>'
        project_name_p = Paragraph(project_name_bold, body_style_l)
        
        table_data = [[project_name_p, []]]
        proj_table = Table(table_data, colWidths=table_widths)
        proj_table.setStyle(
            table_style
        )

        descriptions_list = self.write_bullets()

        return proj_table, descriptions_list


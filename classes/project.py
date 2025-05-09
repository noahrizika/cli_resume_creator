from typing import List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle

class Project:
    def __init__(
        self,
        project_name: str,
        descriptions: list[str],
    ) -> None:
        self.project_name = project_name
        self.descriptions = descriptions.copy()

    def write_project(
        self,
        body_style,
        bullet_style,
        table_style,
        bold_words: Optional[list[str]] = None,
        reg_words: Optional[list[str]] = None,
        table_widths: Optional[list[float]] = [350.0, 150.0],
    ):
        project_name_bold = f'<b>{self.project_name}</b>'
        project_name_p = Paragraph(project_name_bold, body_style)
        
        table_data = [[project_name_p, []]]
        proj_table = Table(table_data, colWidths=table_widths)
        proj_table.setStyle(
            table_style
        )

        descriptions = [(ListItem(Paragraph(description, bullet_style))) for description in self.descriptions]
        descriptions_list = ListFlowable(descriptions, bulletType='bullet')

        return proj_table, descriptions_list



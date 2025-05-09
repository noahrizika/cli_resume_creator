from typing import List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle

class Experience:
    def __init__(
        self,
        position: str,
        company: str,
        location: str,
        duration: str,
        duties: list[str],
    ) -> None:
        self.position = position
        self.company = company
        self.location = location
        self.duration = duration
        self.duties = duties.copy()

    def write_experience(
        self,
        body_style_l,
        body_style_r,
        sub_body_style_l,
        sub_body_style_r,
        bullet_style,
        table_style,
        bold_words: Optional[list[str]] = None,
        reg_words: Optional[list[str]] = None,
        table_widths: Optional[list[float]] = [350.0, 150.0],
    ):
        # make a table for 1st and 2nd lines to have L and R alignment
        # write position in bold
        position_bold = f"<b>{self.position}</b>"
        position_p = Paragraph(position_bold, body_style_l)

        # write company in italics
        company_italics = f"<i>{self.company}</i>"
        company_p = Paragraph(company_italics, sub_body_style_l)

        location_p = Paragraph(self.location, body_style_r)
        duration_p = Paragraph(self.duration, sub_body_style_r)

        table_data = [[position_p, location_p], [company_p, duration_p]]
        exp_table = Table(table_data, colWidths=table_widths)
        exp_table.setStyle(table_style)

        # 3rd p - duties
        duties = [(ListItem(Paragraph(duty, bullet_style))) for duty in self.duties]
        duties_list = ListFlowable(duties, bulletType='bullet')

        return exp_table, duties_list



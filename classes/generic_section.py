"""
classes/generic_section.py
"""

from typing import Dict, List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable

from styles import bullet_style

class GenericSection:
    def __init__(
        self, details: List[str]
    ) -> None:
        self.details = details

    def write_bullets(self, b_style: Optional = bullet_style):
        content = [(ListItem(Paragraph(detail, b_style))) for detail in self.details]
        content_list = ListFlowable(content, bulletType='bullet')
        return content_list

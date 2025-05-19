"""
classes/qualifications.py
"""

from typing import Dict, List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle

from styles import title_style
from classes.generic_section import GenericSection

class Qualifications(GenericSection):
    def __init__(
        self, data: [],
    ) -> None:

        quals = []
        for k, v in metadata.items():
            if "_HS" in k:      # hard skills first
                quals.insert(0, v)
            elif "GIT" in k:    # git skills second
                quals.insert(1, v)
            else:               # experience highlights at the end
                quals.append(v)
        super().__init__(details=quals)  # Call the parent constructor to initialize details


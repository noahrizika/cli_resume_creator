from typing import List, Optional
from reportlab.platypus import Paragraph, ListItem, ListFlowable, Table, TableStyle

class Qualifications:

    def __init__(
        self, skill_type: str, have_fullstack: bool, have_syseng: bool, have_ml: bool
    ) -> None:
        SKILL_DESCRIPTIONS = {
            "embedded": "C/C++, Golang, Python, FreeRTOS, Distributed Systems, IP/TCP, Linux, Bash, Wireshark, GDB",
            "fullstack": "Javascript, React/Next.js, TypeScript, Tailwind, CSS, Jest, Docker, Python, PostgreSQL, C, AWS",
            "softeng": "Hard Skills:  C/C++, TypeScript, Python, Java, React/Next.js, PostgreSQL, AWS, Linux, Git, Pandas, PyTorch",
        }

        self.A_hard_skills_header = "Hard Skills"
        self.A_hard_skills = SKILL_DESCRIPTIONS.get(skill_type, "")

        self.B_git_skills_header = "CI/CD & Git"
        self.B_git_skills = "Experienced in agile workflows, automated testing, and integrating production-ready code"  # hard coded

        self.C_fullstack_header = "Full-Stack Developer"
        self.C_fullstack = (
            "Led data pipeline design and development to expand database and improve UX"
            if have_fullstack
            else ""
        )

        self.D_syseng_header = "Machine-Level Engineer"
        self.D_syseng = (
            "Built networked embedded systems with multithreading and sensor fusion"
            if have_syseng
            else ""
        )

        self.E_ml_header = "Computer Vision Engineer"
        self.E_ml = (
            "Created image classification ML model for Dartmouth biology research"
            if have_ml
            else ""
        )

        # get list of all class variables
        self.quals = [
            attr
            for attr in dir(self)
            if not callable(getattr(self, attr))
            and not attr.startswith("__")
            and not attr.endswith("_header")
        ]
        self.quals.sort()

    def write_qualifications(self, bullet_style, title_style):
        body = []
        for qualification in self.quals:
            qual = getattr(
                self, qualification
            )  # get the value of the attribute by name
            if qual == "":
                continue

            # get header
            header = getattr(self, qualification + "_header")
            header = f"<b>{header}: </b>"

            # write line
            line = ""
            line += header
            line += qual
            body.append(ListItem(Paragraph(line, bullet_style)))

        body_list = ListFlowable(body, bulletType='bullet')

        title_p = Paragraph("QUALIFICATIONS", title_style)

        return [title_p, body_list]




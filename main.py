import argparse

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate

from build_resume import build_resume

# inputs -> resume content / structure
preset = None # if user specifies preset, then auto assign vars
name = "Noah Rizika"
skill_type = "embedded"
#order = ['edu', 'exp', 'proj']
have_fullstack, have_syseng, have_ml = False, True, True
selected_educations = [3, 2, 1]
selected_experiences = [3, 2, 1]
selected_projects = [5, 4, 3]
project_url = "https://github.com/noahrizika"
filename = "test.pdf"

# initialize pdf
pagesize = letter  # 8.5 x 11 inches (standard US paper)
margin_width = 0.84
margin_top = 0.4
margin_bottom = 0.6
doc = SimpleDocTemplate(
    filename,
    pagesize=pagesize,
    leftMargin=margin_width*inch,
    rightMargin=margin_width*inch,
    topMargin=margin_top*inch,
    bottomMargin=margin_bottom*inch,
)

resume = build_resume(
    name=name,
    skill_type=skill_type,
    have_fullstack=have_fullstack,
    have_syseng=have_syseng,
    have_ml=have_ml,
    selected_experiences=selected_experiences,
    selected_projects=selected_projects,
    selected_educations=selected_educations,
    project_url=project_url,
)

doc.build(resume)

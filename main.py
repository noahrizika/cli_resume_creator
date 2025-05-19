#!/usr/bin/env python3

"""
main.py
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate

from config import update_configs 
from handle_args import get_args
from build_resume import build_resume

def main():
    args = get_args()
    update_configs(
        new_name=args['change_name'],
        new_phone_number=args['change_phone_number'],
        new_github_url=args['change_github_url'],
        new_linkedin_url=args['change_linkedin_url'],
        new_email=args['change_email'],
        new_project_url=args['change_project_url'],
        new_filepath=args['change_filepath']
    )

    # initialize pdf
    pagesize = letter  # 8.5 x 11 inches (standard US paper)
    margin_width = 0.84
    margin_top = 0.6
    margin_bottom = 0.6
    doc = SimpleDocTemplate(
        filename=args['resume_filepath'],
        pagesize=pagesize,
        leftMargin=margin_width * inch,
        rightMargin=margin_width * inch,
        topMargin=margin_top * inch,
        bottomMargin=margin_bottom * inch,
    )

    resume = build_resume(
        skill_type=args['skill_type'],
        have_fullstack=args['have_fullstack'],
        have_syseng=args['have_syseng'],
        have_ml=args['have_ml'],
        have_clearance=args["have_clearance"],
        included_sections=args['sections'],
        selected_experiences=args["selected_experiences"],
        selected_projects=args["selected_projects"],
        selected_educations=args["selected_educations"],
    )

    # maybe build in an order functionality later?
    # eg: order = ['edu', 'exp', 'proj']
    doc.build(resume)

main()

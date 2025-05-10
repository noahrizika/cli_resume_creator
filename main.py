#!/usr/bin/env python3

import os

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate

from handle_args import get_args, assign_preset
from build_resume import build_resume

def main():
    args = get_args()

    args_dict= dict()
    if args.preset:
        args_dict = assign_preset(args.preset)
        args_dict['project_url'] = 'https://github.com/noahrizika'
        args_dict['name'] = "Noah Rizika"
        args_dict['filename'] = '/Users/noahrizika/Desktop/NoahRizikaResume.pdf'
    else:
        args_dict = vars(args)

    # initialize pdf
    pagesize = letter  # 8.5 x 11 inches (standard US paper)
    margin_width = 0.84
    margin_top = 0.6
    margin_bottom = 0.6
    doc = SimpleDocTemplate(
        filename=args_dict['filename'],
        pagesize=pagesize,
        leftMargin=margin_width * inch,
        rightMargin=margin_width * inch,
        topMargin=margin_top * inch,
        bottomMargin=margin_bottom * inch,
    )

    resume = build_resume(
        name=args_dict['name'],
        skill_type=args_dict['skill_type'],
        have_fullstack=args_dict['have_fullstack'],
        have_syseng=args_dict['have_syseng'],
        have_ml=args_dict['have_ml'],
        selected_experiences=list(map(int, args_dict["selected_experiences"].split())),
        selected_projects=list(map(int, args_dict["selected_projects"].split())),
        selected_educations=list(map(int, args_dict["selected_educations"].split())),
        project_url=args_dict['project_url'],
    )

    # maybe build in an order functionality later?
    # eg: order = ['edu', 'exp', 'proj']
    doc.build(resume)

main()

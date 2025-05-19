"""
handle_args.py
"""

import argparse

from config import (
    resume_filepath,
    QUALIFICATIONS,
    EDUCATION,
    EXPERIENCES,
    PROJECTS,
    PUBLICATIONS,
    RESEARCH_EXPERIENCES,
    CONFERENCES,
)       

def assign_args(args):
    # overwrite preset args with manually set args, while excluding qualification highlights
    update_dict = vars(args)
    args_dict = assign_preset(args.preset)
    exclude_boolean_keys = {'have_fullstack', 'have_syseng', 'have_ml'}
    args_dict.update({k: v for k, v in update_dict.items() if k not in exclude_boolean_keys and (v != None or k not in args_dict)})
    for key in exclude_boolean_keys:
        args_dict[key] = update_dict[key] or args_dict[key]
    
    # clean skill_type value
    skill_type_map = {
        "e": "embedded_hs",
        "embedded": "embedded_hs",
        "embedded_hs": "embedded_hs",
        "f": "fullstack_hs",
        "fullstack": "fullstack_hs",
        "fullstack_hs": "fullstack_hs",
        "s": "softeng_hs",
        "softeng": "softeng_hs",
        "softeng_hs": "softeng_hs",
    }
    args_dict["skill_type"] = skill_type_map[args_dict["skill_type"]]

    # clean content value
    content_map = {
        "edu": EDUCATION,
        "exp": EXPERIENCES,
        "proj": PROJECTS,
        "pub": PUBLICATIONS,
        "rexp": RESEARCH_EXPERIENCES,
        "conf": CONFERENCES,
    }
    args_dict["sections"] = [content_map[section] for section in args_dict["sections"]]

    # assign filepath if unassigned
    if not args_dict["resume_filepath"]:
        # use config's filepath unless going to change config filepath
        if args_dict["change_filepath"]:
            args_dict["resume_filepath"] = args_dict["change_filepath"]
        else:
            args_dict["resume_filepath"] = resume_filepath

    return args_dict


def assign_preset(preset):
    match preset:
        case "e": # embedded
            return {
                "skill_type": "embedded_hs",
                "have_fullstack": False,
                "have_syseng": True,
                "have_ml": True,
                "sections": ["edu", "exp", "proj"],
                "selected_educations": [3, 2, 1], # midd, udacity, sec+
                "selected_experiences": [3, 2, 1], # atom, mpomp, ml
                "selected_projects": [5, 4, 3],  # drone, sysprog, sonar
            }

        case "f": # fullstack
            return {
                "skill_type": "fullstack_hs",
                "have_fullstack": True,
                "have_syseng": False,
                "have_ml": True,
                "sections": ["edu", "exp", "proj"],
                "selected_educations": [3, 2, 1], # midd, udacity, sec+
                "selected_experiences": [3, 2, 1], # atom, mpomp, ml
                "selected_projects": [5, 3, 2],  # drone, sonar, climbing
            }

        case "a": # all
            return {
                "skill_type": "e",
                "have_fullstack": True,
                "have_syseng": True,
                "have_ml": True,
                "sections": [],
                "selected_educations": [],
                "selected_experiences": [],
                "selected_projects": [],
            }

        case "n": # no preset
            return {}

        case _:
            print(f"preset not found: preset '{preset}' does not exist.")
            return {}

# TODO: create negate booleans to remove certain qualifications or selected_XXX from a preset
def get_args():
    parser = argparse.ArgumentParser(description="create a resume pdf")

    # use preset config as base resume
    parser.add_argument(
        "-p",
        "--preset",
        default="a",
        type=str,
        help='use a preset configuration. content specifications overrule preset specs (ie: "e" / "embedded", "f" / "fullstack", "a" / "all")',
    )

    # select qualifications
    parser.add_argument(
        "-sk",
        "--skill_type",
        type=str,
        help='highlight specific hard skills (ie: "e" / "embedded", "f" / "fullstack", "s" / "softeng"',
    )
    parser.add_argument(
        "-fs",
        action="store_true",
        dest="have_fullstack",
        help="includes fullstack highlight",
    )
    parser.add_argument(
        "-se",
        action="store_true",
        dest="have_syseng",
        help="include systems highlight",
    )
    parser.add_argument(
        "-ml", action="store_true", dest="have_ml", help="include ML highlight"
    )

    # select content
    parser.add_argument(
        "-s",
        "--sections",
        nargs="+",
        type=str,
        dest="sections",
        help='choose content and order (eg: "edu exp proj pub rexp conf")',
    )
    parser.add_argument(
        "--edu",
        nargs="+",
        type=int,
        dest="selected_educations",
        help='include specific educations (eg: "3 2 1")',
    )
    parser.add_argument(
        "--exp",
        nargs="+",
        type=int,
        dest="selected_experiences",
        help='include specific experiences (eg: "3 2 1")',
    )
    parser.add_argument(
        "--proj",
        nargs="+",
        type=int,
        dest="selected_projects",
        help='include specific projects (eg: "3 2 1")',
    )

    # misc
    parser.add_argument(
        "-o",
        "--filename",
        dest="resume_filepath",
        type=str,
        help="set outputted file's name",
    )
    parser.add_argument(
        "-c",
        "--have_clearance",
        action="store_true",
        help="include a final line stating you're eligible for a security clearance",
    )

    # config changes
    parser.add_argument("--change_name", type=str, help="change the name permanently")
    parser.add_argument(
        "--change_phone_number", type=str, help="change the phone number permanently"
    )
    parser.add_argument(
        "--change_github_url",
        type=str,
        help="change the github url / portfolio url permanently",
    )
    parser.add_argument(
        "--change_linkedin_url", type=str, help="change the linkedin url permanently"
    )
    parser.add_argument(
        "--change_project_url",
        type=str,
        help="change the project url permanently",
    )
    parser.add_argument("--change_email", type=str, help="change the email permanently")
    parser.add_argument(
        "--change_filepath",
        type=str,
        help="change the outputted file's name permanently",
    )

    args = parser.parse_args()
    args_dict = assign_args(args)
    return args_dict

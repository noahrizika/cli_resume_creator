import argparse

def assign_preset(preset):
    match preset:
        case 'e':
            return {
                "skill_type": "embedded",
                "have_fullstack": False,
                "have_syseng": True,
                "have_ml": True,
                "selected_educations": "3 2 1",
                "selected_experiences": "3 2 1",
                "selected_projects": "5 4 3", # drone, syseng, sonar
            }

        case 'f':
            return {
                "skill_type": "fullstack",
                "have_fullstack": True,
                "have_syseng": False,
                "have_ml": True,
                "selected_educations": "3 2 1",
                "selected_experiences": "3 2 1",
                "selected_projects": "5 3 2", # drone, sonar, climbing
            }

        case '2':
            return {
                "skill_type": "",
                "have_fullstack": True,
                "have_syseng": True,
                "have_ml": True,
                "selected_educations": "",
                "selected_experiences": "",
                "selected_projects": "", # all
            }

        case _:
            print('preset not found: preset does not exist.')
            return -1


def get_args():
    parser = argparse.ArgumentParser(description="create a resume pdf")
    parser.add_argument(
        "-p",
        "--preset",
        default="e",
        help='for a preset configuration (ie: "e" / "embedded", "f" / "fullstack")',
    )
    parser.add_argument("-n", "--name", default="Noah Rizika", help="set a name")
    parser.add_argument(
        "-s",
        "--skill_type",
        default='e',
        help='highlight specific hard skills (ie: "e" / "embedded", "f" / "fullstack", "frontend", "backend"',
    )
    parser.add_argument(
        "--fs", type=int, default=0, help="include fullstack experience (1/0)"
    )
    parser.add_argument(
        "--se", type=int, default=0, help="include systems experience (1/0)"
    )
    parser.add_argument("--ml", type=int, default=0, help="include ML experience (1/0)")
    parser.add_argument(
        "--edu", default="3 2 1", help='include specific educations (eg: "3 2 1")'
    )
    parser.add_argument(
        "--exp", default="3 2 1", help='include specific experiences (eg: "3 2 1")'
    )
    parser.add_argument(
        "--proj", default="5 4 3", help='include specific projects (eg: "3 2 1")'
    )
    parser.add_argument(
        "--proj_url",
        default="https://github.com/noahrizika",
        help='include project url to include in projects title section (ie: "1" or "0"',
    )
    parser.add_argument(
        "-o",
        "--filename",
        default="~Desktop/NoahRizikaResume.pdf",
        help="set outputted file's name",
    )

    args = parser.parse_args()
    return args

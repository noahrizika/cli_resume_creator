# CLI Resume Creator
...just turn all your resume content into JSON first -> see resume_creator/content/ for what to overwrite with your information  
(an LLM can format it for you really quickly as long as you give it the JSON structure beforehand)  

- Play around with resume_creator/styles.css as interested  
- Use '[name_of_command] -h' for help  

### Why I Made This
- Quick, custom formatted resume generation immediately 'saved' as a pdf
    - I was annoyed manually tailoring resumes to a fullstack vs backend vs etc job application 
- Edited resume content will be reflected across all future resumes
    - As a result of the first bullet point, I had many different resumes. To revise my resume style or content, I'd need to do it manually for all resumes
- Locally hosted development
    - No need for internet connection. Privacy
- Using the CLI
    - No need to launch an application, just to save a preconfigured resume as a pdf
- But...if I were to do it again, I'd just use LaTex instead of the reportlab library
    - I wasn't too familiar with LaTex before writing this program

### Steps to Install (MacOS)
1. Git clone into a filepath that would (ideally) never change
1. Change the 'resume_filepath' key in resume_creator/content/configs.json to whatever default filepath you want your resume have  
1. Create a file in /Users/[your_username]/bin/[name_of_command]
1. Name the file whatever you want the command to be called. Make sure the chosen filename is not already used as a terminal command
    - Confirm it's unused by first typing "which [name]" in terminal. It's unused if the output says '[name_of_command] not found'
1. Update this line: python3 [absoulte_path_to_resume_creator_directory]/main.py "$@"

#### Now that you know what should change, edit the below command. Then paste the edited command into your terminal
- Replace what is wrapped in brackets (ie: [ ]) with what you changed
- Remove all brackets
```

echo "#!/bin/bash\n\npython3 [absoulte_path_to_resume_creator_directory]/main.py \"$@\"" > /Users/[your_username]/bin/[name_of_command]

```

### Please add to this project as you see fit!

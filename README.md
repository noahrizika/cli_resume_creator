# CLI Resume Creator
...just turn all your resume content into JSON first -> see resume_creator/content/ for what to overwrite with your information  

- Also, change the 'resume_filepath' in resume_creator/content/configs.json to whatever filepath you want  
- Play around with resume_creator/styles.css as interested  
- Use '[name_of_command] -h' for help  

### Steps to Install (MacOS)
1. Git clone into a filepath that would (ideally) never change
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

Please add to this project as you see fit!

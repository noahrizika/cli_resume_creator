# cli resume creator
...just turn all your resume content into JSON first -> see resume_creator/content/ for what to overwrite with your information
use '[name_of_command] -h' for help

### steps
1. git clone into a filepath that shouldn't (often) change
1. create a file in /Users/[your_username]/bin/[name_of_command]
1. call the file whatever you want the shell command to be. make sure it's a unique name. check it's unique by first typing "which [name]" in terminal and ensuring the output is blank.
1. update this line: python3 [absoulte_path_to_resume_creator_directory]/main.py "$@"

#### now that you know what should change, edit this command: replace what is wrapped in brackets (ie: [ ]) with what you changed, then remove all brackets. paste the changed command in your terminal
```

echo "#!/bin/bash\n\npython3 [absoulte_path_to_resume_creator_directory]/main.py \"$@\"" > /Users/[your_username]/bin/[name_of_command]

```

please add to this project as you see fit!

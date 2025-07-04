# Project Setup and Execution Guide

## Getting Started

### Install Required Libraries
```sh
pip install -r requirement.txt
```

# You're All Not Set!
🐛 **Debug Mode Activated!** The project has bugs waiting to be squashed - your mission is to fix them and bring it to life.

## Debugging Instructions

1. **Identify the Bug**: Carefully read the code and understand the expected behavior.
2. **Fix the Bug**: Implement the necessary changes to fix the bug.
3. **Test the Fix**: Run the project and verify that the bug is resolved.
4. **Repeat**: Continue this process until all bugs are fixed.


## Here is my complete debug details for this project

I have solved the following bugs in this project:

Bug 1 : requirements.txt -> requirementsnew.txt
- I have used the uv dependency management rather than pip beause it is faster and easy to use.
- uv has automatic virtual environment creation on running the project.
- updated the requirements.txt into requirementsnew.txt to make the project compatible with the dependecies.

Bug 2 : solved the pydantic deprecation 
- removed the deprecated functions of the pydantic module.
- added the new pydantic module to make it compatible

Bug 3 : updated the import of crewai.agents module into CrewAgent in the agents.py file
- To do so, I refered the CrewAI docs and used the AI tools.
- Updated the CrewAI to >=0.130.0

Bug 4 : Fix for the Import
- (old) from crewai_tools.tools.serper_dev_tool import SerperDevTool
- (updated) from crewai_tools import SerperDevTool

Bug 5 : Used the Locally Installed LLM for API Key
- llama3.2:1b is use for the API Key
- Used the Ollama tool for local Installation and then used in the project for the API Key

Bug 6 : modifies the PDF loader function
- to reduce the laency of the post request, modifies the pdf loader function
- also modifies the class of the blood_test_report


## complete working of the project
- step 1 : Install the uv and requirementsnew.txt
- step 2 : run the project using the command "uvicorn main:app --reload"
- step 3 : Test the project on the server "http://127.0.0.1:8000/doc"

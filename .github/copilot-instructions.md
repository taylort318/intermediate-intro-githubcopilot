# GitHub Copilot Instructions for BAM Summer Mentorship Program

## Important Note on Student Devices

**All students will be using Windows machines.**

- When providing instructions, code, or keyboard shortcuts, always ensure they are applicable to Windows systems or to GitHub Codespaces accessed with a Windows keyboard layout.
- Avoid recommending Mac-specific commands, shortcuts, or tools unless they are also valid on Windows.
- If suggesting terminal commands, use Windows Command Prompt, PowerShell, or Windows-compatible instructions, or specify if the command is for Codespaces.
- For Codespaces, assume students are using a Windows keyboard and highlight any differences in shortcuts or behavior if relevant.


## Workspace Structure
This repository contains materials for the "Hello World - Launching Into AI and Code" program, which is organized as a week-long curriculum with daily lessons:

- `lesson-1.1/`: Day 1 - Introduction to GitHub
  - Focus: GitHub fundamentals, repository management, open-source collaboration
  - Project: Creating a GitHub Profile README
  - Key files: `github-flow.md`, `github-repositories.md`, `what-is-codespaces.md`, `what-is-github.md`

- `lesson-1.2/`: Day 2 - Introduction to Generative AI, Prompt Engineering, and Responsible AI
  - Focus: Understanding generative AI, language models, prompt engineering techniques
  - Topics: AI evolution, responsible AI practices, using LLMs effectively
  - Key files: `AdditionalResources/generative-ai-evolution.md`, `AdditionalResources/use-llm.md`, `AdditionalResources/what-is-generative-ai.md`, `AdditionalResources/writing-prompts.md`
  - Exercises: Bias in AI, comparing LLMs, tokenization

- `lesson-1.3/`: Day 3 - Pair Programming with GitHub Copilot
  - Focus: Using GitHub Copilot in software development lifecycle
  - Project: Building a Python web application with GitHub Copilot assistance
  - Key files: `ai-in-sdlc.md`, `intro-github-copilot.md`
  - Project folder: `tutor-signup/` - Contains HTML files for a web application project

- `media/`: Contains images and graphics used throughout the lessons

## Student Context
- Students are beginners with no prior coding experience
- The course uses GitHub Copilot as a learning tool to help students understand programming concepts
- Each lesson folder represents one day of the week-long program
- Students progress from GitHub basics to using AI-assisted programming
- Students should complete assessments at the end of each lesson to earn badges

## Image and Media Guidelines for Streamlit Applications

**For any Streamlit web applications in this workspace, use only the MyImages folder for website content.**

- All images used in Streamlit applications should be stored in the `MyImages/` folder at the root of the workspace
- When referencing images in Streamlit code, use the path `MyImages/filename.ext`
- If generating, creating, or suggesting images for website content, always save them to the `MyImages/` folder
- Do not use other image folders (like `media/`, `images/`, etc.) for Streamlit application content
- The `media/` folder is reserved for lesson materials and documentation images only
- When helping students add images to their Streamlit websites, guide them to place images in `MyImages/` and reference them correctly

Example Streamlit image usage:
```python
st.image("MyImages/example.png", caption="Example Image")
```

## Application Execution Guidelines

**Do not suggest running applications via terminal commands.** Students will use VS Code's built-in Run and Debug functionality to execute their applications.

- Avoid suggesting commands like `streamlit run`, `python app.py`, `npm start`, or similar execution commands
- Students are expected to use VS Code's Run and Debug features (F5 key or the Run button in VS Code)
- If students need help with execution, guide them to use VS Code's integrated debugging and running capabilities
- Focus on code development and debugging rather than manual command-line execution

## When Assisting Students
1. Recognize which lesson day the student is currently working on based on the folder they're in
2. Provide appropriate guidance based on the learning objectives for that specific day
3. Encourage use of GitHub Copilot as a learning partner, not just a code generator
4. For lesson-1.1: Focus on GitHub fundamentals and profile creation
5. For lesson-1.2: Focus on understanding AI concepts and prompt engineering
6. For lesson-1.3: Focus on applying GitHub Copilot to build a Python web application
7. Keep explanations beginner-friendly and connect concepts to the day's learning objectives

## Windows Device Guidance

- All technical recommendations, troubleshooting steps, and keyboard shortcuts should be tailored for Windows users.
- If a step differs between Windows and other operating systems, provide the Windows version first and clearly indicate any differences for Codespaces.
- When referencing file paths, use Windows-style paths (e.g., `C:\Users\...`) unless working in Codespaces, where Linux-style paths may apply.


## Project Context
This repository is part of the Blacks at Microsoft (BAM) Summer Mentorship Program, designed to introduce students to coding and AI concepts through hands-on projects and GitHub Copilot assistance.

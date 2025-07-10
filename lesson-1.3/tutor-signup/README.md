# Lessson 1.3 Build a Website Using GitHub Copilot

[Click here for the full program overview](https://bsmp-coders.github.io/#/2025/intermediate/lesson_summary)

In this exercise, you'll use GitHub Copilot to create a basic webpage! We want to create a website that allows students to signup for additional coaching for our program. A few requirements we were given:Build a Website Using GitHub Copilot
In this exercise, you’ll use GitHub Copilot to create a basic webpage! We want to create a website that allows students to signup for additional coaching for our program. A few requirements we were given:

- Students should enter their basic information(Name, Email, etc.)
- Students must be able to see a list of multiple options they would like to request tutoring(Python Programming, Web Design, Startup Ideas, College Application, etc.)
- Students should be able to enter their preferred days and times for coaching

### Steps
1. Open the project in GitHub Codespaces  
  - Go to [https://github.com/BSMP-Coders/intermediate-intro-githubcopilot](https://github.com/BSMP-Coders/intermediate-intro-githubcopilot)
  - Click the green "Code" button, then select "Open with Codespaces" and create a new Codespace
  - This will set up your development environment in the cloud, ready for you to start building your website

2. You’ll first need to decide what your webpage should look like. You’ll want to keep it fairly simple for this first time. Some things to note:
    - Do some research on some similar websites for inspiration.
    - If you want to learn how people create wireframes of websites, check out this article by [Skillcrush: Website Wireframe 101](https://skillcrush.com/blog/website-wireframe/)


3. Next, you'll need to sketch your webpage. There are different ways to do this, here are some options:
    - **Pen and Paper**: Draw your webpage on a piece of paper and take a picture with your phone
    - **Phone/Tablet Drawing**: Use a free drawing app like:
      - Notes app (iPhone/iPad) - Just use your finger to draw!
      - Google Keep (Android) - Has a drawing feature built in
    - **Simple Online Tools** (no signup required):
      - [Excalidraw](https://excalidraw.com/) - Free, no login needed, just start drawing!
      - [Draw.io](https://app.diagrams.net/) - Drag and drop shapes to create your layout
      - [Generate your own images with Microsoft Copilot](https://copilot.microsoft.com)
    - **Remember**: This is just a rough sketch! Think of it like drawing a blueprint - it doesn't need to be pretty, just show where things go
    - **Upload your sketch**: Once you have your drawing, save it as an image (like .png or .jpg). Then in your Codespace, right-click on the `MyImages` folder and select "Upload..." to add your sketch file

4.  Create your UI in home.py
    - Open GitHub Copilot Chat using one of these methods:
      - Press Ctrl+I on your keyboard
      - Look for the Copilot icon in the activity bar
      - Click "View" in the top menu, then find "Chat"
    - Add your sketch to the chat by clicking the paperclip icon and selecting your uploaded image
    - Write a prompt like: "Based on this sketch, create a website for a tutoring signup form with [describe your layout]"
    - Copy the generated code into your home.py file
    - Continue to refine until you get your initial design working

4.  If you noticed, maybe Copilot created everything in the home.py page.  
    - Continue to iterate on the design.  What additional functionality could you add to make it better?
    - What other things should you consider?

### Additional Prompt Ideas for adding to your website

1. Let's add some accessibility
```
Can you review the website you made and make sure that it's accessible?
``` 

2. Let's improve the visual design  
```
Can you suggest some color schemes or styles to make the website look more appealing for students?
```

3. Add form validation  
```
Can you help me add validation so users must enter a valid email address before submitting the form?
```

4. Add confirmation message  
```
Can you add a message that appears after a student submits the form to confirm their signup was successful?
```

5. Make the website mobile-friendly  
```
Can you update the website so it looks good and works well on both computers and mobile devices?
```

6. Add tooltips or help text  
```
Can you add helpful tooltips or short descriptions next to each form field to guide students on what to enter?
```

**When you are done, make sure to check-in code to your repository. (Hint - maybe Copilot could help you!)**

[Click here for the full program overview](https://bsmp-coders.github.io/#/2025/intermediate/lesson_summary)
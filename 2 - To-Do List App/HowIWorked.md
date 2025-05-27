# How I worked

## Learning Vue.js

Firstly, I didn't know any of new web frameworks, so I thought it would be a great challenge to start learning a new one.

I chose Vue.js based on how much I hear about this framework.

To learn it, I mainly based on the official documentation.

## What I did

First, I ran this command: `npm create vue@latest`

I used Visual Studio Code with the official vue extension

Then, I started only to create the designs with the tri state buttons (Todo, In progress, Done).

I faced the problem that all my tri state buttons were linked together, so i had to provide a different id and name foreach tri state button.
To do so, I used the power of Vue.js with props as I could read in the docs, and also some computed property for the id to follow the official documentation. 

Then, I created a model (a checklist and a task) to use the v- attributes to be able to display multiple tasks and multiple checklists with loops.

Furthermore, I implemented the system to CRUD tasks and checklists by linking it to the "model" (classes).

Finally, I added the local storage part to have a persistence logic.

I didn't use any AI, I only used the official documentation, and before, I read an article explaining how to build a ToDo List app in Vue JS. However, this documentation didn't help at all, because the way it was working wasn't up to my expectations. So, I decided to apply all I've read + my skills to be able to be autonomous and create an app, with maybe not the best practices, but a working app meeting the requirements and which I could be proud of.

I strongly believe that the most important part which I'm proud of is the way I managed to "learn", use the official documentation, to be able to create a working app (SFC) very simple in only a few hours. I think this shows how I'm able to adapt to different technologies and more globally to different environments.

Alongside, I also used some StackOverflow when I ran through JavaScript/HTML problems like "How to call a javascript function on radio click". I didn't want to use some AI because my goal was to showcase my skill to adapt, even for CSS.

To add some details about how I work, I also start by doing very simple ideas (starting with the design, with a MVP1, like doing the persistence at the very end). It helps doing an iterative work, working well with SCRUM methods used in some companies.

In this project, I've learnt the framework Vue.js which I didn't know anything about. The most interesting thing was, I think, the "v-" attributes idea coupled with all :prop="" providing a nice tool to do some binding (which I was struggling to make work in other projects with pure HTML/JS).

## Features

I managed to allow:
- CRUD for Checklists
- CRUD for Tasks
- Persistence
- Responsive
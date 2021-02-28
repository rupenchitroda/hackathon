# MINeD Hackathon 2021

### Investigation, Medication and Chief complaint recognition from text area box

### Problem Definition
To develop a solution, the first step is to understand the problem. Develop an NLP module to identify the keywords related to a patient's investigation, medication and chief complaint from a free text in the text box. Highlight the extracted content and feed them as input in EMR’s Chief complaint, Investigation and Medication module.

### Flow of Code
- As patient submits the story, whole description goes to views.py file in backend.
- Here necessary parts of sentence are extracted and stored in dictionary object.
- Also with other details like name and date, it is stored in ‘.csv’ file for doctor’s reference.
- Patient itself can view brief about their report.
- Doctor can view all details of patient in table format on their side.

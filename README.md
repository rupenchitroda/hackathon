# MINeD Hackathon 2021

## Investigation, Medication and Chief complaint recognition from text area box

### Problem Definition
To develop a solution, the first step is to understand the problem. Develop an NLP module to identify the keywords related to a patient's investigation, medication and chief complaint from a free text in the text box. Highlight the extracted content and feed them as input in EMR’s Chief complaint, Investigation and Medication module.

### Flow of Code
- As patient submits the story, whole description goes to views.py file in backend.
- Here necessary parts of sentence are extracted and stored in dictionary object.
- Also with other details like name and date, it is stored in ‘.csv’ file for doctor’s reference.
- Patient itself can view brief about their report.
- Doctor can view all details of patient in table format on their side.

### Steps to Execute
#### For webpage
- download the whole code
- in views.py file set the path of csv as absolute location
- run using 'py.manage.py runserver' command
- index has patient details to get input
- you will be redirected on output part after entering your details
- click doctor part on left menu to see all deatils by patient stored previously
- new entries will be available at end
#### For 5000 entries using jupyter notebook
- donwload notebook folder
- open doctor.ipynb in software like jupyter or anaconda
- goto cells at bottom of notebook, in last 4-5 cells, there will be comment of 'read data using this cell' execute that, make sure both csv file in notebook folder are there
- execute cell after that which has 'creating csv to write 5000 entries'
- same for cell below that, which will perform execution over 5000 entries  having title 'main extractor'
- execute below that to see output of new entries in dataframe
- on any issue contact me or mail me (7984675687) (rahuldsoni2001@gmail.com)
### College Details
Institute of Technology, Nirma University, Ahmedabad 
### Requirements
Django : so it is easy to use web service for all platform. You can also make API for using views.py file
no other libraries are used, we can used nlp for few purpose but that will reduce speed and we found few patterns which were easy to track so code in working with it.
we can use diseases stored in dictionary and refere that for checking but we found pattern in sentences whivh was using word like having and since whivh kind of reduces size to make comaprision.
but sure user can add their requirement by very minor modifications

### Team Details
- Rahul Soni
- Rupen Chitroda

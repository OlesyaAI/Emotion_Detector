## Disclaimer

This project is inspired by a lab exercise from the [Coursera Course: "Developing AI Application with Python and Flask tought by Abhishek Gagneja and Ramesh Sannareddy]: https://www.coursera.org/learn/python-project-for-ai-application-development/home/info

While the concepts and methodology are based on the lab, the implementation and code in this repository were written to demonstrate my understanding and skills. This project does not contain any proprietary materials or solutions provided by Coursera, and all datasets used here are either publicly available or synthetic.

If you are currently enrolled in the course, I encourage you to complete the lab exercises independently to maximize your learning experience.

# Changes commited: 11/29/2024 
# Task 1: Create an emotion detection application using the Watson NLP library (see emotion_detection.py file for code) 

# For this project,  the Emotion Predict function of the Watson NLP Library is used 
# Note that the text_to_analyze is being used as a variable that holds the actual written text that needs to be analyzed.

# 1. Create a folder in the Terminal: mkdir final_project 
# 2. Clone git repository: git clone <insert your repository url here>

# 3. Create a file named emotion_detection.py in final_project folder.
# 4. Create a file "__init__.py" and within the file state the following: 
from emotional_detection import emotion_detector 

# 5. In the emotion_detection.py file, write the function to run emotion detection using the appropriate Emotion Detection function. Name this function emotion_detector. Note: Assume that that text to be analyzed is passed to the function as an argument and is stored in the variable text_to_analyze. The value being returned must be the text attribute of the response object as received from the Emotion Detection function.

import requests # Import the requests library to handle the HTTP requests 

# Difine a function named emotion_detector that takes a string input text_to_analyze
def emotion_detector(text_to_analyze):

    # The URL of the Emotion Predict function 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with text to be analyzed 
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers required for the API requets 
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send the POST request to the API with texts and headers 
    response = requests.post(url, json = myobj, headers = Headers)

    # Return the response text from the API
    return response.text 

# 6. Import the application 
# 7. After successful import of the application, test your application in Python shell with "I love this new technology" 
from emotion_detection import emotion_detector 
emotion_detector("I love this new technology") 
# The following should be received: '{"emotionPredictions":[{"emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":26, "text":"I love this new technology"}, "emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'




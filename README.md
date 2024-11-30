## Disclaimer

This project is inspired by a lab exercise from the [Coursera Course: "Developing AI Application with Python and Flask tought by Abhishek Gagneja and Ramesh Sannareddy]: https://www.coursera.org/learn/python-project-for-ai-application-development/home/info

While the concepts and methodology are based on the lab, the implementation and code in this repository were written to demonstrate my understanding and skills. This project does not contain any proprietary materials or solutions provided by Coursera, and all datasets used here are either publicly available or synthetic.

If you are currently enrolled in the course, I encourage you to complete the lab exercises independently to maximize your learning experience.

# Changes commited: 11/30/2024 
# TASK 1: CREATE AN EMOTION DETECTION APPLICATION USING THE WATSON NLP LIBRARY (SEE THE emotion_detection.py FILE FOR CODE) 

# For this project,  the Emotion Predict function of the Watson NLP Library is used 
# Note that the text_to_analyze is being used as a variable that holds the actual written text that needs to be analyzed.

# 1.1 Create a folder in the Terminal: mkdir final_project 
# 1.2 Clone git repository: git clone <insert your repository url here>

# 1.3 Create a file named emotion_detection.py in final_project folder.
# 1.4 Create a file "__init__.py" and within the file state the following: 
from emotional_detection import emotion_detector 

# 1.5 In the emotion_detection.py file, write the function to run emotion detection using the appropriate Emotion Detection function. Name this function emotion_detector. Note: Assume that that text to be analyzed is passed to the function as an argument and is stored in the variable text_to_analyze. The value being returned must be the text attribute of the response object as received from the Emotion Detection function.

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

# 1.6 Import the application 
# 1.7 After successful import of the application, test your application in Python shell with "I love this new technology" 
    from emotion_detection import emotion_detector 
    emotion_detector("I love this new technology") 
# The following should be received: '{"emotionPredictions":[{"emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":26, "text":"I love this new technology"}, "emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'

# TASK 2: FORMAT THE OUTPUT OF THE APPLICATION 

# 2.1 Convert the response text into dictionary using json library function 
    import json 
# 2.2 Write the code logic to find the dominant emotion (see the updated code): 

import requests  # Import the requests library to handle HTTP requests
import json

>>> UPDATED CODE START >>> 
# Define a function named emotion detection that takes a string input (text_to_analyse)
    def emotion_detector(text_to_analyse): 
# URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
# Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } } 
# Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
# Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers = header)  
# Parsing the json response from the API 
    formatted_response = json.loads(response.text) 
# Extracting emotions
    emotion = formatted_response['emotionPredictions'][0]['emotion']

>>> UPDATED CODE END >>> 
    
#2.3 Test the application in Python shell again with the statement "I am so happy I am doing this" (continue this input in the same terminal): 
    >>> import json 
    >>> from emotion_detection import emotion_detector
    >>> response = emotion_detector("I am so happy I am doing this")
    >>> print(response)
    {"emotionPredictions":[{"emotion":{"anger":0.0043079085, "disgust":0.00041127237, "fear":0.0037504788, "joy":0.9918804, "sadness":0.014091322}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":29, "text":"I am so happy I am doing this"}, "emotion":{"anger":0.0043079085, "disgust":0.00041127237, "fear":0.0037504788, "joy":0.9918804, "sadness":0.014091322}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}

# TASK 3: PACKAGE THE PREVIOUSLY CREATED APPLICATION
# 3.1 Create a package folder within final_project.py folder 
    mkdir EmotionDetection
# 3.2 Move emotion_detection and __init__ files into EmotionDetection package 
    mv ./emotion_detection.py ./EmotionDetection
    mv ./__init__.py ./EmotionDetection
# 3.3 Modify the contents of __init__.py file and test the appliation within the package (inside of Python shell): 
    >>> from EmotionDetection.emotion_detection import emotion_detector
    >>> emotion_detector("I hate working long hours")
    Dominant Emotion: anger with a score of 0.64949876









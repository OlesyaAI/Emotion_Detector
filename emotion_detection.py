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

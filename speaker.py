from playsound import playsound
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('bC-lv8cLfXCtDUSfmXbftp30Nzv9lbn4dt1o4K2lO0CV')
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/06a6317d-1712-4e16-bef1-899443902386')

var="Plant quality detected: Unhealthy due to Malnutrition. The fertilizer is successfully supplied to the plant"

with open('Voice.wav', 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize(var,voice='en-US_AllisonV3Voice',accept='audio/wav').get_result().content)

playsound('/home/pi/NutriBud/Voice.wav',block=False)
print('playing Voice using speaker')

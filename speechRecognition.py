import speech_recognition as sr
import os
import time
import playsound
from gtts import gTTS
from googletrans import Translator
import sys
import arabic_reshaper
from deep_translator import GoogleTranslator

#recognize_sphinx

def speech_to_text():
    '''
    fromm is the language to be detected
    '''
    r = sr.Recognizer()
           

    with sr.Microphone() as source:
        print('Speak anything')
        audio = r.listen(source)
    
        try:
            #text = r.recognize_google(audio, config=speech.types.RecognitionConfig(profanity_filter=False))
            text = r.recognize_google(audio)
            print('You said: ' + text)
        except:
            print('sorry')
            return 'sorry'
    first =list(text.split(' '))
    new=[]
    for i in range(len(first)):
        if first[i] == 'b****':
            new.append('bitch')
            continue            
        elif first[i] == 'f***':
            new.append('fuck')
            continue
        else:
            new.append(first[i])
        
    y=''
    y = ' '.join(new)
    return y


def speak(text, src):
    '''
    src is the language to be spoken in 
    '''
    tts = gTTS(text=text, lang=src)
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    delete_mp3()
    return
    
    
def delete_mp3():
    '''
    deletes mp3 file to be able to script through command line
    '''
    os.remove('voice.mp3')
    return
    
    
def get_langs_code():
    return GoogleTranslator.get_supported_languages(as_dict=True)  


def translate(text, src, destination):
    '''
    source = source language 
    dest = destination language
    '''
    translated = GoogleTranslator(source = src, target = destination).translate(text)
    print('traslation: ' + translated)
    return translated
    
 
def reshape_arabic(text):
    '''
    -> text to be reshaped so it joins properly for viewing
    -> do not reshape for speech
    '''
    reshaped_text = arabic_reshaper.reshape(text)
    rev_text = reshaped_text[::-1]  # slice backwards 
    return rev_text


if __name__ =='__main__':
    fromm = 'de'
    too = 'en'
    
    recording = speech_to_text()
    #reshaped = reshape_arabic(recording)
    #print(reshaped)
    translated_text = translate(recording, fromm, too)
    #speak('The translation is', 'en') # always say this in english
    speak(translated_text, too)
    
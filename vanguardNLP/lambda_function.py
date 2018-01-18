"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""
from __future__ import print_function
from twilio.rest import Client
from random import randint
import pickle
import sys
import requests

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------


#
# def Preprocess(text):
#     tokens = word_tokenize(text)
#     tokens = [t.lower() for t in tokens]
#     #stops = stopwords.words('english')
#     #tokens = [t for t in tokens if t  not in stops]
#     pst = PorterStemmer()
#     tokens = [pst.stem(t) for t in tokens]
#     text = ' '.join(tokens)
#     return text
#
# def Predict(comment):
#     f = open('v.pickle','rb')
#     vectorizer = pickle.load(f)
#     f = open('m.pickle','rb')
#     model = pickle.load(f)
#
#     processedComment = Preprocess(comment)
#     X = vectorizer.transform([processedComment,]).toarray()
#     ans = int(model.predict(X))
#
#     return ans


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    global g_investment_behavior
    g_investment_behavior =''

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Vanguard AI V MAP Investment Allocation Demo. " \
                    "Tell me about your investment behavior"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Tell me about your investment behavior"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def Collect_investment_behavior(intent, session):
    global g_investment_behavior
    
    card_title = intent['name']

    session_attributes = {}
    investment_behavior = intent['slots']['investment']['value']
    #investment_behavior = intent['slots']['investment']

    print ("investment behavor is " + str(list(iter(investment_behavior))))
    #print ("investment behavor name is " + str(list(iter(investment_behavior['name']))))

    g_investment_behavior = g_investment_behavior +' '+ investment_behavior

    speech_output = "Okay, what else ? "

    # do some thing
    reprompt_text = ""
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def end_question_behavior(intent, session):

    card_title = intent['name']

    session_attributes = {}

    global g_investment_behavior

    speech_output = "Okay, let me read back your investment behavior "+ g_investment_behavior

    r = requests.post('http://54.173.193.196:5001/clsfy', data = {'textinput':g_investment_behavior})

    prediction = r.json()['y']

    print ("Prediction is" + str(prediction))

    if prediction == -1:
        print('conservative')
        speech_output = "Okay, let me read back your investment behavior "+ g_investment_behavior + " . And you seem to be a conservative investor. "

    if prediction == 1:
        print('aggressive')
        speech_output = "Okay, let me read back your investment behavior "+ g_investment_behavior + " . And you seem to be an aggressive investor. "
    # do some thing
    reprompt_text = ""
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



def send_key(intent, session):
    card_title = intent['name']

    account_sid = "ACa35ea580c7f4e30d2f4aaa3eed3c2fe6"
    # Your Auth Token from twilio.com/console
    auth_token  = "94f09ea764f53f2448f7cf4d0a487043"

    should_end_session = True
    session_attributes = {}

    global mKey

    mKey=random_with_N_digits(4)

    try:
        client = Client(account_sid, auth_token)

        # message = client.messages.create(
        #     to="+17735587753",
        #     from_="+12242573280",
        #     body="Hello from Python!")

        #client = Client(account_sid, auth_token)

        client.api.account.messages.create(
            to="+17735587753",
            from_="+12242573280",
            body="Your authetication code generated by Vanguard is " + str(mKey) + "  Please verify this with Vanguard Alexa app")


    except (RuntimeError, TypeError, NameError):
        speech_output = "I am sorry, there is some technical issues sending you the code."
        return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

    speech_output = "The code has been sent to your mobile number registered in your account.  Please verify that code with me when you are ready. "
    reprompt_text = ""

    should_end_session = False

    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def verify_key(intent, session):
    global mKey

    card_title = intent['name']

    session_attributes = {}
    aKey = intent['slots']['authenticationcode']['value']

    print('The key is '+str(aKey))

    if (aKey == mKey):
        speech_output = "You have successfully authenticated yourself. "
    else:
        speech_output = "Sorry, your authentication code is incorrect. "


    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))



def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Vanguard Virtual Assitant. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))




# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "generateKey":
        return send_key(intent, session)
    elif intent_name =="end_of_behavior":
        return end_question_behavior(intent, session)
    elif intent_name == "investment_behavior":
        return Collect_investment_behavior(intent, session)
    # elif intent_name == "SendPicture":
    #     return sendpicture(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
        

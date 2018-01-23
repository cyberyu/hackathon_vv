"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""
from __future__ import print_function
import json as JSON


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
        'shouldEndSession': should_end_session,

    }



def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------


def create_previous_intent_attribute(intent_name):
    return {"previous_intent": intent_name}

def create_name_attribute(my_name):
    return {"name": my_name}

def create_age_attribute(my_age):
    return {"age": my_age}

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    global g_investment_behavior, session_attributes
    g_investment_behavior =''

    session_attributes = {}
    session_attributes['previous_intent'] = 'welcome'

    card_title = "Welcome"
    speech_output = "Welcome to Session Test.  What is your name?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Welcome to Session Test.  What is your name? "
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



def get_name(intent, session):

    card_title = "What is your name"

    my_name = intent['slots']['name']['value']

    if session.get('attributes', {}) and "previous_intent" not in session.get('attributes', {}):
        session_attributes.update(create_previous_intent_attribute('get_name'))
    elif  "previous_intent" in session.get('attributes', {}):
        session_attributes.update(create_previous_intent_attribute('get_name'))
    else:
        print("not found session attributes")


    if session.get('attributes', {}) and "name" not in session.get('attributes', {}):
        session_attributes.update(create_name_attribute(my_name))
    elif "name" in session.get('attributes', {}):
        session_attributes.update(create_name_attribute(my_name))
    else:
        print("not found session attributes")

    speech_output = "Thank you, may I confirm that your name is " + my_name + " ?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Thank you, may I confirm that your name is " + my_name + " ?"
    should_end_session = False


    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def confirm_name(intent, session):

    card_title = "confirm the name"

    my_name ="Unknown"

    if session.get('attributes', {}) and "name" in session.get('attributes', {}):
        my_name = session['attributes']['name']

    if session.get('attributes', {}) and "previous_intent" not in session.get('attributes', {}):
        session_attributes.update(create_previous_intent_attribute('confirm_name'))
    elif  "previous_intent" in session.get('attributes', {}):
        session_attributes.update(create_previous_intent_attribute('confirm_name'))
    else:
        print("not found session attributes")

    reprompt_text = "Thank you, " +  my_name + " may I ask how old are you?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    speech_output = "Thank you, " +  my_name + " may I ask how old are you?"
    should_end_session = False


    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



def ask_age(intent, session):

    card_title = "confirm the age"

    if session.get('attributes', {}) and "previous_intent" not in session.get('attributes', {}):
        session_attributes.update(create_previous_intent_attribute('ask_age'))
    elif  "previous_intent" in session.get('attributes', {}):
        session_attributes.update(create_previous_intent_attribute('ask_age'))
    else:
        print("not found session attributes")


    my_age = intent['slots']['age']['value']


    if session.get('attributes', {}) and "age" not in session.get('attributes', {}):
        session_attributes.update(create_age_attribute(my_age))
    elif "age" in session.get('attributes', {}):
        session_attributes.update(create_name_attribute(my_age))
    else:
        print("not found session attributes")


    if session.get('attributes', {}) and "previous_intent" not in session.get('attributes', {}):
        session_attributes.update(create_previous_intent_attribute('get_name'))

    my_name ="Unknown"

    if session.get('attributes', {}) and "name" in session.get('attributes', {}):
        my_name = session['attributes']['name']


    reprompt_text = "Thank you " + my_name+" , may I confirm that your age is " + my_age + " ?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    speech_output = "Thank you "  + my_name +" , may I confirm that your age is " + my_age + " ?"
    should_end_session = False


    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



def confirm_age(intent, session):


    card_title = "I got it"

    my_name ="Unknown"

    if session.get('attributes', {}) and "name" in session.get('attributes', {}):
        my_name = session['attributes']['name']

    my_age =0

    if session.get('attributes', {}) and "age" in session.get('attributes', {}):
        my_age = session['attributes']['age']

    reprompt_text = "Thank you I got it. Your name is " + my_name + " and you are " +str(my_age) + " years old. "
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    speech_output = "Thank you I got it. Your name is " + my_name + " and you are " +str(my_age) + " years old. "
    should_end_session = False


    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying Session Test. " \
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

    # global session_attributes
    #
    # p_node = ""
    #
    # try:
    #     print("session previous node name is " + session_attributes['previous_node'])
    #     p_node = session_attributes['previous_node']
    #
    # except KeyError:
    #     print("No previous node yet")
    #
    # print("on_intent requestId=" + intent_request['requestId'] +
    #       ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']


    p_intent = ''

    if (session.get('attributes', {})) and ("previous_intent" in session.get('attributes', {})):
        p_intent = session['attributes']['previous_intent']


    # Dispatch to your skill's intent handlers
    if intent_name=="get_name":
        return get_name(intent, session)
    elif intent_name=="ask_age":
        return ask_age(intent, session)
    elif (intent_name=="general_confirm") and (p_intent=='get_name'):
        return confirm_name(intent, session)
    elif (intent_name=="general_confirm") and (p_intent=='ask_age'):
        return confirm_age(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "Stop":
        return handle_session_end_request()

    else:
        raise ValueError("Invalid intent")



def on_intent_name(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    # global session_attributes
    #
    # p_node = ""
    #
    # try:
    #     print("session previous node name is " + session_attributes['previous_node'])
    #     p_node = session_attributes['previous_node']
    #
    # except KeyError:
    #     print("No previous node yet")
    #
    # print("on_intent requestId=" + intent_request['requestId'] +
    #       ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    #
    print ("intent name is " + intent_name)


    # Dispatch to your skill's intent handlers
    if intent_name=="get_name":
        return get_name(intent, session)
    elif intent_name=="ask_age":
        return ask_age(intent, session)
    elif intent_name=="confirm_name":
        return confirm_name(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "Stop":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")



def on_intent_age(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    # global session_attributes
    #
    # p_node = ""
    #
    # try:
    #     print("session previous node name is " + session_attributes['previous_node'])
    #     p_node = session_attributes['previous_node']
    #
    # except KeyError:
    #     print("No previous node yet")
    #
    # print("on_intent requestId=" + intent_request['requestId'] +
    #       ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    #
    # print ("intent name is " + intent_name + " and pnode is " + p_node)


    # Dispatch to your skill's intent handlers
    if intent_name=="get_name":
        return get_name(intent, session)
    elif intent_name=="ask_age":
        return ask_age(intent, session)
    elif intent_name == "confirm_age":
        return confirm_age(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "Stop":
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





# def body_template(intent, session):
#
#     card_title = intent['name']
#
#     session_attributes = {}
#
#     number = intent['slots']['templateNum']['value']
#
#
#     print("slot filling body_template {}".format(number))
#
#     if number == "1":
#         return body_template_one()
#     elif number == "2":
#         return body_template_two()
#     elif number == "3":
#         return body_template_three()
#     elif number == "6":
#         return body_template_six()
#
#     #return help()



# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """

    print("===EVENT=== \n"+ JSON.dumps(event))

    my_session = event['session']
    p_intent = ''

    if (my_session.get('attributes', {})) and ("previous_intent" in my_session.get('attributes', {})):
        p_intent = my_session['attributes']['previous_intent']

    print ('p_intent ' + p_intent)


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
        # try to grab the session object
        # my_session = event['session']
        # if p_intent=='get_name':
        #     return on_intent_name(event['request'], event['session'])
        # elif p_intent=='get_age':
        #     return on_intent_age(event['request'], event['session'])
        # else:
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


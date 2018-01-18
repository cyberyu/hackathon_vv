/**
    Copyright 2016 Greg Yeutter. Code is modified from example code provided by Amazon.com, Inc.

    Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

        http://aws.amazon.com/apache2.0/

    or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
*/

/**
 * This skill has Alexa repeat a short phrase given by the user
 * 
 * For example:
 * User: Alexa, ask repeat this to repeat 'the meaning of life'
 * Alexa: 'the meaning of life'
 */


/**
 * App ID for the skill
 */
var APP_ID = undefined; //replace with 'amzn1.echo-sdk-ams.app.[your-unique-value-here]';

var https = require('https');

/**
 * The AlexaSkill Module that has the AlexaSkill prototype and helper functions
 */
var AlexaSkill = require('./AlexaSkill');

/**
 * RepeatThisSkill is a child of AlexaSkill.
 */
var RepeatThisSkill = function() {
    AlexaSkill.call(this, APP_ID);
};

// Extend AlexaSkill
RepeatThisSkill.prototype = Object.create(AlexaSkill.prototype);
RepeatThisSkill.prototype.constructor = RepeatThisSkill;

RepeatThisSkill.prototype.eventHandlers.onSessionStarted = function (sessionStartedRequest, session) {
    console.log("RepeatThisSkill onSessionStarted requestId: " + sessionStartedRequest.requestId
        + ", sessionId: " + session.sessionId);

    // any session init logic would go here
};

RepeatThisSkill.prototype.eventHandlers.onLaunch = function (launchRequest, session, response) {
    console.log("RepeatThisSkill onLaunch requestId: " + launchRequest.requestId + ", sessionId: " + session.sessionId);
    getWelcomeResponse(response);
};

RepeatThisSkill.prototype.eventHandlers.onSessionEnded = function (sessionEndedRequest, session) {
    console.log("onSessionEnded requestId: " + sessionEndedRequest.requestId
        + ", sessionId: " + session.sessionId);

    // any session cleanup logic would go here
};

RepeatThisSkill.prototype.intentHandlers = {

    "RepeatIntent": function (intent, session, response) {
        handleFirstEventRequest(intent, session, response);
    },

    "AMAZON.HelpIntent": function (intent, session, response) {
        var speechText = "Repeat This repeats a short phrase you specify.  " +
            "For example, you could say the meaning of life is 42 and I would say the meaning of life is 42. " + 
            "Now, what would you like me to repeat?";
        var repromptText = "What would you like me to say?";
        var speechOutput = {
            speech: speechText,
            type: AlexaSkill.speechOutputType.PLAIN_TEXT
        };
        var repromptOutput = {
            speech: repromptText,
            type: AlexaSkill.speechOutputType.PLAIN_TEXT
        };
        response.ask(speechOutput, repromptOutput);
    },

    "AMAZON.StopIntent": function (intent, session, response) {
        var speechOutput = {
                speech: "Goodbye",
                type: AlexaSkill.speechOutputType.PLAIN_TEXT
        };
        response.tell(speechOutput);
    },

    "AMAZON.CancelIntent": function (intent, session, response) {
        var speechOutput = {
                speech: "Goodbye",
                type: AlexaSkill.speechOutputType.PLAIN_TEXT
        };
        response.tell(speechOutput);
    },

    "AMAZON.PauseIntent": function (intent, session, response) {
        var speechOutput = {
                speech: "Goodbye",
                type: AlexaSkill.speechOutputType.PLAIN_TEXT
        };
        response.tell(speechOutput);
    }
};

/**
 * Function to handle the onLaunch skill behavior
 */
function getWelcomeResponse(response) {
    // If we wanted to initialize the session to have some attributes we could add those here.
    var cardTitle = "Repeat This";
    var repromptText = "Repeat This repeats a short phrase you specify.  " +
            "For example, you could say the meaning of life is 42 and I would say the meaning of life is 42. " + 
            "Now, what would you like me to repeat?";
    var speechText = "<p>Repeat This.</p> <p>What would you like me to say?</p>";
    var cardOutput = "Repeat This. What would you like me to say?";
    // If the user either does not reply to the welcome message or says something that is not
    // understood, they will be prompted again with this text.

    var speechOutput = {
        speech: "<speak>" + speechText + "</speak>",
        type: AlexaSkill.speechOutputType.SSML
    };
    var repromptOutput = {
        speech: repromptText,
        type: AlexaSkill.speechOutputType.PLAIN_TEXT
    };
    response.askWithCard(speechOutput, repromptOutput, cardTitle, cardOutput);
}

/**
 * Gets a poster prepares the speech to reply to the user.
 */
function handleFirstEventRequest(intent, session, response) {
    var repromptText = "Repeat This repeats a short phrase you specify.  " +
            "For example, you could say the meaning of life is 42 and I would say the meaning of life is 42. " + 
            "Now, what would you like me to repeat?"

    var input = intent.slots.input.value;
    
    var sessionAttributes = {};

    var prefixContent = "<p>Your phrase: </p>";
    var cardContent = "Your phrase: ";

    var cardTitle = "Repeat This";

    // sessionAttributes.text = input;
    // session.attributes = sessionAttributes;

    speechText = input;
    cardContent = speechText;

    response.tell(speechText);
    response.askWithCard(speechOutput, repromptOutput, cardTitle, cardContent);
}

// Create the handler that responds to the Alexa Request.
exports.handler = function (event, context) {
    // Create an instance of the RepeatThis Skill.
    var skill = new RepeatThisSkill();
    skill.execute(event, context);
};
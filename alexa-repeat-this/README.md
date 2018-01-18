# Repeat This Alexa Skill

Repeat This is a simple skill for [Amazon Alexa](https://developer.amazon.com/alexa) (e.g. Echo) that repeats any phrase spoken by the user. 

For example:
* User: "Alexa, ask Repeat This to repeat 'we are the music makers'"
* Alexa: "We are the music makers"
* User: "Alexa, ask Repeat This 'we are the dreamers of dreams'"
* Alexa: "We are the dreamers of dreams"
* User: "Alexa, ask Repeat This to say 'come along'"
* Alexa: "Come along"

Repeat This demonstrates Alexa's natural language recognition capabilities. The input query is passed as one or more Strings to Alexa's text-to-speech engine. The code could be modified to pass the input query to another web service, giving Alexa superpowers.

This skill cannot be submitted to the Skills Store because it uses the deprecated AMAZON.LITERAL slot type, which Amazon [no longer allows](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-interaction-model-reference#literal-slot-type-reference) in public skills. However, you can upload it for personal use on AWS Lambda.

Repeat This is released under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0), which gives you the freedom to use the software for any purpose, distribute it, modify it, and distribute modified versions. No warranty is provided.

For more interesting projects, visit my [website](https://gregyeutter.com/).
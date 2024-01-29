"""Ask a question to GPT."""
from .config import baseConf
from .conversation import Conversation
from .OwegaFun import existingFunctions, connectLTS, functionlist_to_toollist
import time
import openai
import json5 as json
import re
from .utils import debug_print


def convert_invalid_json(invalid_json):
    """
    Try converting invalid json to valid json.

    Sometimes, GPT will give back invalid json.
    This function tries to make it valid.
    """
    def replace_content(match):
        content = match.group(1)
        content = (
            content
            .replace('"', '\\"')
            .replace("\n", "\\n")
        )
        return f'"{content}"'
    valid_json = re.sub(r'`([^`]+)`', replace_content, invalid_json)
    return valid_json


# ask openAI a question
# TODO: comment a lot more
def ask(
    prompt: str = "",
    messages: Conversation = Conversation(),
    model=baseConf.get("model", ""),
    temperature=baseConf.get("temperature", 0.8),
    max_tokens=baseConf.get("max_tokens", 3000),
    function_call="auto",
    temp_api_key="",
    temp_organization="",
    top_p=baseConf.get("top_p", 1.0),
    frequency_penalty=baseConf.get("frequency_penalty", 0.0),
    presence_penalty=baseConf.get("presence_penalty", 0.0),
):
    """Ask OpenAI a question."""
    if baseConf.get("debug", False):
        bc = baseConf.copy()
        bc["api_key"] = "REDACTED"
        debug_print(f"{bc}", True)
    connectLTS(messages.add_memory, messages.remove_memory, messages.edit_memory)
    old_api_key = openai.api_key
    old_organization = openai.organization
    if (prompt):
        messages.add_question(prompt)
    else:
        prompt = messages.last_question()
    if isinstance(function_call, bool):
        if function_call:
            function_call = "auto"
        else:
            function_call = "none"
    response = False
    while (not response):
        try:
            if (temp_api_key):
                openai.api_key = temp_api_key
            if (temp_organization):
                openai.organization = temp_organization
            response = openai.chat.completions.create(
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                messages=messages.get_messages(),
                tools=functionlist_to_toollist(
                    existingFunctions.getEnabled()),
                tool_choice=function_call,
            )
            if (temp_api_key):
                openai.api_key = old_api_key
            if (temp_organization):
                openai.organization = old_organization
        except openai.BadRequestError:
            messages.shorten()
        except openai.InternalServerError:
            print("[Owega] Service unavailable...", end="")
            time.sleep(1)
            print(" Retrying now...")
    # do something with the response
    message = response.choices[0].message
    while message.tool_calls is not None:
        try:
            for tool_call in message.tool_calls:
                tool_function = tool_call.function
                function_name = tool_function.name
                try:
                    kwargs = json.loads(tool_function.arguments)
                except json.decoder.JSONDecodeError:
                    unfixed = tool_function.arguments
                    fixed = convert_invalid_json(unfixed)
                    kwargs = json.loads(fixed)
                function_response = \
                    existingFunctions.getFunction(function_name)(**kwargs)
                messages.add_function(function_name, function_response)
            response2 = False
            while not (response2):
                try:
                    if (temp_api_key):
                        openai.api_key = temp_api_key
                    if (temp_organization):
                        openai.organization = temp_organization
                    response2 = openai.chat.completions.create(
                        model=model,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        top_p=top_p,
                        frequency_penalty=frequency_penalty,
                        presence_penalty=presence_penalty,
                        messages=messages.get_messages(),
                        tools=functionlist_to_toollist(
                            existingFunctions.getEnabled()),
                        tool_choice=function_call,
                    )
                    if (temp_api_key):
                        openai.api_key = old_api_key
                    if (temp_organization):
                        openai.organization = old_organization
                except openai.error.InvalidRequestError:
                    messages.shorten()
                except openai.error.ServiceUnavailableError:
                    print("[Owega] Service unavailable...", end="")
                    time.sleep(1)
                    print(" Retrying now...")
                message = response2.choices[0].message
        except Exception as e:
            print("Exception: " + str(e))
            print(message.tool_calls[0].function.name)
            print(message.tool_calls[0].function.arguments)
            break
    try:
        messages.add_answer(message.content.strip())
    except Exception as e:
        print("Exception: " + str(e))
    return messages

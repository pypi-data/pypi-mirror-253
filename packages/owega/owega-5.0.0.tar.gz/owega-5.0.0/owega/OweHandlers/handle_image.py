"""Handle /image."""
import openai
import tempfile
import prompt_toolkit as pt
from ..utils import (
    info_print,
    estimated_tokens,
    clrtxt,
    play_opus,
)
from ..OwegaSession import OwegaSession as ps
from ..config import baseConf
from ..OwegaFun import existingFunctions, functionlist_to_toollist
import time
from ..ask import ask


def handle_image(temp_file, messages, given="", temp_is_temp=False):
    """Handle /image."""
    given = given.strip()
    given = given.split(' ')[0]
    if given:
        image_url = given
    else:
        image_url = ps['main'].prompt(pt.ANSI(
            clrtxt("yellow", " IMAGE URL ") + ": ")).strip()
    image_urls = [image_url]
    user_prompt = ps['main'].prompt(pt.ANSI(
        clrtxt("yellow", " PRE-FILE PROMPT ") + ": ")).strip()
    if baseConf.get("estimation", False):
        etkn = estimated_tokens(
            "",
            messages,
            functionlist_to_toollist(existingFunctions.getEnabled())
        )
        cost_per_token = (
            0.03
            if 'gpt-4' in baseConf.get("model", "")
            else 0.003
        ) / 1000
        cost = cost_per_token * etkn
        print(f"\033[37mestimated tokens: {etkn}\033[0m")
        print(f"\033[37mestimated cost: {cost:.5f}\033[0m")
    if baseConf.get("debug", False):
        pre_time = time.time()
    messages.add_image(user_prompt, image_urls)
    messages = ask(
        prompt=None,
        messages=messages,
        model=baseConf.get("model", ""),
        temperature=baseConf.get("temperature", 0.8),
        max_tokens=baseConf.get("max_tokens", 3000),
        top_p=baseConf.get("top_p", 1.0),
        frequency_penalty=baseConf.get("frequency_penalty", 0.0),
        presence_penalty=baseConf.get("presence_penalty", 0.0)
    )
    if baseConf.get("debug", False):
        post_time = time.time()
        print(f"\033[37mrequest took {post_time-pre_time:.3f}s\033[0m")
    print()
    print(' ' + clrtxt("magenta", " Owega ") + ": ")
    print()
    print(messages.last_answer())
    if baseConf.get('tts_enabled', False):
        tmpfile = tempfile.NamedTemporaryFile(
            prefix="owegatts.",
            suffix=".opus",
            delete=False
        )
        tmpfile.close()
        tts_answer = openai.audio.speech.create(
            model='tts-1',
            voice='nova',
            input=messages.last_answer()
        )
        if baseConf.get("debug", False):
            posttts_time = time.time()
            print(f"\033[37mrequest took {posttts_time-pre_time:.3f}s\033[0m")
        tts_answer.stream_to_file(tmpfile.name)
        play_opus(tmpfile.name)
    return messages


item_image = {
    "fun": handle_image,
    "help": "sends a prompt and an image from an url",
    "commands": ["image"],
}

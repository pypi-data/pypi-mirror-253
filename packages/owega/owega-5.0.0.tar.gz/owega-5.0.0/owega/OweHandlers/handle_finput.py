"""Handle /file_input."""
import os
import time
import tempfile
import openai
import prompt_toolkit as pt
from ..config import baseConf
from ..utils import (
    clrtxt,
    estimated_tokens,
    info_print,
    play_opus,
)
from ..ask import ask
from ..OwegaFun import existingFunctions, functionlist_to_toollist
from ..OwegaSession import OwegaSession as ps


def guess_language(file_path: str) -> str:
    """Try to guess the file's [programming] language."""
    filename = file_path.split('/')[-1].lower()
    if 'iptables' in filename:
        return 'iptables'
    if 'makefile' in filename:
        return 'makefile'

    ext = filename.split('.')[-1]

    known_exts = {}

    def add_exts(lang: str, exts) -> None:
        if isinstance(exts, str):
            known_exts[exts] = lang.lower()
        else:
            for ext in exts:
                known_exts[ext] = lang.lower()

    def add_sexts(langs) -> None:
        if isinstance(langs, str):
            known_exts[langs] = langs.lower()
        else:
            for lang in langs:
                known_exts[lang] = lang.lower()

    add_exts('brainfuck', ['brainfuck', 'bf'])
    add_exts('c', ['c', 'h'])
    add_exts(
        'cpp',
        ['cpp', 'cxx', 'c++', 'cc', 'hpp', 'hxx', 'h++', 'hh']
    )
    add_exts('csharp', 'cs')
    add_exts('clojure', ['clojure', 'clj'])
    add_exts('diff', ['diff', 'patch'])
    add_exts('dos', ['dos', 'bat', 'cmd'])
    add_exts('elixir', ['elixir', 'ex', 'exs'])
    add_exts('erlang', ['erlang', 'erl'])
    add_exts('fortran', ['fortran', 'f90', 'f95'])
    add_exts('golang', 'go')
    add_exts('xml',
        ['xml', 'rss', 'atom', 'xjb', 'xsd', 'xsl', 'plist', 'svg'])
    add_exts('haskell', ['haskell', 'hs'])
    add_exts('haxe', ['haxe', 'hx'])
    add_exts('julia', ['julia', 'jl'])
    add_exts('kotlin', ['kotlin', 'kt'])
    add_exts('makefile', ['mk', 'mak', 'make', 'makefile'])
    add_exts('markdown', ['markdown', 'md', 'mkdown', 'mkd'])
    add_exts('mirc', ['mirc', 'mrc'])
    add_exts('nim', ['nim', 'nimrod'])
    add_exts('ocaml', ['ocaml', 'ml'])
    add_exts('objc',
        ['objectivec', 'mm', 'objc', 'obj-c', 'obj-c++', 'objective-c++'])
    add_exts('openscad', ['openscad', 'scad'])
    add_exts('perl', ['perl', 'pl', 'pm'])
    add_exts('pgsql', ['pgsql', 'postgres', 'postgresql'])
    add_exts('powershell', ['powershell', 'ps', 'ps1'])
    add_exts('puppet', ['puppet', 'pp'])
    add_exts('python', ['python', 'py', 'gyp'])
    add_exts('rpm', ['rpm-specfile', 'rpm', 'spec', 'rpm-spec', 'specfile'])
    add_exts('ruby', ['ruby', 'rb', 'gemspec', 'podspec', 'thor', 'irb'])
    add_exts('rust', ['rust', 'rs'])
    add_exts('scilab', ['scilab', 'sci'])
    add_exts('tcl', ['tcl', 'tk'])
    add_exts('typescript', ['typescript', 'ts', 'tsx', 'mts', 'cts'])
    add_exts('verilog', ['verilog', 'v'])
    add_exts('yaml', ['yaml', 'yml'])
    add_sexts([
        'ada', 'ino', 'awk', 'sh', 'bash', 'zsh', 'basic', 'bbcode', 'blade',
        'bnf', 'bqn', 'cmake', 'cobol', 'coq', 'csp', 'css', 'd', 'dart',
        'fix', 'gcode', 'gdscript', 'gradle', 'graphql', 'gsql', 'html',
        'xhtml', 'haml', 'hlsl', 'ini', 'toml', 'json', 'java', 'js', 'jsx',
        'tex', 'leaf', 'less', 'lisp', 'lua', 'matlab', 'nix', 'oak', 'ocl',
        'glsl', 'pf', 'php', 'parser3', 'processing', 'prolog', 'properties',
        'qml', 'r', 'sas', 'scss', 'sql', 'scala', 'scheme', 'sfz', 'smali',
        'spl', 'svelte', 'swift', 'thrift', 'toit', 'tp', 'tsql', 'vbnet',
        'vb', 'vba', 'vbscript', 'vbs', 'vhdl', 'vala'
    ])

    lang = known_exts.get(ext.lower(), '')

    if not lang:
        if 'vim' in filename:
            return 'vim'

    return lang


# get input from a file instead of the terminal
def handle_finput(temp_file, messages, given="", temp_is_temp=False):
    """Handle /file_input."""
    given = given.strip()
    given = given.split(' ')[0]
    if given:
        file_path = given
    else:
        file_path = ps['load'].prompt(pt.ANSI(
            clrtxt("yellow", " FILE LOCATION ") + ": ")).strip()
    if (os.path.exists(file_path)):
        user_prompt = ps['main'].prompt(pt.ANSI(
            clrtxt("yellow", " PRE-FILE PROMPT ") + ": ")).strip()
        with open(file_path, "r") as f:
            language = guess_language(file_path)
            file_contents = f.read()
            full_prompt = \
                f"{user_prompt}\n```{language}\n{file_contents}\n```\n"
            if baseConf.get("estimation", False):
                etkn = estimated_tokens(
                    full_prompt,
                    messages,
                    functionlist_to_toollist(existingFunctions.getEnabled())
                )
                cost_per_token = [0.001, 0.002]  # prices for gpt3-turbo
                if 'gpt-4' in baseConf.get('model', ''):
                    cost_per_token = [0.03, 0.06]  # prices for gpt4
                    if 'preview' in baseConf.get('model', ''):
                        cost_per_token = [0.01, 0.03]  # prices for gpt4-turbo
                cost_per_token = [i/1000 for i in cost_per_token]
                cost = (cost_per_token[0] * etkn) + (4096 * cost_per_token[1])
                print(f"\033[37mestimated tokens: {etkn}\033[0m")
                print(f"\033[37mestimated cost: {cost:.5f}\033[0m")
            if baseConf.get("debug", False):
                pre_time = time.time()
            messages = ask(
                prompt=full_prompt,
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
                os.remove(tmpfile.name)
    else:
        info_print(f"Can't access {file_path}")
    return messages


item_finput = {
    "fun": handle_finput,
    "help": "sends a prompt and a file from the system",
    "commands": ["file_input"],
}

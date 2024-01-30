"""Handle /edit."""
import editor
import prompt_toolkit as pt
from ..utils import (
    info_print,
    clrtxt,
)
from ..OwegaSession import OwegaSession as ps


def handle_edit(temp_file, messages, given="", temp_is_temp=False):
    """Handle /edit."""
    ids = []
    for msg_id, msg in enumerate(messages.messages):
        if isinstance(msg.get('content', ''), str):
            ids.append(msg_id)
            role = msg.get('role', 'unknown')
            if role == 'user':
                print(f"[\033[0;93mUSER\033[0m] [\033[0;92m{msg_id}\033[0m]:")
                print('\033[0;37m', end='')
                print(
                    msg.get('content', '')
                    .encode('utf16', 'surrogatepass')
                    .decode('utf16')
                )
                print('\033[0m', end='')
                print()
            elif role == 'system':
                print(f"[\033[0;95mSYSTEM\033[0m] [\033[0;92m{msg_id}\033[0m]:")
                print('\033[0;37m', end='')
                print(
                    msg.get('content', '')
                    .encode('utf16', 'surrogatepass')
                    .decode('utf16')
                )
                print('\033[0m', end='')
                print()
            elif role == 'assistant':
                print(f"[\033[0;96mOWEGA\033[0m] [\033[0;92m{msg_id}\033[0m]:")
                print('\033[0;37m', end='')
                print(
                    msg.get('content', '')
                    .encode('utf16', 'surrogatepass')
                    .decode('utf16')
                )
                print('\033[0m', end='')
                print()
    try:
        msg_id = ps['integer'].prompt(pt.ANSI(
            '\n' + clrtxt("magenta", " message ID ") + ': ')).strip()
    except (ValueError, KeyboardInterrupt, EOFError):
        info_print("Invalid message ID, cancelling edit")
        return messages

    msg_id = int(msg_id)

    if msg_id not in ids:
        info_print("Invalid message ID, cancelling edit")
        return messages

    try:
        new_msg = editor.edit(
            contents=messages.messages[msg_id].get('content', '').encode(
                'utf16', 'surrogatepass')
        ).decode('utf16')
    except UnicodeDecodeError:
        info_print("Error handling given message, edit not saved")
        return messages
    if new_msg:
        messages.messages[msg_id]['content'] = new_msg
    else:
        info_print("Message empty, deleting it...")
        messages.messages.pop(msg_id)

    return messages


item_edit = {
    "fun": handle_edit,
    "help": "edits the history",
    "commands": ["edit"],
}

"""Handle /estimation."""
from ..config import baseConf
from ..utils import info_print
from ..OwegaSession import OwegaSession as ps


# enables/disables command execution
def handle_estimation(temp_file, messages, given="", temp_is_temp=False):
    """Handle /estimation."""
    if given.lower() in ["on", "true", "enable", "enabled"]:
        baseConf["estimation"] = True
        info_print("Token estimation enabled.")
        return messages

    if given.lower() in ["off", "false", "disable", "disabled"]:
        baseConf["estimation"] = False
        info_print("Token estimation disabled.")
        return messages

    baseConf["estimation"] = (not baseConf.get("estimation", False))
    if baseConf.get("estimation", False):
        info_print("Token estimation enabled.")
    else:
        info_print("Token estimation disabled.")
    return messages


item_estimation = {
    "fun": handle_estimation,
    "help": "toggles displaying the token estimation",
    "commands": ["estimation"],
}

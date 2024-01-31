import logging
from ._version import __version__
from .core.jejudo import Jejudo
from .core.jeju_log import *
from os.path import isfile
import os
import json

Directory = os.path.dirname(os.path.realpath(__file__))

logger: logging.Logger = logging.getLogger(__name__)

if not isfile(f'{Directory}/core/data.json'):
    sdd = {
            "jejudo": {
                "tag": "jejudo",
                "value": "**jejudo project for py-cord**\n```py\npip install -U jejudo\n```\n```py\nbot.load_extension('jejudo')\n# or\nawait bot.load_extension('jejudo')\n```"
            } 
        }
    with open(f"{Directory}/core/data.json", "w",encoding="utf-8-sig") as json_file:
        json.dump(sdd,json_file,ensure_ascii = False, indent=4)
else:
    logger.info("[ jejudo ] The initial setup was skipped because the file was already created.")

def setup(bot):
    bot.add_cog(log(bot))
    bot.add_cog(Jejudo(bot))
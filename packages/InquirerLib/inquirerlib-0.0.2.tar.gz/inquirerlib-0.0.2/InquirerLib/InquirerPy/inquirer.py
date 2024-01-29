"""Servers as another entry point for `InquirerPy`.

See Also:
    :ref:`index:Alternate Syntax`.

`inquirer` directly interact with individual prompt classes. It’s more flexible, easier to customise and also provides IDE type hintings/completions.
"""

__all__ = [
    "checkbox",
    "confirm",
    "expand",
    "filepath",
    "fuzzy",
    "text",
    "select",
    "number",
    "rawlist",
    "secret",
]

from InquirerLib.InquirerPy.prompts import CheckboxPrompt as checkbox
from InquirerLib.InquirerPy.prompts import ConfirmPrompt as confirm
from InquirerLib.InquirerPy.prompts import ExpandPrompt as expand
from InquirerLib.InquirerPy.prompts import FilePathPrompt as filepath
from InquirerLib.InquirerPy.prompts import FuzzyPrompt as fuzzy
from InquirerLib.InquirerPy.prompts import InputPrompt as text
from InquirerLib.InquirerPy.prompts import ListPrompt as select
from InquirerLib.InquirerPy.prompts import NumberPrompt as number
from InquirerLib.InquirerPy.prompts import RawlistPrompt as rawlist
from InquirerLib.InquirerPy.prompts import SecretPrompt as secret

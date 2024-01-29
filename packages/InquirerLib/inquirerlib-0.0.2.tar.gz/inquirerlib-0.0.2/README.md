# InquirerLib

<!-- TODO: UPDATED BADGES -->

An updated fork of InquirerPy - see API notice below

<!-- start intro -->

## Introduction

`InquirerPy` is a Python port of the famous [Inquirer.js](https://github.com/SBoudrias/Inquirer.js/) (A collection of common interactive command line user interfaces).
This project is a re-implementation of the [PyInquirer](https://github.com/CITGuru/PyInquirer) project, with bug fixes of known issues, new prompts, backward compatible APIs
as well as more customisation options.

<!-- end intro -->

![Demo](https://github.com/kazhala/gif/blob/master/InquirerPy-demo.gif)

## Motivation

[PyInquirer](https://github.com/CITGuru/PyInquirer) is a great Python port of [Inquirer.js](https://github.com/SBoudrias/Inquirer.js/), however, the project is slowly reaching
to an unmaintained state with various issues left behind and no intention to implement more feature requests. I was heavily relying on this library for other projects but
could not proceed due to the limitations.

Some noticeable ones that bother me the most:

- hard limit on `prompt_toolkit` version 1.0.3
- various color issues
- various cursor issues
- No options for VI/Emacs navigation key bindings
- Pagination option doesn't work

This project uses python3.7+ type hinting with focus on resolving above issues while providing greater customisation options.

## Requirements

### OS

Leveraging [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit), `InquirerPy` works cross platform for all OS. Although Unix platform may have a better experience than Windows.

### Python

```
python >= 3.7
```

## API notice

Some functions are exported directly using `from InquirerLib`; other functions and all exported objects are within `InquirerLib.InquirerPy` namespace.

The optional arguments for `prompt` and `prompt_async` are now keyword arguments, with `raise_keyboard_interrupt` (which defaults to `True`) now deprecated. Rationale is to support a possible easier prompt API in the future - see DRAFT RFC PR: <https://github.com/brodybits/InquirerLib/pull/3>

**[Documentation for InquirerPy](https://inquirerpy.readthedocs.io/)** applies with these updated imports and optional arguments for `prompt` and `prompt_async` as now keyword arguments.

Note that importing from `InquirerLib.InquirerPy.inquirer` is DEPRECATED, as documented below.

Examples in `examples` may be helpful.

## Getting Started

### Install

```sh
pip install InquirerLib
```

### Quick Start

#### Classic Syntax (PyInquirer)

```python
from InquirerLib import prompt

questions = [
    {"type": "input", "message": "What's your name:", "name": "name"},
    {"type": "confirm", "message": "Confirm?", "name": "confirm", "default": True},
]
result = prompt(questions)
name = result["name"]
confirm = result["confirm"]
```

NOTE: `default` may be used for any question type.

#### Alternate Syntax

Using individual constructors:

```python
from InquirerLib.InquirerPy import prompts

name = prompts.InputPrompt(message="What's your name:").execute()
confirm = prompts.ConfirmPrompt(message="Confirm?", default=True).execute()
```

DEPRECATED API:

```python
from InquirerLib.InquirerPy import inquirer

name = inquirer.text(message="What's your name:").execute()
confirm = inquirer.confirm(message="Confirm?", default=True).execute()
```

These are deprecated aliases that may be removed or replaced in the future.

<!-- start migration -->

## Migrating from InquirerPy

Need to update the imports, as described above.

## Migrating from PyInquirer

Most APIs from [PyInquirer](https://github.com/CITGuru/PyInquirer) should be compatible with `InquirerPy`. If you have discovered more incompatible APIs, please
create an issue or directly update README via a pull request.

### EditorPrompt

`InquirerPy` does not support [editor](https://github.com/CITGuru/PyInquirer#editor---type-editor) prompt as of now.

### CheckboxPrompt

The following table contains the mapping of incompatible parameters.

| PyInquirer      | InquirerPy      |
| --------------- | --------------- |
| pointer_sign    | pointer         |
| selected_sign   | enabled_symbol  |
| unselected_sign | disabled_symbol |

### Style

Every style keys from [PyInquirer](https://github.com/CITGuru/PyInquirer) is present in `InquirerPy` except the ones in the following table.

| PyInquirer | InquirerPy |
| ---------- | ---------- |
| selected   | pointer    |

Although `InquirerPy` support all the keys from [PyInquirer](https://github.com/CITGuru/PyInquirer), the styling works slightly different.
Please refer to the [Style](https://inquirerpy.readthedocs.io/en/latest/pages/style.html) documentation for detailed information.

<!-- end migration -->

## Similar projects

### questionary

[questionary](https://github.com/tmbo/questionary) is a fantastic fork which supports `prompt_toolkit` 3.0.0+ with performance improvement and more customisation options.
It's already a well established and stable library.

Comparing with [questionary](https://github.com/tmbo/questionary), `InquirerPy` offers even more customisation options in styles, UI as well as key bindings. `InquirerPy` also provides a new
and powerful [fuzzy](https://inquirerpy.readthedocs.io/en/latest/pages/prompts/fuzzy.html) prompt.

### python-inquirer

[python-inquirer](https://github.com/magmax/python-inquirer) is another great Python port of [Inquirer.js](https://github.com/SBoudrias/Inquirer.js/). Instead of using `prompt_toolkit`, it
leverages the library `blessed` to implement the UI.

Before implementing `InquirerPy`, this library came up as an alternative. It's a more stable library comparing to the original [PyInquirer](https://github.com/CITGuru/PyInquirer), however
it has a rather limited customisation options and an older UI which did not solve the issues I was facing described in the [Motivation](#Motivation) section.

Comparing with [python-inquirer](https://github.com/magmax/python-inquirer), `InquirerPy` offers a slightly better UI,
more customisation options in key bindings and styles, providing pagination as well as more prompts.

## Credit

This project is based on the great work done by the following projects & their authors.

- [PyInquirer](https://github.com/CITGuru/PyInquirer)
- [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit)

## License

This project is licensed under [MIT](https://github.com/kazhala/InquirerPy/blob/master/LICENSE).

# Copyright (c) 2024 espehon
# MIT License

import sys


if sys.stdout.encoding.lower() == 'utf-8':
    style = 'fancy'
else:
    style = 'plain'


DEFAULT_VALUES = {
    'dataFolder': '~/.local/share/tasky/',
    'dataFile': 'tasky.json',
    'newTaskSymbol': {
        'fancy': '[!]',
        'plain': '[!]'
    },
    'startedTaskSymbol': {
        'fancy': '[▶]',
        'plain': '[>]'
    },
    'stoppedTaskSymbol': {
        'fancy': '[.]',
        'plain': '[.]'
    },
    'completeTaskSymbol': {
        'fancy': '✔ ',
        'plain': '√ '
    },
    'flagSymbol': {
        'fancy': '🏳 ',
        'plain': ' *'
    },
    'flagSymbolAlt': {
        'fancy': '🏴',
        'plain': ' *'
    },
    'boarderColor': 'bright_black',
    'newTaskColor': 'red',
    'startedTaskColor': 'bright_yellow',
    'stoppedTaskColor': 'bright_red',
    'completeTaskColor': 'bright_green',
    'priorityColor1': 'white',
    'priorityColor2': 'cyan',
    'priorityColor3': 'yellow',
    'priorityColor4': 'red',
    'prioritySymbol1': {
        'fancy': '',
        'plain': ''
    },
    'prioritySymbol2': {
        'fancy': '(!)',
        'plain': '(!)'
    },
    'prioritySymbol3': {
        'fancy': '(!!)',
        'plain': '(!!)'
    },
    'prioritySymbol4': {
        'fancy': '(!!!)',
        'plain': '(!!!)'
    }
}


default_configs = f"""\
[Settings]
taskPath = "{DEFAULT_VALUES['dataFolder']}"
taskFile = "{DEFAULT_VALUES['dataFile']}"

newTaskSymbol = "{DEFAULT_VALUES['newTaskSymbol'][style]}"
startedTaskSymbol = "{DEFAULT_VALUES['startedTaskSymbol'][style]}"
stoppedTaskSymbol = "{DEFAULT_VALUES['stoppedTaskSymbol'][style]}"
completeTaskSymbol = "{DEFAULT_VALUES['completeTaskSymbol'][style]}"
flagSymbol = "{DEFAULT_VALUES['flagSymbol'][style]}"
flagSymbolAlt = "{DEFAULT_VALUES['flagSymbolAlt'][style]}"

boarderColor = "{DEFAULT_VALUES['boarderColor']}"
newTaskColor = "{DEFAULT_VALUES['newTaskColor']}"
startedTaskColor = "{DEFAULT_VALUES['startedTaskColor']}"
stoppedTaskColor = "{DEFAULT_VALUES['stoppedTaskColor']}"
completeTaskColor = "{DEFAULT_VALUES['completeTaskColor']}"

priorityColor1 = "{DEFAULT_VALUES['priorityColor1']}"
priorityColor2 = "{DEFAULT_VALUES['priorityColor2']}"
priorityColor3 = "{DEFAULT_VALUES['priorityColor3']}"
priorityColor4 = "{DEFAULT_VALUES['priorityColor4']}"

prioritySymbol1 = "{DEFAULT_VALUES['prioritySymbol1'][style]}"
prioritySymbol2 = "{DEFAULT_VALUES['prioritySymbol2'][style]}"
prioritySymbol3 = "{DEFAULT_VALUES['prioritySymbol3'][style]}"
prioritySymbol4 = "{DEFAULT_VALUES['prioritySymbol4'][style]}"
"""
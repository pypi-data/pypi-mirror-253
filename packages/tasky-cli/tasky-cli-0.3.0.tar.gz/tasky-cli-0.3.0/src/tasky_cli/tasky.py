# Copyright (c) 2024 espehon
# MIT License

#region: Housekeeping
import os
import sys
import argparse
import json
import datetime
import copy
from configparser import ConfigParser

from tasky_cli import defaults
from colorama import Fore, Style, init
init(autoreset=True)

# Set user paths
# home = os.path.expanduser("~") # not needed?
config_path = os.path.expanduser("~/.config/tasky/")
config_file = f"{config_path}tasky.ini"

# Set argument parsing
parser = argparse.ArgumentParser(
    description="Tasky: A to-do list program!\n\nBased off of klaudiosinani's Taskbook for JavaScript.",
    epilog="Examples: ts --task this is a new task, ts --switch 1, ts --complete 1",
    allow_abbrev=False,
    add_help=False,
    usage="ts [option] <arguments>    'try: ts --help'"
)

parser.add_argument('-?', '--help', action='help', help='Show this help message and exit.')
parser.add_argument('-t', '--task', action='store_true', help='Add a new task')
parser.add_argument('-c', '--complete', nargs='+', metavar='T', action='store', type=int, help='Mark task(s) complete')
parser.add_argument('-s', '--switch', nargs='+', metavar='T', action='store', type=int, help='Toggle task(s) as started/stopped')
parser.add_argument('-f', '--flag', nargs='+', metavar='T', action='store', type=int, help='Flag task(s) with astrict (*)')
parser.add_argument('-p', '--priority', nargs=2, metavar=('T', 'P'), action='store', type=int, help='Set the priority of task [T] to [P]')
parser.add_argument('-e', '--edit', nargs=1, metavar='T', action='store', type=int, help='Enter edit mode on a task')
parser.add_argument('-d', '--delete', nargs='+', metavar='T', action='store', type=int, help='Mark task [T] for deletion')
parser.add_argument('--clean', action='store_true', help='Remove complete/deleted tasks and reset indices')
parser.add_argument('--configs', action='store_true', help='Check/reset configs')
parser.add_argument('text', nargs=argparse.REMAINDER, help='Task description that is used with --task')

config = ConfigParser()


# Set Variables / Constants
PRIORITIES = (1, 2, 3, 4)
DEFAULT_PRIORITY = 1

#TODO: #4 There should be an ASCII only set of characters for older terminals that tasky defaults too provided there is a way to get check a terminals ability.
# DEFAULT_CONFIGS = """\
# [Settings]
# taskPath = "~/.local/share/tasky/"
# taskFile = "tasky.json"

# newTaskSymbol = "[!]"
# startedTaskSymbol = "[▶]"
# stoppedTaskSymbol = "[.]"
# completeTaskSymbol = "✔ "
# flagSymbol = "🏳 "
# flagSymbolAlt = "🏴"

# boarderColor = "bright_black"
# newTaskColor = "red"
# startedTaskColor = "bright_yellow"
# stoppedTaskColor = "bright_red"
# completeTaskColor = "bright_green"

# priorityColor1 = "white"
# priorityColor2 = "cyan"
# priorityColor3 = "yellow"
# priorityColor4 = "red"

# prioritySymbol1 = ""
# prioritySymbol2 = "(!)"
# prioritySymbol3 = "(!!)"
# prioritySymbol4 = "(!!!)"
# """

# Color name mapping for colorama
COLORS = {
    'red': {'norm': Fore.RED, 'alt': Fore.LIGHTRED_EX},
    'yellow': {'norm': Fore.YELLOW, 'alt': Fore.LIGHTYELLOW_EX},
    'green': {'norm': Fore.GREEN, 'alt': Fore.LIGHTGREEN_EX},
    'cyan': {'norm': Fore.CYAN, 'alt': Fore.LIGHTCYAN_EX},
    'blue': {'norm': Fore.BLUE, 'alt': Fore.LIGHTBLUE_EX},
    'magenta': {'norm': Fore.MAGENTA, 'alt': Fore.LIGHTMAGENTA_EX},
    'black': {'norm': Fore.BLACK, 'alt': Fore.LIGHTBLACK_EX},
    'white': {'norm': Fore.WHITE, 'alt': Fore.LIGHTWHITE_EX},

    'bright_red': {'norm': Fore.LIGHTRED_EX, 'alt': Fore.RED},
    'bright_yellow': {'norm': Fore.LIGHTYELLOW_EX, 'alt': Fore.YELLOW},
    'bright_green': {'norm': Fore.LIGHTGREEN_EX, 'alt': Fore.GREEN},
    'bright_cyan': {'norm': Fore.LIGHTCYAN_EX, 'alt': Fore.CYAN},
    'bright_blue': {'norm': Fore.LIGHTBLUE_EX, 'alt': Fore.BLUE},
    'bright_magenta': {'norm': Fore.LIGHTMAGENTA_EX, 'alt': Fore.MAGENTA},
    'bright_black': {'norm': Fore.LIGHTBLACK_EX, 'alt': Fore.BLACK},
    'bright_white': {'norm': Fore.LIGHTWHITE_EX, 'alt': Fore.WHITE}
}


# Check if config folder exists, create it if missing.
if os.path.exists(config_path) == False:
    os.makedirs(config_path)

# Check if config file exists, create it if missing.
if os.path.exists(config_file) == False:
    with open(config_file, 'w', encoding='utf-8') as settingsFile:
        settingsFile.write(defaults.default_configs)

# Read-in configs
try:
    config.read(config_file, encoding='utf-8')
except:
    print(f"{Fore.RED}FATAL: Reading config file failed!")
    sys.exit(1)


# Unpack configs dict
#TODO: #2 Nest each variable in a try/except to fall back to a default value if the user messed up the config file.
    # variable_name = config["Settings"]["VarInFile"]
config_errors = []

try:
    data_path = config["Settings"]["taskPath"].replace('\"', '')
except:
    data_path = defaults.DEFAULT_VALUES['dataFolder']
    config_errors.append('dataFolder')

try:
    data_file = config["Settings"]["taskFile"].replace('\"', '')
except:
    data_file = defaults.DEFAULT_VALUES['dataFile']
    config_errors.append('dataFile')

try:
    newTaskSymbol = config["Settings"]["newTaskSymbol"].replace('\"', '')
except:
    newTaskSymbol = defaults.DEFAULT_VALUES['newTaskSymbol']['plain']
    config_errors.append('newTaskSymbol')

try:
    startedTaskSymbol = config["Settings"]["startedTaskSymbol"].replace('\"', '')
except:
    startedTaskSymbol = defaults.DEFAULT_VALUES['startedTaskSymbol']['plain']
    config_errors.append('startedTaskSymbol')

try:
    stoppedTaskSymbol = config["Settings"]["stoppedTaskSymbol"].replace('\"', '')
except:
    stoppedTaskSymbol = defaults.DEFAULT_VALUES['stoppedTaskSymbol']['plain']
    config_errors.append('stoppedTaskSymbol')

try:
    completeTaskSymbol = config["Settings"]["completeTaskSymbol"].replace('\"', '')
except:
    completeTaskSymbol = defaults.DEFAULT_VALUES['completeTaskSymbol']['plain']
    config_errors.append('completeTaskSymbol')

try:
    flagSymbol = config["Settings"]["flagSymbol"].replace('\"', '')
except:
    flagSymbol = defaults.DEFAULT_VALUES['flagSymbol']['plain']
    config_errors.append('flagSymbol')

try:
    flagSymbolAlt = config["Settings"]["flagSymbolAlt"].replace('\"', '')
except:
    flagSymbolAlt = defaults.DEFAULT_VALUES['flagSymbolAlt']['plain']
    config_errors.append('flagSymbolAlt')

try:
    boarderColor = config['Settings']['boarderColor'].replace('\"', '')
except:
    boarderColor = defaults.DEFAULT_VALUES['boarderColor']
    config_errors.append('boarderColor')

try:
    newTaskColor = config["Settings"]["newTaskColor"].replace('\"', '')
except:
    newTaskColor = defaults.DEFAULT_VALUES['newTaskColor']
    config_errors.append('newTaskColor')

try:
    startedTaskColor = config["Settings"]["startedTaskColor"].replace('\"', '')
except:
    startedTaskColor = defaults.DEFAULT_VALUES['startedTaskColor']
    config_errors.append('startedTaskColor')

try:
    stoppedTaskColor = config["Settings"]["stoppedTaskColor"].replace('\"', '')
except:
    stoppedTaskColor = defaults.DEFAULT_VALUES['stoppedTaskColor']
    config_errors.append('stoppedTaskColor')

try:
    completeTaskColor = config["Settings"]["completeTaskColor"].replace('\"', '')
except:
    completeTaskColor = defaults.DEFAULT_VALUES['completeTaskColor']
    config_errors.append('completeTaskColor')

try:
    priorityColor1 = config["Settings"]["priorityColor1"].replace('\"', '')
except:
    priorityColor1 = defaults.DEFAULT_VALUES['priorityColor1']
    config_errors.append('priorityColor1')

try:
    priorityColor2 = config["Settings"]["priorityColor2"].replace('\"', '')
except:
    priorityColor2 = defaults.DEFAULT_VALUES['priorityColor2']
    config_errors.append('priorityColor2')

try:
    priorityColor3 = config["Settings"]["priorityColor3"].replace('\"', '')
except:
    priorityColor3 = defaults.DEFAULT_VALUES['priorityColor3']
    config_errors.append('priorityColor3')

try:
    priorityColor4 = config["Settings"]["priorityColor4"].replace('\"', '')
except:
    priorityColor4 = defaults.DEFAULT_VALUES['priorityColor4']
    config_errors.append('priorityColor4')

try:
    prioritySymbol1 = config["Settings"]["prioritySymbol1"].replace('\"', '')
except:
    prioritySymbol1 = defaults.DEFAULT_VALUES['prioritySymbol1']['plain']
    config_errors.append('prioritySymbol1')

try:
    prioritySymbol2 = config["Settings"]["prioritySymbol2"].replace('\"', '')
except:
    prioritySymbol2 = defaults.DEFAULT_VALUES['prioritySymbol2']['plain']
    config_errors.append('prioritySymbol2')

try:
    prioritySymbol3 = config["Settings"]["prioritySymbol3"].replace('\"', '')
except:
    prioritySymbol3 = defaults.DEFAULT_VALUES['prioritySymbol3']['plain']
    config_errors.append('prioritySymbol3')

try:
    prioritySymbol4 = config["Settings"]["prioritySymbol4"].replace('\"', '')
except:
    prioritySymbol4 = defaults.DEFAULT_VALUES['prioritySymbol4']['plain']
    config_errors.append('prioritySymbol4')


# Priority tables
priority_color = {
    1: priorityColor1,
    2: priorityColor2,
    3: priorityColor3,
    4: priorityColor4,
}

priority_symbol = {
    1: prioritySymbol1,
    2: prioritySymbol2,
    3: prioritySymbol3,
    4: prioritySymbol4,
}


# Prepare for data read-in
data_path = os.path.expanduser(data_path)
data_path_file = data_path + data_file
data = {}

# Check if data folder exists, create it if missing.
if os.path.exists(data_path) == False:
    os.makedirs(data_path)


# Check if file exists, create it if missing.
if os.path.exists(data_path_file) == False:
    with open(data_path_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Read-in data
with open(data_path_file, 'r') as json_file:
    data = json.load(json_file)

#endregion



#region: Functions
def add_new_task(task: dict):
    """Adds a new task dict to the data dict"""
    data.update(task)


def update_tasks(override_data=None):
    """Write data dict to json. Allows for an optional override_data to use in place of the global data"""
    if override_data is None:
        with open(data_path_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        with open(data_path_file, 'w') as json_file:
            json.dump(override_data, json_file, indent=4)


def color(color_name: str, alternate_style: bool=False) -> str:
    """Takes a color name like 'red' and returns its colorama formatter string.
    alternate_style switches the bright status of the given color."""
    key1 = color_name
    key2 = 'norm' if not alternate_style else 'alt'
    return COLORS[key1][key2]


def color_gradient(scale: int) -> str:
    """Takes a float between 0 and 100 inclusive and returns a colorama color"""
    if scale >= 100:
        return Fore.LIGHTWHITE_EX
    elif scale >= 87:
        return Fore.LIGHTCYAN_EX
    elif scale >= 75:
        return Fore.CYAN
    elif scale >= 62:
        return Fore.LIGHTGREEN_EX
    elif scale >= 50:
        return Fore.GREEN
    elif scale >= 37:
        return Fore.LIGHTYELLOW_EX
    elif scale >= 25:
        return Fore.YELLOW
    elif scale >= 12:
        return Fore.LIGHTRED_EX
    else:
        return Fore.RED


def index_data(current_dict: dict) -> list:
    """
    Return list of keys as int from data dict.
    This is to get around the JavaScript limitation of keys being strings
    """
    output = []
    for k in current_dict.keys():
        output.append(int(k))
    return output


def format_new_task(index: int, task_desc: str, priority: int, flagged: bool) -> dict:
    "Return new task as a dict for storage"
    output = {str(index): {
        "desc": task_desc,
        "status": 0,
        "created": str(datetime.datetime.now().date()),
        "switched": "None",
        "priority": priority,
        "flag": flagged
    }}
    return output


def check_for_priority(text: str) -> tuple:
    """
    Returns a tuple containing bool and int.
    Bool represents if the priority was passed in the task description.
    Int represents the priority.
    """
    # This could be done with a match/case block, but I want to keep the Python requirements low.
    if len(text) == 3:
        a, b, c = text
        if str.lower(a) == 'p':
            if b == ':':
                try:
                    if int(c) in PRIORITIES:
                        return (True, int(c))
                except:
                    pass
    return (False, DEFAULT_PRIORITY)


def render_tasks(prolog: str="") -> None:
    """Print the tasks in all their glory"""

    # Get a fresh copy of data from file ()
    fresh_data = {}
    with open(data_path_file, 'r') as json_file: #TODO: #3 This function should take an optional passed dict for printing if it is not going to use the global data.
        fresh_data = json.load(json_file)
    data_copy = copy.deepcopy(fresh_data)

    # Count up the tasks and their status
    done, working, pending = 0, 0, 0
    for key, task in fresh_data.items():
        status = task['status']
        if status in [0, 2]:
            pending += 1
        elif status in [1]:
            working += 1
        elif status in [3]:
            done += 1
        elif status in [4]:
            data_copy.pop(key)
    total = done + working + pending

    # Calculate percent complete
    if total == 0:
        rate = 100
    else:
        rate = int((done / total) * 100)
    
    # Calculate the width of printout (length of longest description and a buffer)
    buffer = 20
    desc_lens = []
    for task in data_copy.values():
        desc_lens.append(len(task['desc']))
    if len(desc_lens) == 0:
        width = buffer
    else:
        width = max(desc_lens) + buffer

    # Format and prep line elements for printout
    boarder = [color(boarderColor) + "┍" + ("━"*width),
                " " + (color(boarderColor) + "─"*width) + "┚"]
    title = f"{color(boarderColor)}│{Style.RESET_ALL}  Tasky {color(boarderColor)}[{done}/{total}]"
    complete_stat = f"{color_gradient(rate)}{str(rate).rjust(3)}%{color(boarderColor)} of all tasks complete.{Style.RESET_ALL}"
    breakdown_stat = f"{color(completeTaskColor)}{str(done).rjust(3)}{color(boarderColor)} done · {color(startedTaskColor)}{working}{color(boarderColor)} in-progress · {color(stoppedTaskColor)}{pending}{color(boarderColor)} pending"
    
    def get_task_lines():
        """Prints a formatted line for each task"""
        for key, task in data_copy.items():
            if task['flag']:
                if task['status'] == 3:
                    flag = f"{color(boarderColor)}{flagSymbolAlt}{Style.RESET_ALL}"
                else:
                    flag = f"{color(priority_color[1],alternate_style=True)}{flagSymbol}{Style.RESET_ALL}"
            else:
                flag = "  "
            id = f"{flag}{color(boarderColor) + key.rjust(3) + '. ' + Style.RESET_ALL}"
            if task['status'] == 0:
                symbol = color(newTaskColor) + newTaskSymbol + Style.RESET_ALL + "  "
            elif task['status'] == 1:
                symbol = color(startedTaskColor) + startedTaskSymbol + Style.RESET_ALL + "  "
            elif task['status'] == 2:
                symbol = color(stoppedTaskColor) + stoppedTaskSymbol + Style.RESET_ALL + "  "
            elif task['status'] == 3:
                symbol = color(completeTaskColor) + completeTaskSymbol + Style.RESET_ALL + "  "
            
            if task['status'] == 3:
                desc = color(boarderColor) + task['desc'] + " " + priority_symbol[task['priority']] + Style.RESET_ALL + " "
            else:
                desc = color(priority_color[task['priority']], task['flag']) + task['desc'] + " " + priority_symbol[task['priority']] + Style.RESET_ALL + " "
            
            if task['status'] in [3]:
                start_date = datetime.datetime.strptime(task['created'], "%Y-%m-%d").date()
                end_date = datetime.datetime.strptime(task['switched'], "%Y-%m-%d").date()
            else:
                start_date = datetime.datetime.strptime(task['created'], "%Y-%m-%d").date()
                end_date = datetime.datetime.now().date()
            delta = end_date - start_date
            days = f"{color(boarderColor)}{str(delta.days)}d{Style.RESET_ALL}"
            
            print(id + symbol + desc + days)

    print() # print a blank line to help breakup the clutter
    if config_errors:
        print(f"{len(config_errors)} config(s) missing. try 'ts --configs' for details")
    if prolog != "":
        print(f"{prolog}")
    print(boarder[0])
    print(title)
    get_task_lines()
    print(boarder[1])
    print(complete_stat)
    print(breakdown_stat)


def switch_task_status(task_keys):
    updates = 0
    for task_key in task_keys:
        working_task = data[task_key]
        new_status = None
        if working_task['status'] in [0, 2]:
            new_status = 1
        elif working_task['status'] in [1]:
            new_status = 2
        if new_status is not None:
            working_task['status'] = new_status
            working_task['switched'] = str(datetime.datetime.now().date())
            data[task_key] = working_task
            updates += 1
    if updates > 0:
        update_tasks()
        render_tasks(f"{updates} task{'' if updates == 1 else 's'} updated.")


def mark_tasks_complete(task_keys):
    updates = 0
    for task_key in task_keys:
        working_task = data[task_key]
        new_status = None
        if working_task['status'] in [0, 1, 2]:
            new_status = 3
        elif working_task['status'] in [3]:
            new_status = 1
        if new_status is not None:
            working_task['status'] = new_status
            working_task['switched'] = str(datetime.datetime.now().date())
            data[task_key] = working_task
            updates += 1
    if updates > 0:
        update_tasks()
        render_tasks(f"{updates} task{'' if updates == 1 else 's'} updated.")


def mark_tasks_deleted(task_keys):
    updates = 0
    for task_key in task_keys:
        working_task = data[task_key]
        new_status = None
        if working_task['status'] != 4:
            new_status = 4
        if new_status is not None:
            working_task['status'] = new_status
            working_task['switched'] = str(datetime.datetime.now().date())
            data[task_key] = working_task
            updates += 1
    if updates > 0:
        update_tasks()
        render_tasks(f"{updates} task{'' if updates == 1 else 's'} marked for deletion.")


def clean_task_list(task_keys, old_data):
    updates = 0
    for key in task_keys:
        if old_data[key]['status'] in [3, 4]:
            old_data.pop(key)
            updates += 1
    new_data = {}
    for index, task in enumerate(old_data.values()):
        new_data[str(index + 1)] = task
    if updates > 0:
        update_tasks(new_data)
        render_tasks("Tasks cleaned.")
    else:
        print("Nothing to clean.")


def change_task_priority(task_id, new_priority):
    updates = 0
    if new_priority in PRIORITIES:
        if data[str(task_id)]['priority'] != new_priority:
            data[str(task_id)]['priority'] = new_priority
            updates += 1
        if updates > 0:
            update_tasks()
            render_tasks(f"Task #{task_id} set to priority level {new_priority}.")
    else:
        print(f"{new_priority} is not an available priority level.")


def flag_tasks(task_keys):
    updates = 0
    for task_key in task_keys:
        try:
            working_task = data[task_key]
            working_task['flag'] = not working_task['flag']
            updates += 1
        except:
            print(f"'{task_key}' is an invalid task id.")
    if updates > 0:
        update_tasks()
        render_tasks(f"{updates} task{'' if updates == 1 else 's'} updated.")


def edit_task(task_key):
    if task_key in data:
        new_desc = input(f"Enter new task description for #{task_key}...\n>>> ").strip()
        data[task_key]['desc'] = new_desc
        update_tasks()
        render_tasks(f"Task #{task_key} has been edited.")
    else:
        print(f"'{task_key}' is an invalid task id.")


def check_configs(reset_keyword: str=""):
    if reset_keyword == "reset":
        repair_configs(warn=True)
    elif config_errors:
        print('Missing configurations:')
        for error in config_errors:
            print(f"\t{error}")
        print("\nUse 'ts --configs reset' to reset the config file")
    else:
        print("No config errors found.")


def repair_configs(warn: bool=True):
    if warn:
        user = input("Overwrite configuration file with defaults? [y/N] > ").lower()
        if user == "y":
            with open(config_file, 'w', encoding='utf-8') as settingsFile:
                settingsFile.write(defaults.default_configs)
            print(f"{config_file} reset.")

    

# Main
tasks_index = index_data(data)

if len(tasks_index) == 0:
    next_index = 1
else:
    next_index = max(tasks_index) + 1

def tasky(argv=None):
    args = parser.parse_args(argv) #Execute parse_args()

    passed_string = (" ".join(args.text)).strip()
    passed_priority = check_for_priority(passed_string[-3:])

    if passed_priority[0]:
        passed_string = passed_string[:-3].strip()


    # --task
    if args.task:    
        new_task = format_new_task(next_index, passed_string, passed_priority[1], False)
        add_new_task(new_task)
        update_tasks()
        render_tasks("New task added.")

    # --switch
    elif args.switch:
        keys = [str(i) for i in args.switch]
        switch_task_status(keys)

    # --complete
    elif args.complete:
        keys = [str(i) for i in args.complete]
        mark_tasks_complete(keys)


    # --delete
    elif args.delete:
        keys = [str(i) for i in args.delete]
        mark_tasks_deleted(keys)


    # --clean
    elif args.clean:
        keys = [str(i) for i in tasks_index]
        clean_task_list(keys, data)


    # --priority
    elif args.priority:
        T, P = args.priority
        change_task_priority(T, P)


    # --flag
    elif args.flag:
        keys = [str(i) for i in args.flag]
        flag_tasks(keys)


    # --edit
    elif args.edit:
        key = str(args.edit[0])
        edit_task(key)
    

    # --configs
    elif args.configs:
        check_configs(passed_string.lower())


    # no args
    else:
        render_tasks()
    




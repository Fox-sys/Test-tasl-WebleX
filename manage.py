import os
import sys
import importlib
import traceback
from src.config import Config
from src.app import app


def get_command_list() -> list:
    commands = os.listdir(Config().BASE_DIR / 'src' / 'commands')
    commands.remove('__init__.py')
    edited_commands = []
    for command in commands:
        edited_commands.append(command[:-3:])
    return edited_commands


def main():
    commands = get_command_list()
    args = sys.argv
    if len(args) < 2:
        return 'Для запуска конкретной команды пропишите python project_manager *название композита*'
    if args[1] == 'help':
        return 'список доступных команд: \n' + "\n".join(commands)
    if args[1] not in commands:
        return 'Такой команды не существует, список доступных команд: \n' + "\n".join(commands)
    try:
        module = importlib.import_module(f'src.commands.{args[1]}')
    except ModuleNotFoundError:
        return 'Это не команда, это папка)'
    except Exception:
        print(traceback.format_exc())
        return
    try:
        return module.entrypoint(*args[2:])
    except AttributeError:
        return 'Кто то написал слово entrypoint с ошибкой или вообще решил, что эта функция нам даром не сдалась'
    except Exception:
        print(traceback.format_exc())
        return


if __name__ == '__main__':
    print(main())

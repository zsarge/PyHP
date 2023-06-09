import re
import os
import argparse
from typing import Callable, Match

EXECUTE_REGEX = re.compile(r'\{\%(.*?)\%\}', re.DOTALL)
EVALUATE_REGEX = re.compile(r'\{\{(.*?)\}\}', re.DOTALL)
template_namespace = {}


def parse(template: str) -> str:
    def make_replacer(handler: Callable) -> Callable[[Match], str]:
        def replace(match: Match) -> str:
            code = str(match[1]).strip()
            return str(handler(parse(code), globals(), template_namespace) or "")
        return replace

    executor = make_replacer(exec)
    evaluator = make_replacer(eval)

    # execute everything between '{%' and '%}' and replace it with nothing
    template = EXECUTE_REGEX.sub(executor, template)

    # evaluate everything between '{{' and '}}' and recursively replace it with its result
    return EVALUATE_REGEX.sub(evaluator, template)


def include(path: str):
    assert os.path.isfile(path)
    with open(path) as f:
        return parse(f.read())


def define(func):
    globals()[func.__name__] = func
    return lambda: func()


def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument(
        '--file', type=str, help='Enter the path to the file you want to convert', required=True)
    parsedArgs = argParser.parse_args()

    assert os.path.isfile(parsedArgs.file)
    # change director to specified file
    os.chdir(os.path.dirname(parsedArgs.file))

    with open(parsedArgs.file) as file:
        print(parse(file.read()))


if __name__ == "__main__":
    main()

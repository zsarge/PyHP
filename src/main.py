import re
import os
import argparse
from typing import Callable

EXECUTE_REGEX = re.compile(r'\{\%(.*?)\%\}', re.DOTALL)
EVALUATE_REGEX = re.compile(r'\{\{(.*?)\}\}', re.DOTALL)
template_namespace = {}


def parse(template: str) -> str:
    def make_replacer(handler: Callable) -> Callable[[str], str]:
        def replace(match: str) -> str:
            new_template = parse(str(match[1]).strip())
            return str(handler(new_template, globals(), template_namespace) or "")
        return replace

    executor = make_replacer(exec)
    evaluator = make_replacer(eval)

    # execute everything between '{%' and '%}' and replace them with nothing
    template = EXECUTE_REGEX.sub(executor, template)

    # execute everything between '{{' and '}}' and recursively replace them with their result
    return EVALUATE_REGEX.sub(evaluator, template)


def include(path: str):
    assert os.path.isfile(path)
    with open(path) as f:
        return parse(f.read())


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

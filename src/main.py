import re
import time
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


def main():
    template = r"""
    <html>
        {% def say_hello(n: int) -> str:
            return 'hello! ' * n
        %} 
        {{ say_hello(10) }}
    </html>
     """
    print(parse(template))


if __name__ == "__main__":
    main()

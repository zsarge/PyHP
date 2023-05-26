import re
import time

EXECUTE_REGEX = re.compile(r'\{\%(.*?)\%\}', re.DOTALL)
EVALUATE_REGEX = re.compile(r'\{\{(.*?)\}\}', re.DOTALL)


template_namespace = {}


def parse(template: str) -> str:
    # execute everything between '{%' and '%}' and replace them with nothing
    template = EXECUTE_REGEX.sub(
        lambda match: exec(str(match[1]).strip(), globals(), template_namespace), template)

    # execute everything between '{{' and '}}' and recursively replace them with their result
    def replace(match: str) -> str:
        return str(eval(parse(str(match[1]).strip()), globals(), template_namespace))
    new_template = EVALUATE_REGEX.sub(replace, template)
    return new_template


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

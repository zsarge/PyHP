{%
import random
import string
define(random)  # could be nested in function as well
define(string)

@define
def obfuscate(letter: str, garbage: bool = False) -> str:
    if garbage:
        return f"<span class=\"garbage\">{letter}</span>"
    else:
        return f"<span>{letter}</span>"

@define
def get_garbage() -> str:
    alphabet = string.ascii_letters
    return random.choice(alphabet)

def obfuscate_email(email: str) -> str:
    result = ""
    for letter in email:
        result += obfuscate(letter)
        result += obfuscate(get_garbage(), garbage=True)
    return result
%}

<style>
.garbage {
    display: none;
}
</style>

<div id="my-email-i-want-to-protect-from-scammers">
    {{ obfuscate_email("e@a.com") }}
</div>
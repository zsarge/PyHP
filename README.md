# PyHP

Python Home Page

A static site generator built using only the Python standard library, used for templating in Python.

The syntax is loosely based on Jinja templates:

|   Syntax    | Description                                                             |
| :---------: | :---------------------------------------------------------------------- |
| `{{ ... }}` | evaluates the contents of the brackets and includes the results as text |
| `{% ... %}` | executes the contents of the brackets                                   |

All of the parsing comes from Python's built-in `eval` and `exec` statements, so there are some limitations.
For example, for loops cannot currently be spread apart in execution brackets, as Python will not be able to interpret the partial code. However, this can be worked around returning all the necessary HTML in another block.

## Basic Example

```
<p>
    {% from datetime import datetime %}
    {{ datetime.now().strftime("%Y-%m-%d") }}
</p>
```

when evaluated with `python3 src/main.py --file $(realpath example_site/example.php)`,

will print:

```
<p>

    2023-05-25
</p>
```

## Including templates

As demonstrated in the [Example Site](./example_site/), it is possible to include code from partial views:

```
{{ include('./head.php') }}
```

Given that `{{ ... }}` simply includes the results of evaluated code, the `include` function simply reads a file, parses it, and returns it as a string, for use in templating.

Given these basic building blocks, it should be possible to create many types of static sites.

#### Inspired by [CincyPy](https://cincypy.com/)

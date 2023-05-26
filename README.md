# PyHP - Python Home Page

> A static site generator built using only the Python standard library, used for templating in Python.

The syntax is loosely based on Jinja templates:

|   Syntax    | Description                                                             |
| :---------: | :---------------------------------------------------------------------- |
| `{{ ... }}` | evaluates the contents of the brackets and includes the results as text |
| `{% ... %}` | executes the contents of the brackets                                   |

All of the parsing comes from Python's built-in `eval` and `exec` statements, so there are some limitations.
For example, for loops cannot currently be spread apart in execution brackets, as Python will not be able to interpret the partial code. However, this can be worked around returning all the necessary HTML in another block.

You can find the main parser [here](https://github.com/zsarge/PyHP/blob/main/src/main.py#L11-L31).

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

As demonstrated in the [example site](./example_site/), it is possible to include code from partial views:

```
{{ include('./head.php') }}
```

Given that `{{ ... }}` simply includes the results of evaluated code, the `include` function simply reads a file, parses it, and returns it as a string, for use in templating.

Given these basic building blocks, it should be possible to create many types of static sites.

## Advanced example

Given the [example site](./example_site/),

```console
$ python3 src/main.py --file $(realpath example_site/index.php)
```

produces

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Example Document</title>
  </head>

  <body>
    <h1>Hello World!</h1>

    <p>Generated at 1685073812.9931087</p>

    <footer>&copy; 2023 Zack Sargent</footer>
  </body>
</html>
```

(with slightly different whitespace).

![image](https://github.com/zsarge/PyHP/assets/46602241/9282b725-8109-4315-86d0-25e9532d6a43)

## To Do

- [x] Evaluate basic templates
- [ ] Evaluate multiple templates from a director
- [ ] Output to files / directories, instead of standard output
- [ ] Include asset management system for non-template files
- [ ] Figure out how to handle pagination

#### Inspired by [CincyPy](https://cincypy.com/)

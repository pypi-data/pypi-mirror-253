"""Fills in placeholder values in a string or file.

Intended for HTML files. Simple substitution only, with an easy API
"""

import re


class TemplateError(KeyError):
    """Rendering a template failed due a placeholder without a value."""


def render(template: str, /, **variables) -> str:
    """Render the template with the provided variables.

    The template should contain placeholders that will be replaced. These
    placeholders consist of the placeholder name within double curly braces. The
    name of the placeholder should be a valid python identifier. Whitespace
    between the braces and the name is ignored. E.g.: `{{ placeholder_name }}`

    An exception will be raised if there are placeholders without corresponding
    values. It is acceptable to provide unused values; they will be ignored.

    Parameters
    ----------
    template: str
        Template to fill with variables.

    **variables: Any
        Keyword arguments for the placeholder values. The argument name should
        be the same as the placeholder's name. You can unpack a dictionary of
        value with `render(template, **my_dict)`.

    Returns
    -------
    rendered_template: str
        Filled template.

    Raises
    ------
    TemplateError
        Value not given for a placeholder in the template.
    TypeError
        If the template is not a string, or a variable cannot be casted to a
        string.

    Examples
    --------
    >>> template = "<p>Hello {{myplaceholder}}!</p>"
    >>> simple_template.render(template, myplaceholder="World")
    "<p>Hello World!</p>"
    """

    def isidentifier(s: str):
        return s.isidentifier()

    def extract_placeholders():
        matches = re.finditer(r"{{\s*([^}]+)\s*}}", template)
        unique_names = {match.group(1) for match in matches}
        return filter(isidentifier, unique_names)

    def substitute_placeholder(name):
        try:
            value = str(variables[name])
        except KeyError as err:
            raise TemplateError("Placeholder missing value", name) from err
        pattern = r"{{\s*%s\s*}}" % re.escape(name)
        return re.sub(pattern, value, template)

    for name in extract_placeholders():
        template = substitute_placeholder(name)
    return template


def render_file(template_path: str, /, **variables) -> str:
    """Render a template directly from a file.

    Otherwise the same as `simple_template.render()`.

    Examples
    --------
    >>> simple_template.render_file("/path/to/template.html", myplaceholder="World")
    "<p>Hello World!</p>"
    """
    with open(template_path, "rt", encoding="UTF-8") as fp:
        template = fp.read()
    return render(template, **variables)

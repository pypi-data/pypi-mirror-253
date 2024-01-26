"""Tests for the whole simple_template module."""

import pytest

import simple_template


def test_simple_placeholder():
    """Simple case of a single placeholder being templated."""
    template = "<p>{{greeting}} World!</p>"
    actual = simple_template.render(template, greeting="Hello")
    expected = "<p>Hello World!</p>"
    assert actual == expected


def test_multiple_placeholders():
    """Templating of multiple different placeholders."""
    template = "<p>{{greeting}} {{who}}!</p>"
    actual = simple_template.render(template, greeting="Hello", who="World")
    expected = "<p>Hello World!</p>"
    assert actual == expected


def test_repeated_placeholders():
    """Templating of repeated placeholders."""
    template = "<p>{{who}} says {{greeting}} {{ who }}!</p>"
    actual = simple_template.render(template, greeting="Hello", who="World")
    expected = "<p>World says Hello World!</p>"
    assert actual == expected


def test_template_with_no_placeholders():
    """Trivial case with no placeholders."""
    template = "<p>Hello World!</p>"
    assert simple_template.render(template) == template


def test_extra_arguments():
    """Give unneeded keyword arguments to ensure they are ignored."""
    template = "<p>{{greeting}} World!</p>"
    actual = simple_template.render(template, greeting="Hello", extra="Ignored")
    expected = "<p>Hello World!</p>"
    assert actual == expected


def test_missing_argument_exception():
    """Exception raised if template is missing a value."""
    template = "<p>{{greeting}} World!</p>"
    with pytest.raises(simple_template.TemplateError):
        simple_template.render(template)


def test_improper_template_type_exception():
    """Exception raised if template isn't a string."""
    template = 3.14159265
    with pytest.raises(TypeError):
        simple_template.render(template)


def test_render_file():
    """Render a template in a file."""
    actual = simple_template.render_file("tests/template_file.html", greeting="Hello")
    expected = "<p>Hello World!</p>\n"
    assert actual == expected

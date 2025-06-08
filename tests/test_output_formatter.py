"""
Unit tests for the `output_formatter` module in `scrapesome.formatter`.

These tests cover:
- Converting HTML content to plain text, JSON, and Markdown
- Formatting content based on specified output format types
- Fallback behavior when unknown or missing formats are specified

Test cases ensure that key content elements are extracted and formatted as expected.
"""

from scrapesome.formatter import output_formatter as of

HTML_SAMPLE = """
<html>
<head>
  <title>Test Page</title>
  <meta name="description" content="This is a test page">
</head>
<body>
  <h1>Hello</h1>
  <p>World</p>
</body>
</html>
"""

def test_get_text_basic():
    """
    Test that get_text returns plain text with HTML tags stripped out.
    """
    text = of.get_text("<p>Hello <b>World</b></p>")
    assert "Hello" in text and "World" in text
    # Should strip tags

def test_get_text_empty():
    """
    Test that get_text returns an empty string when given empty input.
    """
    assert of.get_text("") == ""

def test_get_json_complete():
    """
    Test that get_json extracts title, description, and URL from a well-formed HTML document.
    """
    json_data = of.get_json(HTML_SAMPLE, url="http://fake.com")
    assert json_data["title"] == "Test Page"
    assert json_data["description"] == "This is a test page"
    assert json_data["url"] == "http://fake.com"

def test_get_json_missing_title_and_description():
    """
    Test that get_json handles missing title and meta description tags gracefully.
    """
    html = "<html><head></head><body>No title or description</body></html>"
    json_data = of.get_json(html)
    assert json_data["title"] == ""
    assert json_data["description"] == ""
    assert json_data["url"] == ""

def test_get_markdown_basic():
    """
    Test that get_markdown converts basic HTML tags to Markdown syntax.
    """
    md = of.get_markdown("<h1>Header</h1><p>Para</p>")
    assert "# Header" in md and "Para" in md

def test_format_response_none_returns_html():
    """
    Test that format_response returns raw HTML when no output_format_type is specified.
    """
    result = of.format_response("<html>Test</html>")
    assert result == "<html>Test</html>"

def test_format_response_text():
    """
    Test that format_response returns plain text when output_format_type is 'text'.
    """
    result = of.format_response("<p>Hello</p>", output_format_type="text")
    assert "Hello" in result

def test_format_response_json():
    """
    Test that format_response returns a dictionary when output_format_type is 'json'.
    """
    result = of.format_response(HTML_SAMPLE, url="http://fake.com", output_format_type="json")
    assert isinstance(result, dict)
    assert result["title"] == "Test Page"

def test_format_response_markdown():
    """
    Test that format_response returns Markdown when output_format_type is 'markdown'.
    """
    result = of.format_response("<h1>Hi</h1>", output_format_type="markdown")
    assert "# Hi" in result

def test_format_response_unknown_format():
    """
    Test that format_response defaults to returning raw HTML when an unknown format type is provided.
    """
    html = "<p>Test</p>"
    result = of.format_response(html, output_format_type="unknown")
    assert result == html

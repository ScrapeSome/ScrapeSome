
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
    text = of.get_text("<p>Hello <b>World</b></p>")
    assert "Hello" in text and "World" in text
    # Should strip tags

def test_get_text_empty():
    assert of.get_text("") == ""

def test_get_json_complete():
    json_data = of.get_json(HTML_SAMPLE, url="http://fake.com")
    assert json_data["title"] == "Test Page"
    assert json_data["description"] == "This is a test page"
    assert json_data["url"] == "http://fake.com"

def test_get_json_missing_title_and_description():
    html = "<html><head></head><body>No title or description</body></html>"
    json_data = of.get_json(html)
    assert json_data["title"] == ""
    assert json_data["description"] == ""
    assert json_data["url"] == ""

def test_get_markdown_basic():
    md = of.get_markdown("<h1>Header</h1><p>Para</p>")
    assert "# Header" in md and "Para" in md

def test_format_response_none_returns_html():
    result = of.format_response("<html>Test</html>")
    assert result == "<html>Test</html>"

def test_format_response_text():
    result = of.format_response("<p>Hello</p>", output_format_type="text")
    assert "Hello" in result

def test_format_response_json():
    result = of.format_response(HTML_SAMPLE, url="http://fake.com", output_format_type="json")
    assert isinstance(result, dict)
    assert result["title"] == "Test Page"

def test_format_response_markdown():
    result = of.format_response("<h1>Hi</h1>", output_format_type="markdown")
    assert "# Hi" in result

def test_format_response_unknown_format():
    html = "<p>Test</p>"
    result = of.format_response(html, output_format_type="unknown")
    assert result == html

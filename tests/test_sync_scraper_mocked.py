
from unittest.mock import patch, MagicMock
import requests
from scrapesome import sync_scraper

# SUCCESS: simple fetch returns content with output_format_type
@patch("scrapesome.scraper.sync_scraper.sync_render_page")
@patch("scrapesome.scraper.sync_scraper.format_response")
@patch("scrapesome.scraper.sync_scraper.requests.get")
def test_scraper_success_with_format(mock_get, mock_format_response, mock_render):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "<html><body>Hello World</body></html>"
    mock_get.return_value = mock_response

    mock_format_response.return_value = "Hello World"

    result = sync_scraper("http://fake.com", output_format_type="text")
    assert result == "Hello World"

# SUCCESS: fallback to render when content is too short
@patch("scrapesome.scraper.sync_scraper.sync_render_page")
@patch("scrapesome.scraper.sync_scraper.requests.get")
def test_scraper_fallback_to_render(mock_get, mock_render):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "Too short"
    mock_get.return_value = mock_response

    mock_render.return_value = "<html><body>Rendered Content</body></html>"

    result = sync_scraper("http://fake.com")
    assert "Rendered Content" in result

# SUCCESS: force Playwright rendering
@patch("scrapesome.scraper.sync_scraper.sync_render_page")
def test_scraper_force_playwright(mock_render):
    mock_render.return_value = "<html><body>Playwright Content</body></html>"

    result = sync_scraper("http://fake.com", force_playwright=True)
    assert "Playwright Content" in result

# FAILURE: all retries fail and Playwright fallback also fails
@patch("scrapesome.scraper.sync_scraper.sync_render_page", side_effect=Exception("Rendering failed"))
@patch("scrapesome.scraper.sync_scraper.requests.get", side_effect=Exception("HTTP failed"))
def test_scraper_all_failures(mock_get, mock_render):
    result = sync_scraper("http://fake.com")
    assert result is None


@patch("scrapesome.scraper.sync_scraper.sync_render_page")
@patch("scrapesome.scraper.sync_scraper.requests.get")
def test_scraper_retries_on_403_then_succeeds(mock_get, mock_render):
    mock_403 = MagicMock()
    mock_403.status_code = 403
    mock_403.text = "Forbidden"

    mock_200 = MagicMock()
    mock_200.status_code = 200
    mock_200.text = "<html><body>" + "Recovered " * 50 + "</body></html>"

    mock_get.side_effect = [mock_403, mock_200]

    result = sync_scraper("http://fake.com")
    assert "Recovered" in result

@patch("scrapesome.scraper.sync_scraper.requests.get")
def test_scraper_no_redirects(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "<html><body>" + "No redirects" * 50+"</body></html>"
    mock_get.return_value = mock_response

    result = sync_scraper("http://fake.com", allow_redirects=False)
    assert "No redirects" in result

@patch("scrapesome.scraper.sync_scraper.requests.get")
def test_scraper_with_custom_user_agents(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "<html><body>"+"UA test" * 50+"</body></html>"
    mock_get.return_value = mock_response

    result = sync_scraper("http://fake.com", user_agents=["TestAgent/1.0"])
    assert "UA test" in result

# simulate multiple request exceptions then successful render fallback
@patch("scrapesome.scraper.sync_scraper.requests.get", side_effect=requests.exceptions.RequestException)
@patch("scrapesome.scraper.sync_scraper.sync_render_page")
def test_sync_scraper_retries_exhausted_then_render_fallback(mock_render, mock_get):
    mock_render.return_value = "<html>Fallback Render</html>"
    result = sync_scraper("http://fake.com", max_retries=2)
    assert "Fallback Render" in result

# simulate short response content triggers rendering fallback
@patch("scrapesome.scraper.sync_scraper.requests.get")
@patch("scrapesome.scraper.sync_scraper.sync_render_page")
def test_sync_scraper_short_content_triggers_render(mock_render, mock_get):
    mock_resp = MagicMock(status_code=200, text="short")
    mock_get.return_value = mock_resp
    mock_render.return_value = "<html>Rendered Content</html>"
    result = sync_scraper("http://fake.com")
    assert "Rendered Content" in result


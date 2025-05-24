
def test_default_timeout_env():
    from scrapesome.config import Settings
    settings = Settings()
    assert  settings.fetch_page_timeout != 42

def test_enable_logging_env():
    from scrapesome.config import Settings
    settings = Settings()
    assert settings.log_level == "INFO"

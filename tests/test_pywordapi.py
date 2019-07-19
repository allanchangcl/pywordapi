from pywordapi import WpRest


def test_get_posts():
    api_url = "https://demo.wp-api.org/"
    api = WpRest(api_url)
    results = api.get_posts()
    assert isinstance(results, dict) is True


def test_get_posts_with_wrong_headers():
    headers = ''
    api_url = "https://demo.wp-api.org/"
    api = WpRest(api_url, headers)
    results = api.get_posts()
    assert isinstance(results, dict) is True


def test_get_posts_with_headers():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
        + "Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "Accept-Language": "en-US,en;q=0.8"
    }
    api_url = "https://demo.wp-api.org/"
    api = WpRest(api_url, headers)
    results = api.get_posts()
    assert isinstance(results, dict) is True


def test_get_categories():
    api_url = "https://demo.wp-api.org/"
    api = WpRest(api_url)
    results = api.get_categories()
    assert isinstance(results, dict) is True


def test_get_posts_from_non_existent_site():
    api_url = "https://demo.iamnotasite.xyz/"
    api = WpRest(api_url)
    results = api.get_posts()
    # print(results['error'])
    assert isinstance(results, dict) is True


def test_get_categories_from_non_existent_site():
    api_url = "https://demo.iamnotasite.xyz/"
    api = WpRest(api_url)
    results = api.get_categories()
    # print(results['error'])
    assert isinstance(results, dict) is True


def test_get_categories_from_non_wordpress_site():
    api_url = "https://httpbin.org/"
    api = WpRest(api_url)
    results = api.get_categories()
    # print(results)
    assert isinstance(results, dict) is True

# def test_get_posts_with_proxy():
    # api_url = "https://demo.wp-api.org/"
    # api_url = ""
    # # proxy_url = ""
    # api = WpRest(api_url, proxy_url)
    # results = api.get_posts()
    # assert isinstance(results, dict) is True

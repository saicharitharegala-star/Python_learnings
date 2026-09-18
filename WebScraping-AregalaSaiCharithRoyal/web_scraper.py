"""Simple product scraper made for the Web Scraping using Python assignment.

The default links are from books.toscrape.com, a website created for web
scraping practice. You can also pass your own Books to Scrape product links.
"""

from pathlib import Path
from urllib.parse import urljoin
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from html.parser import HTMLParser
import re
import ssl


# A few product pages are included so the program demonstrates multiple URLs.
PRODUCT_URLS = [
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
    "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
    "https://books.toscrape.com/catalogue/soumission_998/index.html",
]
TARGET_PRICE = 30.00
IMAGE_FOLDER = Path("downloaded_images")
# Some Python installations do not include the system certificate store.
# This project only reads the public Books to Scrape practice website.
SSL_CONTEXT = ssl._create_unverified_context()


class ProductPageParser(HTMLParser):
    """Collect the needed product details from a Books to Scrape page."""

    def __init__(self):
        super().__init__()
        self.product_main_depth = 0
        self.gallery_depth = 0
        self.div_stack = []
        self.reading_title = False
        self.reading_price = False
        self.title = ""
        self.price_text = ""
        self.image_src = ""

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = attributes.get("class", "").split()

        if tag == "div":
            is_product_main = "product_main" in classes
            is_gallery = attributes.get("id") == "product_gallery"
            self.div_stack.append((is_product_main, is_gallery))
            self.product_main_depth += is_product_main
            self.gallery_depth += is_gallery

        if tag == "h1" and self.product_main_depth:
            self.reading_title = True
        elif tag == "p" and "price_color" in classes and self.product_main_depth:
            self.reading_price = True
        elif tag == "img" and self.gallery_depth:
            self.image_src = attributes.get("src", "")

    def handle_endtag(self, tag):
        if tag == "h1":
            self.reading_title = False
        elif tag == "p":
            self.reading_price = False
        elif tag == "div" and self.div_stack:
            is_product_main, is_gallery = self.div_stack.pop()
            self.product_main_depth -= is_product_main
            self.gallery_depth -= is_gallery

    def handle_data(self, data):
        if self.reading_title:
            self.title += data
        elif self.reading_price:
            self.price_text += data


def get_price_as_number(price_text):
    """Remove the currency symbol and return a price that can be compared."""
    match = re.search(r"[0-9]+(?:\.[0-9]+)?", price_text)
    if not match:
        raise ValueError(f"Could not read the price: {price_text}")
    return float(match.group())


def scrape_product(url):
    """Fetch one product page and collect its title, price and image URL."""
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=15, context=SSL_CONTEXT) as response:
        page_html = response.read().decode("utf-8")

    parser = ProductPageParser()
    parser.feed(page_html)

    if not all([parser.title, parser.price_text, parser.image_src]):
        raise ValueError("The expected product details were not found on this page.")

    return {
        "title": parser.title.strip(),
        "price_text": parser.price_text.strip(),
        "price": get_price_as_number(parser.price_text),
        "image_url": urljoin(url, parser.image_src),
    }


def safe_file_name(title):
    """Make a title safe to use as an image file name."""
    cleaned_title = re.sub(r"[^a-zA-Z0-9_-]+", "_", title).strip("_")
    return cleaned_title[:60] or "product_image"


def download_image(image_url, title):
    """Download a product image into the downloaded_images folder."""
    IMAGE_FOLDER.mkdir(exist_ok=True)
    request = Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=15, context=SSL_CONTEXT) as image_response:
        image_data = image_response.read()

    image_path = IMAGE_FOLDER / f"{safe_file_name(title)}.jpg"
    image_path.write_bytes(image_data)
    return image_path


def show_product_result(product, image_path):
    """Print the collected product details in an easy-to-read format."""
    print("\n" + "-" * 55)
    print("Title     :", product["title"])
    print("Price     :", product["price_text"])
    print("Image URL :", product["image_url"])
    print("Saved to  :", image_path)

    if product["price"] <= TARGET_PRICE:
        print(f"Price check: Within the target price of £{TARGET_PRICE:.2f}")
    else:
        print(f"Price check: Above the target price of £{TARGET_PRICE:.2f}")


def main():
    print("Product Web Scraper")
    print(f"Checking {len(PRODUCT_URLS)} product URLs. Target price: £{TARGET_PRICE:.2f}")

    for url in PRODUCT_URLS:
        try:
            product = scrape_product(url)
            image_path = download_image(product["image_url"], product["title"])
            show_product_result(product, image_path)
        except (HTTPError, URLError, TimeoutError) as error:
            print(f"\nCould not open {url}\nReason: {error}")
        except (ValueError, TypeError) as error:
            print(f"\nCould not scrape {url}\nReason: {error}")


if __name__ == "__main__":
    main()

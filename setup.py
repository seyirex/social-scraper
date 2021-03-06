from setuptools import setup

setup(
    name='social_scraper',
    packages=["social_scraper", "social_scraper.collections",
              "social_scraper.items", "social_scraper.platforms", "social_scraper.users"],
    description='Wrapper for snscrape',
    version='0.1',
    url='https://github.com/leoyn/social-scraper',
    author='leoyn',
    keywords=["twitter", "social network", "scraping", "snscrape"],
    python_requires='~=3.8',
    install_requires=[
        "snscrape@git+https://github.com/JustAnotherArchivist/snscrape.git#egg=snscrape"
    ],
)

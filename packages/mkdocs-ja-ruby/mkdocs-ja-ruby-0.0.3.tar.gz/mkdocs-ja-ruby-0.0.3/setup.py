from setuptools import setup, find_packages

setup(
    name="mkdocs-ja-ruby",
    version="0.0.3",
    description="Just for fun. A ruby plugin for mkdocs",
    url="https://ashitemaru.github.io",
    author="Ashitemaru",
    author_email="ashitemaru.holder@gmail.com",
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "mkdocs-ja-ruby=mkdocs_ja_ruby.plugin:ExtendedMarkdown",
        ]
    }
)
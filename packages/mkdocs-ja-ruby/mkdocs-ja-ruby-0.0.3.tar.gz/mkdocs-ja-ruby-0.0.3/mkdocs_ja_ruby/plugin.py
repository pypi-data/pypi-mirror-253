import re
from mkdocs.plugins import BasePlugin

class ExtendedMarkdown(BasePlugin):
    def __init__(self):
        self.raw_pattern = re.compile(r"\[@ (.+) (.+)\]")
        self.ruby_pattern = r"<ruby>\1<rp>(</rp><rt>\2</rt><rp>)</rp></ruby>"

    def on_page_markdown(self, markdown, page, config, files):
        markdown = re.sub(self.raw_pattern, self.ruby_pattern, markdown)
        return markdown

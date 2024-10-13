from pathlib import Path
from ..utils import calc_readtime

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "words"

    def start_requests(self):
        urls = [
            "https://docs.djangoproject.com/en/5.1/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_main)

    def parse_main(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        base_url = "https://docs.djangoproject.com/en/5.1/"
        sub_sections = response.xpath("//div[@id='docs-content']//h2/following::div[@class='section']")
        readtime = calc_readtime(response)
        self.log(f"Total Read Time = {readtime} minutes")
        self.log(f"Saved file {filename}")
        required_sections = ['The model layer', 'The view layer', 'The template layer',
            'Forms', 'The development process', 'The admin', 'Security',
            'Common web application tools', 'Other core functionalities']
        for sub_section in sub_sections:
            subsub_section_urls = sub_section.xpath(".//ul/li/a/@href").getall()
            sub_section_text = sub_section.xpath('.//h2/text()').getall()
            if sub_section_text[0] in required_sections:
                yield from response.follow_all([f"{base_url}{link}" for link in subsub_section_urls], self.parse_sub)
    
    def parse_sub(self, response):
        pass
import scrapy
import os
import re

from ..utils import *

class CompetitionMatchesSpider(scrapy.Spider):
    name = 'competition_matches'

    def __init__(self, fed_acronym='', competition_id='', competition_pid='', **kwargs):
        self.start_urls = [f'https://{fed_acronym}-web.dataproject.com/CompetitionMatches.aspx?ID={competition_id}&PID={competition_pid}']
        self.competition_id = competition_id
        self.competition_pid = competition_pid
        self.fed_acronym = fed_acronym
        match_id = ''
        match_date = ''
        match_location = ''
        home_team = ''
        home_points = ''
        guest_team = ''
        guest_points = ''
        self.first_item_date = ''
        self.last_item_date = ''

        super().__init__(**kwargs)

    def start_requests(self):        
        cookies = {f'CompetitionLangCode{self.fed_acronym}': 'en-GB'}
        yield scrapy.Request(self.start_urls[0], cookies=cookies, callback=self.parse)

    def parse(self, response):
        competition_items = []

        matches = response.xpath("//div[@id='printableArea']/div/div/div/div/div[position() >= 1]/div[2]/div")

        for match in matches:
            match_id_string = match.xpath("./div/div/div[5]/p/@onclick").get()
            match_id = re.search(r'mID=(\d+)', match_id_string).group(1)

            match_date_text = match.xpath("./div/div/div/p[1]/span[1]/text()").get()
            match_date = parse_short_date(match_date_text)

            match_location = match.xpath("./div/div/div/p[2]/span[1]/text()").get()
            if match_location:
                match_location = match_location.lower()

            home_team = match.xpath("./div/div/div[5]/p/span/*/text() | ./div/div/div[5]/p/span/text()").get()
            if home_team:
                home_team = home_team.lower()

            home_points = match.xpath("./div/div/div[7]/p[1]/span[1]/b/text()").get()

            guest_team = match.xpath("./div/div/div[9]/p/span/*/text() | ./div/div/div[9]/p/span/text()").get()
            if guest_team:
                guest_team = guest_team.lower()

            guest_points = match.xpath("./div/div/div[7]/p[1]/span[3]/b/text()").get()

            competition = {
                'Match ID': match_id,
                'Match Date': match_date,
                'Stadium': match_location,
                'Home Team': home_team,
                'Home Points': home_points,
                'Guest Team': guest_team,
                'Guest Points': guest_points,
            }

            competition_items.append(competition)
            yield competition

        first_date = competition_items[0]['Match Date']
        last_date = competition_items[-1]['Match Date']

        regex = r"\b\d{4}\b"
        match_start = re.search(regex, first_date)
        match_final = re.search(regex, last_date)

        if match_start:
            self.first_item_date = match_start.group()

        if match_final:
             self.last_item_date = match_final.group()
        
    def closed(spider, reason):
        src = f'data/{spider.fed_acronym}-{spider.competition_id}-{spider.competition_pid}-competition_matches.csv'

        if spider.competition_pid != None:
            spider.competition_pid = f'{spider.competition_pid}-'

        if spider.competition_pid == None:
            spider.competition_pid = ''


        dst = f'data/{spider.fed_acronym}-{spider.competition_id}-{spider.competition_pid}{spider.first_item_date}-{spider.last_item_date}-competition-matches.csv'

        try:
            os.rename(src, dst)

            print(f'volleystats: {dst} file was created')
        except(FileExistsError):
            print(f'volleystats: file {dst} already exists.\n{src} was created or renamed')
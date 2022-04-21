# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def replace_comma (value):
    
    return value.replace(',','.')

def new(value):
    if value == 'nuova offerta':
        return True
    
    else:
        return False

    
    
    
class IndeedItem(scrapy.Item):
    
    job_title = scrapy.Field(output_processor  = TakeFirst())
    
    company = scrapy.Field(output_processor  = TakeFirst())
    
    company_link = scrapy.Field(output_processor  = TakeFirst())
    
    rating = scrapy.Field(input_processor = MapCompose(replace_comma))
    
    location = scrapy.Field(output_processor  = TakeFirst())
    
    job_link = scrapy.Field(output_processor  = TakeFirst())
    
    new_offer = scrapy.Field(input_processor = MapCompose(new),
                             output_processor = TakeFirst())

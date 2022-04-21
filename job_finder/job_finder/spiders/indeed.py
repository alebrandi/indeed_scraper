from gc import callbacks
import scrapy
from scrapy.loader import ItemLoader
from job_finder.items import IndeedItem

class indeed(scrapy.Spider):
    name = 'indeed'
    
    start_urls = ['https://it.indeed.com/offerte-lavoro?q=project%20manager']    
    
    def parse(self, response): 
        
        for job in response.css('div.mosaic-zone a[id]'):
            
            l = ItemLoader(item = IndeedItem(),response = response, selector = job)
            
            l.add_css('job_title', 'span::attr("title")')#ok
            l.add_css('company','.companyName::text , .companyOverviewLink::text')
            l.add_css('rating', 'span.ratingNumber span::text') ##no
            l.add_css('location', 'div.companyLocation::text') #no
            l.add_css('new_offer', 'span.label::text') #no
                        
                
            job_link = response.urljoin(job.css('::attr("href")').get())
            company_link_text = job.css('a[data-tn-element = "companyName"]::attr("href")').get()
            company_link = response.urljoin(company_link_text) if company_link_text is not None else None 
            l.add_value('company_link', company_link)
            l.add_value('job_link', job_link)
            
            yield l.load_item()
            
        
        next_page = response.css('a[aria-label = "Prossima"]::attr("href")').get()
        
        if next_page:
            next_page = response.urljoin(next_page)
            
            yield scrapy.Request(next_page, callback = self.parse)
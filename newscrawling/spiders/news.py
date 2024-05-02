import scrapy

class news_crawling(scrapy.Spider):
    name = "newscrawl"
    
    def start_requests(self):
        start_url = f"https://www.borsaitaliana.it/borsa/notizie/price-sensitive/risultati.html?page=0"
        yield scrapy.Request(url=start_url, callback=self.total_pages)
    
    def total_pages(self, response):
        self.totalpage = response.css("li.m-pagination__item")[-3].css("a::text").get()
        for i in range(1, int(self.totalpage)+1):
            start_url_2 = f"https://www.borsaitaliana.it/borsa/notizie/price-sensitive/risultati.html?page={str(i)}"
            yield scrapy.Request(url=start_url_2, callback=self.parse)
        
        
    def parse(self, response):
        
        div_container = response.css("div.l-media__body.m-relases__content")
        for data in div_container:
            yield {
                "title": data.css("h3::text").get(),
                "msgdate":data.css("span::text").get()
            }
            
        
        

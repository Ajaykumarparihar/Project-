import scrapy



class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://www.realliving.com/michael.litchin"]

    def parse(self, response):
        print("{ OUR RESPONSE }")
        data = response.css("#website-info-text").get()
        agent_name = response.css("h4::text").get()
        agent_photo = response.css("#agent-photo-widget::attr(src)").get()
        agent_title = response.css("b::text").get()
        agent_address = response.css("#website-info-text::text").getall()[1:3]
        agent_phone = response.css("#website-info-text::text").getall()[3]
        agent_email = response.css("#website-info-text a::attr(href)").get() 
        agent_facebook = response.css("#website-connect a::attr(href)").getall()[0]
        agent_linkedin= response.css("#website-connect a::attr(href)").getall()[1]
        about = response.css("div::text").getall()[34]

        yield{
           "data":data,
            "agent_name":agent_name,
           "agent_photo":agent_photo,
           "agent_title":agent_title,
           "agent_address":agent_address,
           "agent_phone":agent_phone,
            "agent_email":agent_email,
            "agent_facebook":agent_facebook,
            "agent_linkedin":agent_linkedin,
            "about":about   
        }                
        

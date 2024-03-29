import scrapy


class RlofficeSpider(scrapy.Spider):
    name = "rloffice"
    allowed_domains = ["mega.nz"]
    start_urls = ["https://mega.nz/folder/ksYAXR5S#Oy9DapBfBrV2UyM_cksYhw"]

   
class RlofficeSpider(scrapy.Spider):
    name = "rloffice"
    allowed_domains = ["www.realliving.com"]
    start_urls = ["https://www.realliving.com/norman-realty/Office/RealLivingNormanRealty-261547"]


    def parse(self, response):
        print("{OUR RESPONSE}")
        office_name =  response.css(".ao-office-details-container h2 span::text").get()
        office_address = response.css(".ao-office-details-container p span::text").getall()
        office_zipcode = response.css(".ao-office-details-container p span::text").getall()[3]
        office_phone = response.css("#office-phone-main ::text").get()
        office_fax = response.css("#office-phone-fax ::text").get()
        office_url = response.css("#office-website a::attr(href)").getall()[0]
        office_email = response.css("#office-email a::attr(href)").get()

        yield{"name":office_name,
              "address":office_address,
              "zipcode":office_zipcode,
              "phone":office_phone,
              "fax":office_fax,
              "url":office_url,
              "email":office_email}


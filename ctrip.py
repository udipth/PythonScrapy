import scrapy
from scrapy.crawler import CrawlerProcess
import dropbox

class myspider(scrapy.Spider):
    name = "ctrip"
    start_urls = ['http://hotels.ctrip.com/hotel/taipei617#ctm_ref=hod_hp_sb_lst']
    for n in range(2,25):
        k='http://hotels.ctrip.com/hotel/taipei617/p'+str(n)
        start_urls.append(k)
    print start_urls
    def parse(self, response):
        for k in response.css('div.searchresult_list.searchresult_list2'):
            yield {
                'name': k.css('searchresult_name, a::attr(title)').re_first(r'\((.*?)\)') ,
                'rating': k.css('span.hotel_value::text').extract_first() ,
                'image': k.css('view_pic view_pic_fall_down, img::attr(src)').extract_first(),
            }
        

process = CrawlerProcess({
'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
'FEED_FORMAT': 'csv',
'FEED_URI': 'ctrip_data.csv'
})

process.crawl(myspider)
process.start()


dbx = dropbox.Dropbox('ACCESS TOKEN')

with open('ctrip_data.csv', 'rb') as f:
    dbx.files_upload(f.read(), '/ctrip_data.csv')

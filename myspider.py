import scrapy


class myspider(scrapy.Spider):
    name = "ctrip"
    start_urls = ['http://hotels.ctrip.com/hotel/taipei617#ctm_ref=hod_hp_sb_lst']

    def parse(self, response):
        for k in response.css('div.searchresult_list.searchresult_list2'):
            yield {
                'name': k.css('searchresult_name, a::attr(title)').re_first(r'\((.*?)\)') ,
                'rating': k.css('span.hotel_value::text').extract_first() ,
                'image': k.css('view_pic view_pic_fall_down, img::attr(src)').extract_first(),
            }

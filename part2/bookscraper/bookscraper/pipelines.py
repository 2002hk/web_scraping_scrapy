# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter=ItemAdapter(item)
        #strip all the whitespaces from strings
        field_names=adapter.field_names()
        for field_name in field_names:
            if field_name != 'description':
                value=adapter.get(field_name)
                adapter[field_name]=value[0].strip()
        

        #product type-->switch to lowercase
        lowercase_keys=['product_type']
        for lowercase_key in lowercase_keys:
            value=adapter.get(lowercase_key)
            adapter[lowercase_key]=value.lower()

        #price-->convert to float
        price_keys=['price','price_excl','price_incl_tax','tax']
        for price_key in price_keys:
            value=adapter.get(price_key)
            value=value.replace('£','')
            adapter[price_key]=float(value)
        return item


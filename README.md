# Amazon Dataset API
#### Step 1: Python Spider

Source Data: [Amazon Product Dataset](http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/)

Command: `scrapy crawl Amazon`

Action: crawler information from the website and save it to JSON files in the format:

```
{
	"dataset": dataset name, 
	"url": link
}
```

Build Module: https://docs.python.org/2.7/distutils/setupscript.html

#### Step 2: Data Download

Class AmazonData:

- profile(self)

- get(self, dataset, type) 



#### Reference

- [Scrapy](https://doc.scrapy.org/en/latest/)
- [Build Python Modules](https://docs.python.org/2.7/distutils/setupscript.html)






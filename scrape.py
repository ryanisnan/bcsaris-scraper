from scrapely import Scraper


s = Scraper()



url1 = 'https://s3-us-west-2.amazonaws.com/bcsaris/2007/AutoSave_10.htm'
data = {
    'Task Number': '074566',
    'SAR Manager': 'Ron Royston',
    'Reporting SAR Group': 'North Shore Rescue',
    'Contact Phone #': '604-443-2122',
    'Incident Location': 'Mount Seymour, North Vancouver',
    'Incident Province': 'British Columbia'
}
s.train(url1, data)

url2 = 'https://s3-us-west-2.amazonaws.com/bcsaris/2007/AutoSave_11.htm'
print s.scrape(url2)

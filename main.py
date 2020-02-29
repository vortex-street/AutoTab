from scraper import get_urls, url_to_notes

top_tabs_url = r'https://www.ultimate-guitar.com/explore?type[]=Tabs&&order=hitstotal_desc'
urls = get_urls(top_tabs_url)

for url in urls:
    notes, tabs = url_to_notes(url)
    if notes != 'NA' and tabs != 'NA':
        print(notes)
        print(tabs)
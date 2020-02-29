from scraper import get_urls, url_to_notes

top_tabs_url = r'https://www.ultimate-guitar.com/explore?type[]=Tabs&&order=hitstotal_desc'
urls = get_urls(top_tabs_url)
for page in range(2, 10):
    next_page = top_tabs_url + '&page=' + str(page)
    new_urls = get_urls(next_page)
    for url in new_urls:
        urls.append(url)

all_notes = []
all_tabs = []
# urls = [r'https://tabs.ultimate-guitar.com/tab/green-day/wake-me-up-when-september-ends-tabs-141135']
for url in urls:
    try:
        notes, tabs = url_to_notes(url)
    except:
        notes, tabs = 'NA', 'NA'
        continue
    if notes != 'NA' and tabs != 'NA':
        print(notes)
        print(tabs)
        all_notes.append('')
        all_notes.append(notes)
        all_tabs.append('')
        all_tabs.append(tabs)

print(len(all_notes))
print(len(all_tabs))
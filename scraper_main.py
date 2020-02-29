from scraper_fun import get_urls, url_to_notes, parse_name

top_tabs_url = r'https://www.ultimate-guitar.com/explore?type[]=Tabs&&order=hitstotal_desc'
urls = []
for page in range(1, 10):
    if page == 1:
        next_page = top_tabs_url
    else:
        next_page = top_tabs_url + '&page=' + str(page)
    new_urls = get_urls(next_page)
    for url in new_urls:
        urls.append(url)

with open('data.txt', 'w') as new_file:
    new_file.write('notes, tabs\n')
previous_titles = []

for url in urls:
    title = parse_name(url)
    if title not in previous_titles:
        print('\t' + title)
        previous_titles.append(title)
        try:
            notes, tabs = url_to_notes(url)
            if notes == '' and tabs == '':
                print('Not successful')
            else:
                print('Successful')
        except:
            notes, tabs = '', ''
            print('Not successful')
            print()
            continue
        with open('data.txt', 'a') as file:
            added = False
            for note, tab in zip(notes, tabs):
                file.write(note + ', ' + tab + '\n')
                added = True
            if added:
                file.write('END, END\n')
    else:
        continue
    print()

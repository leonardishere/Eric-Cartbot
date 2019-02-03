import requests
from bs4 import BeautifulSoup as bs
import os
import re

base_url = 'https://southpark.fandom.com'

# config params

get_everybody = True
get_person = 'not used'
anonymous = True
file_out = 'everybody_anonymous.dat'

#get_everybody = True
#get_person = 'not used'
#file_out = 'everybody.dat'

# scrapes the links from a given url
def get_out_links(url):
    main_page = requests.get(url)
    main_soup = bs(main_page.text, 'html.parser')
    main_links = main_soup.select('.wikia-gallery-item .lightbox-caption a[href]')
    season_urls = []
    for link in main_links:
        try:
            season_urls.append(base_url + link['href'])
        except KeyError:
            pass
    return season_urls

# scrapes the given url for the contents of the script and writes it to file
def write_content_to_file(url, f):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    table = soup.select('table')[1]
    rows = table.find_all('tr')
    # loop across rows with data
    for i in range(2, len(rows)-1):
        try:
            row = rows[i]
            person = row.contents[1].span.center.string.strip()
            line = row.contents[2].span.string.strip().replace('\n', ' ')
            if get_everybody:
                #s = clean(person + ': ' + line) + '\n'
                #s = (clean(line) if anonymous else clean(person + ': ' + line)) + '\n'
                s = line if anonymous else (person + ': ' + line)
                s = clean_to_file(s) + '\n'
                f.write(s)
            else:
                if person == get_person:
                    s = clean_to_file(line) + '\n'
                    f.write(s)
        except AttributeError:
            pass
        except UnicodeEncodeError:
            print('UnicodeEncodeError at line number: ' + str(i))

# cleans a string so that it can be written to file without a UnicodeEncodeError
def clean_to_file(s):
    s = s.encode('ascii', 'ignore').decode('utf-8') # deletes bad stuff?
    s = re.sub(r'\s+', ' ', s) # convert all groups of whitespace to single space
    return s

# cleans a url, at least makes it look better
def clean_url(url):
    # theres definitely better ways to do this but whatever
    url = (url
        .replace('https://southpark.fandom.com/wiki/Portal:Scripts/', '')
        .replace('https://southpark.fandom.com/wiki/', '')
        .replace('/Script', '')
        .replace('_', ' ')
        .replace('%27', "'")
        .replace('%3F', '?')
        .replace('%26', '&')
        .replace('%C3%A8', 'e')#'è')
        .replace('%25', '%')
    )
    return url

# main function
def main():
    f = open(file_out, 'w')
    season_urls = get_out_links('https://southpark.fandom.com/wiki/Portal:Scripts')
    # for every season
    for season_url in season_urls:
        print(clean_url(season_url))
        episode_urls = get_out_links(season_url)
        # for every episode in season
        for episode_url in episode_urls:
            print('\t' + clean_url(episode_url))
            # write the episode's script to file
            write_content_to_file(episode_url, f)
    f.close()

main()

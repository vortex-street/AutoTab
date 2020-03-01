from __future__ import print_function
from bs4 import BeautifulSoup
import requests
import re

scale = ['A0', 'A+0', 'B0', 'C0', 'C+0', 'D0', 'D+0', 'E0', 'F0', 'F+0', 'G0', 'G+0',
         'A1', 'A+1', 'B1', 'C1', 'C+1', 'D1', 'D+1', 'E1', 'F1', 'F+1', 'G1', 'G+1',
         'A2', 'A+2', 'B2', 'C2', 'C+2', 'D2', 'D+2', 'E2', 'F2', 'F+2', 'G2', 'G+2',
         'A3', 'A+3', 'B3', 'C3', 'C+3', 'D3', 'D+3', 'E3', 'F3', 'F+3', 'G3', 'G+3',
         'A4', 'A+4', 'B4', 'C4', 'C+4', 'D4', 'D+4', 'E4', 'F4', 'F+4', 'G4', 'G+4']
string_dict = {'E': 'E0', 'A': 'A1', 'D': 'D1', 'G': 'G1', 'B': 'B2', 'e': 'E2'}


# This function converts a note in tab form to a note
def note_from_tab(fret, string):
    if string in string_dict:
        string = string_dict.get(string)
    elif string.upper() in string_dict:
        string = string_dict.get(string.upper())
    i = scale.index(string)
    try:
        note = scale[i + fret]
    except:
        note = scale[i + int(str(fret)[0:2])]
    return note


# This function converts the text of a string's notes to notes
def compile_frets(string_text):
    skips = 0
    string_text_notes = []
    string_text_indices = []
    for i, slot in enumerate(string_text):
        num = re.compile(r'\d')
        if num.search(slot) and skips == 0:
            group = slot
            j = 1
            while True:
                next_slot = string_text[i + j]
                if num.search(next_slot):
                    group = group + next_slot
                    j += 1
                else:
                    break
            skips = len(group) - 1
            string_text_notes.append(int(group))
            string_text_indices.append(int(i))
        elif skips != 0:
            skips -= 1
    return string_text_notes, string_text_indices


# These functions work to sort the indices array in order, and adjust the order of the notes and tab arrays
def partition(arr, arr2, arr3, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            arr2[i], arr2[j] = arr2[j], arr2[i]
            arr3[i], arr3[j] = arr3[j], arr3[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    arr2[i + 1], arr2[high] = arr2[high], arr2[i + 1]
    arr3[i + 1], arr3[high] = arr3[high], arr3[i + 1]
    return (i + 1)


def quickSort(arr, arr2, arr3, low, high):
    if low < high:
        pi = partition(arr, arr2, arr3, low, high)
        quickSort(arr, arr2, arr3, low, pi - 1)
        quickSort(arr, arr2, arr3, pi + 1, high)


# This function gets the urls from a tab page on ultimate guitar
def get_urls(tab_page):
    response = requests.get(tab_page)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.findAll('div', {'class': 'js-store'})
    links = re.split(r'https://', str(text))
    good_links = []
    for i, link in enumerate(links):
        if link[0:4] == 'tabs':
            good_links.append(link)
    pattern = re.compile(r'&quot.+')
    final_urls = []
    for link in good_links:
        excess = re.search(r'&quot.+', link)[0]
        link = link[:-len(excess)]
        link = 'https://' + link
        final_urls.append(link)
    return final_urls


# This function parses the name of the song from the URL
def parse_name(url):
    splits = re.split(r'/', url)
    name = splits[-1]
    new_splits = re.split(r'-', name)
    new_name = new_splits[:-2]
    title = ''
    for word in new_name:
        new_word = ''
        for i, letter in enumerate(word):
            if i == 0:
                new_letter = letter.upper()
            else:
                new_letter = letter
            new_word = new_word + new_letter
        title = title + new_word + ' '
    return title


def url_to_notes(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.findAll('div', {'class': 'js-store'})
    tuning = 'EADGBe'
    lines = re.split(r'\[tab]', str(text[0]))
    string_1 = ''
    string_2 = ''
    string_3 = ''
    string_4 = ''
    string_5 = ''
    string_6 = ''
    for line in lines:
        single = re.split(r'\\n', line)
        for lin in single:
            lin = lin.replace('[/tab]', '')
            lin = lin.replace('\\r', '')
            lin = lin.replace('\\\\', '\\')
            lin = lin.replace('||', '|')
            match = re.compile(r'^\w\|.+\|.*$')
            if match.search(lin):
                string_start = lin[0]
                if ' ' in lin:
                    splits = re.split(r'\|', lin)
                    lin = lin.replace(splits[-1], '')
                if string_start == tuning[0]:
                    string_1 = (string_1 + lin).replace('|' + tuning[0] + '|', '|')
                elif string_start == tuning[1]:
                    string_2 = (string_2 + lin).replace('|' + tuning[1] + '|', '|')
                elif string_start == tuning[2]:
                    string_3 = (string_3 + lin).replace('|' + tuning[2] + '|', '|')
                elif string_start == tuning[3]:
                    string_4 = (string_4 + lin).replace('|' + tuning[3] + '|', '|')
                elif string_start == tuning[4]:
                    string_5 = (string_5 + lin).replace('|' + tuning[4] + '|', '|')
                elif string_start == tuning[5]:
                    string_6 = (string_6 + lin).replace('|' + tuning[5] + '|', '|')
                elif string_start in tuning.lower():
                    if string_start == tuning.lower()[1]:
                        string_2 = (string_2 + lin).replace('|' + string_start + '|', '|')
                    elif string_start == tuning.lower()[2]:
                        string_3 = (string_3 + lin).replace('|' + string_start + '|', '|')
                    elif string_start == tuning.lower()[3]:
                        string_4 = (string_4 + lin).replace('|' + string_start + '|', '|')
                    elif string_start == tuning.lower()[4]:
                        string_5 = (string_5 + lin).replace('|' + string_start + '|', '|')

    strings = string_1, string_2, string_3, string_4, string_5, string_6

    for i, string in enumerate(strings[:-1]):
        if len(string) != len(strings[i + 1]) or len(string) == 0:
            return '', ''
    notes = []
    indices = []
    tabs = []
    for string in strings:
        string_notes, string_indices = compile_frets(string)
        for i, note in enumerate(string_notes):
            alph_note = note_from_tab(note, string[0])
            notes.append(alph_note)
            indices.append(string_indices[i])
            tabs.append(string[0] + str(note))

    quickSort(indices, notes, tabs, 0, len(notes) - 1)

    for i, index in enumerate(indices):
        n = i
        dups = 0
        while True:
            if n + 1 < len(indices):
                if indices[n + 1] == index:
                    dups += 1
                    n += 1
                else:
                    break
            else:
                break
        if dups != 0:
            for dup in range(dups, 0, -1):
                notes[i] = notes[i] + ';' + notes[i + dup]
                tabs[i] = tabs[i] + ';' + tabs[i + dup]
                notes.pop(i + dup)
                tabs.pop(i + dup)
                indices.pop(i + dup)
        else:
            continue
    return notes, tabs


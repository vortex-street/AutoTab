from ds import *
import csv


def in_key(note):
    print(note)
    key_truth = []
    for i, key in enumerate([A, B, C, D, E, F, G, A_, C_, D_, F_, G_,
                             Am, Bm, Cm, Dm, Em, Fm, Gm, A_m, C_m, D_m, F_m, G_m]):
        if note in key:
            key_truth.append(True)
        else:
            key_truth.append(False)
    return key_truth


with open('data_test.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_number = 0
    for line in csv_reader:
        line_number += 1
        if line_number == 1:
            continue
        else:
            note = line[0]
            tab = line[1]
            notes_in_cluster = len(tab) / 2
            notes = note.split(';')
            tabs = tab.split(';')
            for tab, note in zip(tabs, notes):
                keys = in_key(note[:-1])
                print(keys)


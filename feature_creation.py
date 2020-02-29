import numpy as np
import csv
import re


def in_key(note):
    A = ['A', 'B', 'C+', 'D', 'E', 'F+', 'G+']
    B = ['B', 'C+', 'D+', 'E', 'F+', 'G+', 'A+']
    C = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    D = ['D', 'E', 'F+', 'G', 'A', 'B', 'C+']
    E = ['E', 'F+', 'G+', 'A', 'B', 'C+', 'D+']
    F = ['F', 'G', 'A', 'A+', 'C', 'D', 'E']
    G = ['G', 'A', 'B', 'C', 'D', 'E', 'F+']
    A_ = ['A+', 'C', 'D', 'D+', 'F', 'G', 'A']
    C_ = ['C+', 'D+', 'F', 'F+', 'G+', 'A+', 'C']
    D_ = ['D+', 'F', 'G', 'G+', 'A+', 'C', 'D']
    F_ = ['F+', 'G+', 'A+', 'B', 'C+', 'D+', 'F']
    G_ = ['G+', 'A+', 'C', 'C+', 'D+', 'F', 'G']
    Am = C
    Bm = D
    Cm = D_
    Dm = F
    Em = G
    Fm = G_
    Gm = A_
    A_m = C_
    C_m = E
    D_m = F_
    F_m = A
    G_m = B
    key_truth = []
    for i, key in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A_', 'C_', 'D_', 'F_', 'G_',
                             'Am', 'Bm', 'Cm', 'Dm', 'Em', 'Fm', 'Gm', 'A_m', 'C_m', 'D_m', 'F_m', 'G_']):
        if note in key:
            key_truth.append(True)
        else:
            key_truth.append(False)
    return key_truth


with open(data_test.csv) as file:
    csv_reader = csv.reader(file, delimiter=', ')
    line_number = 0
    for line in file:
        if line_number == 0:
            continue
        else:
            note = line[0]
            tab = line[1]
            notes_in_cluster = len(tab) / 2
            if notes_in_cluster > 1:
                print(re.split(r'\d', notes_in_cluster))

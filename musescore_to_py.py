from xml.etree import ElementTree
from ds import *


def get_key(measure, old_fifths, old_mode):
    try:
        fifths = measure.findall('attributes/key/fifths')[0].text
        mode = measure.findall('attributes/key/mode')[0].text
    except:
        fifths = old_fifths
        mode = old_mode
    if mode == 'major':
        key = major_dict.get(int(fifths))
    elif mode == 'minor':
        key = minor_dict.get(int(fifths))
    return key, fifths, mode


def adjust(note, shift):
    step = note[0]
    adj = int(shift)
    new_step = chromatic_letters[chromatic_letters.index(step) + adj].replace('_', '+')
    new_note = new_step + note[-1]
    return new_note


def muse_to_py(file):
    tree = ElementTree.parse(file)
    k, f, m = 0, 0, 0
    measures = tree.findall('part/measure')
    my_notes = []
    n = 0
    x_prev = 0
    for measure in measures:
        notes = measure.findall('note')
        for note in notes:
            x = note.attrib.get('default-x')
            k, f, m = get_key(measure, f, m)
            pitches = note.findall('pitch')
            for pitch in pitches:
                step, octave, altered = pitch.findall('step')[0].text, pitch.findall('octave')[0].text, pitch.findall('alter')
                if len(altered) > 0:
                    alter = altered[0].text
                else:
                    alter = 0
                my_note = step + str(int(octave) - 2)
                if alter != 0:
                    my_note = adjust(my_note, alter)
                if x != x_prev:
                    my_notes.append(my_note)
                    n += 1
                else:
                    my_notes[n - 1] = my_notes[n - 1] + ';' + my_note
            x_prev = x
    return my_notes


print(muse_to_py('test_xml_2.xml'))

from xml.etree import ElementTree


def get_key(measure, old):
    try:
        fifths = measure.findall('attributes/key/fifths')[0].text
    except:
        return

    return fifths

key = 0
def muse_to_py(file):
    tree = ElementTree.parse(file)
    measures = tree.findall('part/measure')
    my_notes = []
    n = 0
    x_prev = 0
    for measure in measures:
        notes = measure.findall('note')
        for note in notes:
            x = note.attrib.get('default-x')
            key = get_key(measure, key)
            print(key)
            pitches = note.findall('pitch')
            for pitch in pitches:
                step, octave = pitch.findall('step')[0].text, pitch.findall('octave')[0].text
                my_note = step + str(int(octave) - 2)
                if x != x_prev:
                    my_notes.append(my_note)
                    n += 1
                else:
                    my_notes[n - 1] = my_notes[n - 1] + ';' + my_note
            x_prev = x
    return my_notes


muse_to_py('test_xml.xml')

#!/usr/bin/python
def note(scale, note_name):
    """
    Scales may be from this scale: C  C#  D  D#  E  F  F#  G  G#  A  A#  B
    Note names are of the solfege system: Do Re Mi Fa So La Ti, etc.

    Given a scale eg, "A#" and a solfege system name eg, "Do", returns
    the corresponding note in that scale.
    """
    notes = 'C  C#  D  D#  E  F  F#  G  G#  A  A#  B'.split()
    names_offset = {
        'Do': 0,
        'Re': 2,
        'Mi': 4,
        'Fa': 5,
        'So': 7,
        'La': 9,
        'Ti': 11,
    }
    scale_start = notes.index(scale)
    res = notes[(scale_start + names_offset[note_name]) % len(notes)]
    print(f'scale: {scale}\tname: {note_name}\tresult: {res}')
    return(res)


# our test cases, from the challenge.
print(
    note("C", "Do") == "C",
    note("C", "Re") == "D",
    note("C", "Mi") == "E",
    note("D", "Mi") == "F#",
    note("A#", "Fa") == "D#",
)

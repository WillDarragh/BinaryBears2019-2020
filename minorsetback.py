freqs = [int(440 * 2**(i/12)) for i in range(-48,39)]

notes = ['A',['A#','Bb'],'B','C',['C#','Db'],'D',['D#','Eb'],'E','F',['F#','Gb'],'G',['G#','Ab']]

keys = {"G major":["G",'A','B','C','D','E','F#'],
        "C major":["C",'D',"E",'F','G','A','B'],
        "Eb major":['Eb','F','G','Ab','Bb','C','D'],
        "F# minor":['F#','G#','A','B','C#','D','E'],
        "G minor":['G','A','Bb','C','D','Eb','F']}

mynotes = []

for n in range(int(input())):
    infreq = int(float(input()))
    if infreq in freqs:
        mynotes.append(notes[freqs.index(infreq)%12])

for k,v in keys.items():
    ndex = []
    for note in mynotes:
        for n in note:
            if n not in v:
                #print(k,note)
                break
        else:
            continue
    else:
        print(k)
        for note in mynotes:
            for n in note:
                if n in v:
                    print(n)
        break
else:
    print('cannot determine key')
    
        

fname = input("Skriv filnamn:")
if len(fname) < 1:
    fname = 'datatext.txt'

artists = open(fname)
artist = dict()
erk = []
erk2 = []

for lines in artists:
    lines = lines.replace(')[', ') [')
    lines = lines.replace(' (',',(')
    lines = lines.replace(' [', ',[')
    lines = lines.replace('(','')
    lines = lines.replace(')', '')
    lines = lines.split(",")
    lines.pop()

    if len(lines) <= 1:
        continue
    else:
        erk.append(lines)
for i in range(len(erk)):
    try:
        int(erk[i][1])
        erk[i][1] = int(erk[i][1])
        erk2.append(erk[i])

    except:
        continue

for x in range(len(erk2)):
    if erk2[x][0] not in artist:
        artist[erk2[x][0]] = erk2[x][1]
    else:
        continue




artistlist = list(artist.items())
l = len(artistlist)
for i in range(l-1):
    for j in range(i+1,l):
        if artistlist[i][1] > artistlist[j][1]:
            t = artistlist[i]
            artistlist[i] = artistlist[j]
            artistlist[j] = t
    sortedartist = dict(artistlist)
print(sortedartist)

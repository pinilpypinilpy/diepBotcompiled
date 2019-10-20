with open('/Users/piotrdabkowski/PycharmProjects/ava/toy/pydiep/shoot.raw.log') as f:
    lines = f.readlines()

res = []
i = 0
while i < len(lines):
    line = lines[i]
    if not line.startswith('<'):
        i += 1
        continue
    b = ''
    while 1:
        b += ' '+ ' '.join([e for e in line.split('|')[0].split() if len(e)==2])
        i += 1
        line = lines[i]
        if not line.startswith(' '):
            print(b)
            res.append(b.strip())
            break

with open('shoot.log', 'w') as f:
    f.write('\n'.join(res))



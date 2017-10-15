import json, hashlib

class Commit:
    def __init__(self, s):
        self.id = hashlib.sha1(x).hexdigest()
        self.parents = [p[8:] for p in s.split('\n') if p.startswith('parent: ')]
        self.orig = s
        self.ref = 0

commits = {}
for x in json.loads(raw_input()):
    c = Commit(x)
    commits[c.id] = c

for c in commits.itervalues():
    for p in c.parents:
        if p in commits:
            commits[p].ref += 1

sorted_commits = []
while len(commits) > 0:
    first = [c for c in commits.itervalues() if c.ref == 0]
    sorted_commits.extend(first)

    for c in first:
        for p in c.parents:
            if p in commits:
                commits[p].ref -= 1

        del commits[c.id]

print json.dumps([c.orig for c in sorted_commits])

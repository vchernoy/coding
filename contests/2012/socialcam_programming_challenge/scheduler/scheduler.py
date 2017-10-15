import operator

class User:
    def __init__(self, uid, time):
        self._uid = uid
        self._time = time

def set_user(uid, time):
    global users, lists

    user = users.get(uid, None)
    if not user:
        user = User(uid, time)
        users[uid] = user
        lists.setdefault(time, []).append(user)
    elif user._time != time:
        l = lists[user._time]
        l.remove(user)
        user._time = time
        lists.setdefault(time, []).append(user)

def list_users(time):
    global lists

    time_lists = []
    for (t, l) in lists.iteritems():
        if t <= time:
            time_lists.append((t,l))

    time_lists.sort()
    for t,l in time_lists:
        l.sort(key=operator.attrgetter('_uid'))
        for u in l:
            print u._uid,

    print

def del_user(uid):
    global users, lists

    user = users.get(uid, None)
    if user:
        l = lists[user._time]
        l.remove(user)
        del users[uid]

def clear():
    global users, lists

    lists = {}
    users = {}

clear()
try:
    with open('./db.txt', 'r') as f:
        for s in f:
            a = [int(w) for w in s.split()]
            t = a[0]
            for uid in a[1:]:
                set_user(uid, t)

except IOError:
    pass

for i in xrange(int(raw_input())):
    s = raw_input()
    if s.startswith('set'):
        _, uid, time = s.split()
        uid = int(uid)
        time = int(time)
        set_user(uid, time)
    elif s.startswith('list'):
        _, time = s.split()
        time = int(time)
        list_users(time)
    elif s.startswith('del'):
        _, uid = s.split()
        uid = int(uid)
        del_user(uid)
    elif s.startswith('clear'):
        clear()
    else:
        assert(0) 

with open('./db.txt', 'w') as f:
    for (t, l) in lists.iteritems():
        if l:
            toks = []
            toks.append(str(t))
            for user in l:
                toks.append(' ')
                toks.append(str(user._uid))
                
            toks.append('\n')
            f.write(''.join(toks))


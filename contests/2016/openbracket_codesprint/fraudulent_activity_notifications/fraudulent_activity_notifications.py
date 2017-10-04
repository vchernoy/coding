import heapq

class Median:
    def __init__(self, cap):
        self.cap = cap
        self.min_pq = []
        self.max_pq = []
        self.all = {}
        self.index = 0
        self.min_pq_len = 0
        self.max_pq_len = 0

    def _clean(self):
        while self.min_pq and (self.min_pq[0][2] is None):
            heapq.heappop(self.min_pq)

        while self.max_pq and (self.max_pq[0][2] is None):
            heapq.heappop(self.max_pq)

    def add(self, e):
        elem = [e, self.index, [e, False]]
        self.all[self.index] = elem
        self.index += 1

        self._clean()

        if not self.min_pq and not self.max_pq:
            heapq.heappush(self.min_pq, elem)
            self.min_pq_len += 1
            return

        if e >= self.min_pq[0][2][0]:
            heapq.heappush(self.min_pq, elem)
            self.min_pq_len += 1
        else:
            elem[0] = -e
            elem[2][1] = True
            heapq.heappush(self.max_pq, elem)
            self.max_pq_len += 1

        assert len(self.all) == self.max_pq_len + self.min_pq_len

        if len(self.all) > self.cap:
            index = self.index - self.cap - 1
            y = self.all[index]
            del self.all[index]
            if y[2][1]:
                self.max_pq_len -= 1
            else:
                self.min_pq_len -= 1
            y[2] = None

            self._clean()

        while abs(self.max_pq_len - self.min_pq_len) > 1:
            if self.max_pq_len > self.min_pq_len:
                x = heapq.heappop(self.max_pq)
                x[0] = -x[0]
                x[2][1] = not x[2][1]
                heapq.heappush(self.min_pq, x)
                self.min_pq_len += 1
                self.max_pq_len -= 1
            else:
                x = heapq.heappop(self.min_pq)
                x[0] = -x[0]
                x[2][1] = not x[2][1]
                heapq.heappush(self.max_pq, x)
                self.min_pq_len -= 1
                self.max_pq_len += 1

            self._clean()

        assert len(self.all) == self.max_pq_len + self.min_pq_len

    def median(self):
        assert len(self.all) == self.cap

        self._clean()

        if self.min_pq_len < self.max_pq_len:
            x = self.max_pq[0]
            return x[2][0]

        if self.min_pq_len > self.max_pq_len:
            x = self.min_pq[0]
            return x[2][0]

        x = self.min_pq[0]
        y = self.max_pq[0]

        return (x[2][0] + y[2][0]) / 2


n, d = [int(w) for w in input().split()]
days = [int(w) for w in input().split()]

elems = Median(d)
notifications = 0
for i in range(n):
    if i >= d:
        median = elems.median()
        limit = 2 * median
        if days[i] >= limit:
            notifications += 1

    elems.add(days[i])

print(notifications)


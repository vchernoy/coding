package bathroom_stalls;

import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class BathroomStalls {

    public static final class Tuple<X, Y> {
        public final X x;
        public final Y y;

        public Tuple(X x, Y y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj.getClass() != Tuple.class) {
                return false;
            }
            Tuple<X, Y> that = (Tuple<X, Y>)obj;
            return this.x.equals(that.x) && this.y.equals(that.y);
        }

        @Override
        public int hashCode() {
            return this.x.hashCode() * 31 + this.y.hashCode();
        }
    }


    static Tuple<Long, Long> compute(final long N, final long K) {
        final TreeMap<Long, Long> m = new TreeMap<>();
        m.put(N, 1L);

        long min_d = 0, max_d = 0;
        long k = K;
        while (k > 0 && !m.isEmpty()) {
            final Map.Entry<Long, Long> e = m.lastEntry();
            final long n = e.getKey();
            final long c = e.getValue();

            m.remove(n);

            final long k0 = k < c ? k : c;
            if (n % 2 == 0) {
                final long n0 = n / 2;
                final long n1 = n0 - 1;
                if (n0 > 0) {
                    m.put(n0, m.getOrDefault(n0, 0L) + k0);
                }
                if (n1 > 0) {
                    m.put(n1, m.getOrDefault(n1, 0L) + k0);
                }
                min_d = n1;
                max_d = n0;
            } else {
                final long n0 = n / 2;
                if (n0 > 0) {
                    m.put(n0, m.getOrDefault(n0, 0L) + 2*k0);
                }
                min_d = max_d = n0;
            }
            k -= k0;
        }

        return new Tuple<>(max_d, min_d);
    }

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int ntests = reader.nextInt();
        for (int test = 1; test <= ntests; test++) {
            long N = reader.nextLong();
            long K = reader.nextLong();
            Tuple<Long, Long> res = compute(N, K);
            System.out.println("Case #" + test + ": " + res.x + " " + res.y);
        }
    }
}



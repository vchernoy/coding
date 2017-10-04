

import java.util.*;

public class RecordingEpisodes {
    private static HashSet<Integer> started = new HashSet<>();

    private static class Tuple {
        int _0 = 0;
        int _1 = 0;
        Tuple(int beg, int end) {
            this._0 = beg;
            this._1 = end;
        }

        int len() {
            return this._1 - this._0;
        }

        public String toString() {
            return "[" + _0 +"," + _1 + "]";
        }
    }

    private static class Interval {
        final int beg, end;
        Interval(int beg, int end) {
            this.beg = beg;
            this.end = end;
        }
    }
    private static class Episode {
        final Interval[] intervals = new Interval[2];
        final Interval live, repeat;
        Episode(Interval live, Interval repeat) {
            this.live = live;
            this.repeat = repeat;
            this.intervals[0] = live;
            this.intervals[1] = repeat;
        }
    }
    private static void doit(TreeMap<Integer, Interval> sol, ArrayList<Episode> E, Tuple res, Tuple best) {
        if (best.len() < res.len()) {
            best._0 = res._0;
            best._1 = res._1;
            //System.out.println("" + best);
        }
        if ((best.len() == res.len()) && (best._0 > res._0)) {
            best._0 = res._0;
            best._1 = res._1;
            //System.out.println("" + best);
        }

        if (res._1 >= E.size()) {
            return;
        }
        if (E.size() - res._0 < best.len()) {
            return;
        }
        if (E.size() - res._0 == best.len()) {
            if (res._0 >= best._0) {
                return;
            }
        }
        //System.out.println("try improve: " + res + ", best: " + best);
        Episode cur = E.get(res._1);

        Tuple res1 = new Tuple(res._0, res._1+1);
        for (int i = 0; i < 2; i++) {
            Interval i0 = cur.intervals[i];
            if (!sol.containsKey(i0.beg)) {
                Map.Entry<Integer, Interval> i1 = sol.higherEntry(i0.beg);

                if ((i1 == null) || (i0.end < i1.getValue().beg)) {
                    Map.Entry<Integer, Interval> i2 = sol.lowerEntry(i0.beg);
                    if ((i2 == null) || (i2.getValue().end < i0.beg)) {
                        sol.put(i0.beg, i0);
                        doit(sol, E, res1, best);
                        sol.remove(i0.beg);
                    }
                }
            }
        }

        if (res._0 < res._1) {
            if (!started.contains(res._1)) {
                started.add(res._1);
                TreeMap<Integer, Interval> sol2 = new TreeMap<>();
                doit(sol2, E, new Tuple(res._1, res._1), best);
            }
        }
    }

    private static Tuple solve(ArrayList<Episode> E) {
        int N = E.size();
        if (N == 1) {
            return new Tuple(1, 1);
        }

        TreeMap<Integer, Interval> sol = new TreeMap<>();

        started.clear();
        started.add(0);
        Tuple best = new Tuple(0, 0);
        doit(sol, E, new Tuple(0, 0), best);
        best._0 += 1;
        return best;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int Q = scanner.nextInt();
        //System.out.println("## Q=" + Q);
        for (int i = 0; i < Q; i++) {
            ArrayList<Episode> E = new ArrayList<>();
            int Nq = scanner.nextInt();
            //System.out.println("## " + i + " Nq=" + Nq);
            for (int j = 0; j < Nq; j++) {
                int beg0, end0, beg1, end1;
                beg0 = scanner.nextInt();
                end0 = scanner.nextInt();
                beg1 = scanner.nextInt();
                end1 = scanner.nextInt();
                Interval i1 = new Interval(beg0, end0);
                Interval i2 = new Interval(beg1, end1);
                Episode e = new Episode(i1, i2);
                E.add(e);
            }
            //System.out.println("## " + i + " solving...");
            Tuple t = solve(E);
            System.out.println(t._0 + " " + t._1);
        }
    }
}





import java.io.*;
import java.util.*;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Solution {


    private static ArrayList<Integer> solve(ArrayList<Integer> A, int N) {
        int H = 1;
        {
            int x = N;
            while (x > 1) {
                assert x % 2 == 0;
                H += 1;
                x /= 2;
            }
        }

        Map<Integer, Integer> d = new HashMap<>();
        for (int y : A) {
            d.put(y, d.getOrDefault(y, 0) + 1);
        }

        int n = N;
        ArrayList<ArrayList<Integer>> levels = new ArrayList<>();
        for (int h = H - 1; h >= 0; h--) {
            levels.add(null);
        }

        for (int h = H - 1; h >= 0; h--) {
            if (d.size() != n) {
                return null;
            }

            ArrayList<Integer> elems = new ArrayList<>(d.size());
            elems.addAll(d.keySet());

            int min_el = Collections.min(elems);

            if (d.get(min_el) != h + 1) {
                return null;
            }
            levels.set(h, elems);

            for (int x : elems) {
                d.put(x, d.get(x) - 1);
                if (d.get(x) == 0) {
                    d.remove(x);
                }
            }
            n = n / 2;
        }
        n = 2;
        for (int h = 1; h < H; h++) {
            ArrayList<Integer> pelems = levels.get(h - 1);

            Set<Integer> dset = new HashSet<>(levels.get(h));
            dset.removeAll(pelems);

            TreeSet<Integer> delems = new TreeSet<>(dset);

            ArrayList<Integer> elems = new ArrayList<>(n);
            for (int le : pelems) {
                Integer re = delems.ceiling(le);
                if (re == null) {
                    return null;
                }
                elems.add(le);
                elems.add(re);
                delems.remove(re);
            }
            levels.set(h, elems);
            n = n * 2;
        }

        ArrayList<Integer> T = new ArrayList<>();
        for (int h = 0; h < H; h++) {
            T.addAll(levels.get(h));
        }
        return T;
    }

    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        ArrayList<Integer> A = new ArrayList<>();
        for (int i = 0; i < 2*N-1; i++) {
            A.add(scanner.nextInt());
        }
//        System.out.println(A);

        ArrayList<Integer> sol = Solution.solve(A, N);
        if (sol == null) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
            String buf = sol.stream()
                    .map(Object::toString)
                    .collect(Collectors.joining(" "));

            System.out.println(buf);
        }
    }
}


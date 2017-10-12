package main

import "fmt"

const (
    M uint64 = 1000000007
    MAX_N = 500
    NO uint64 = 18446744073709551615
)

var (
    pow2 [MAX_N+1] uint64
    fact [MAX_N+1] uint64
    binom [MAX_N+1][]uint64
    tab [MAX_N+1][MAX_N+1][3] uint64
)

func _pows2() {
    //pows := make([] uint64, n + 1)
    pow2[0] = 1
    for i := 1; i <= MAX_N; i++ {
        pow2[i] = (pow2[i - 1] * 2) % M
    }
    //return pow2
}

func _factorials() {
    //fact := [n+1] uint64{}
    fact[0] = 1
    for i := 1; i <= MAX_N; i++ {
        fact[i] = (fact[i - 1] * uint64(i)) % M
    }
    //return fact
}


//func inv(x uint64) uint64 {
//    return pow(x, M - 2, M)
//}
//
//
//def _binom(n, k):
//return (fact(n) * inv(fact(k)) * inv(fact(n-k))) % M


func _binomials() {
    //binom := [n+1][]uint64{}
    binom[0] = []uint64{1}
    for i := 1; i <= MAX_N; i++ {
        binom[i] = make([]uint64, i+1)
        binom[i][0] = 1
        binom[i][i] = 1
        for j := 1; j < i; j++ {
            binom[i][j] = (binom[i - 1][j - 1] + binom[i - 1][j]) % M
        }
    }
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func F(be int, n int, m int) uint64 {
	b := 0
	e := 0
	if be == 2 {
		b = 1
		e = 1
	} else if be == 1 {
		e = 1
	}

    if m > n || be > m || n == 0 || (m == 0 && n >= 2) {
        return 0
    }

    if m == n || m <= (n - 2 + be) / 2 {
        return 0
    }

    if m == n-1 {
        if n == 1 {
            if be == 0 {
                return 1
            } else {
                return 0
            }
        }

        if be == 0 {
            return 0
        } else if be == 1 {
            return 1
        } else {
            return (pow2[n - 1] + M - 2) % M
        }
    }

    if m == n-2 {
        if be == 0 {
            return (pow2[n - 1] + M - 2) % M
        }
    }


    res := tab[n][m][be]
    if res != NO {
        return res
    }

    //assert n >= 3
    //assert 1 <= m <= n-1

    //# print('F', key)

    var (
        r, r0 uint64
    )

    if be == 0 {
        r = 2 * (F(0, n - 1, m - 1) + F(1, n - 1, m)) % M
    } else if be == 1 {
        r = F(1, n - 1, m - 1) + F(2, n - 1, m)
        if 2 <= m {
            r0 = F(0, n - 2, m - 2) + F(1, n - 2, m - 1)
        }
    } else if be == 2 {
        if 3 <= m {
            r0 = 2 * (F(1, n - 2, m - 2) + F(2, n - 2, m - 1)) % M
        }
    }

    r0 %= M
    r %= M
    r += (r0 * uint64(n-1)) % M
    r %= M

    //# print('C', r)
    for n1 := 2; n1 < n-2; n1++ {
        n2 := n - n1 - 1
        r0 = 0
        for m1 := b+1; m1 <= min(m,n1); m1++ {
            m2 := m - (m1 + 2)
            if e <= m2 && m2 <= n2 {
                r1 := F(b, n1, m1)
                if r1 > 0 {
                    r2 := F(e, n2, m2)
                    if m2 + 1 <= n2 {
                        r2 += F(1+e, n2, m2 + 1)
                    }
                    r0 += (r1 * r2) % M
                    r0 %= M
                }
            }
            if e <= m2 + 1 && m2+1 <= n2 {
                r1 := F(b+1, n1, m1)
                if r1 > 0 {
                    r2 := F(e, n2, m2 + 1)
                    if m2 + 2 <= n2 {
                        r2 += F(1+e, n2, m2 + 2)
                    }
                    r0 += (r1 * r2) % M
                    r0 %= M
                }
            }
        }
        m2 := m - (b + 2)
        if e <= m2 && m2 <= n2 {
            r1 := F(b, n1, b)
            if r1 > 0 {
                r2 := F(e, n2, m2)
                if m2 <= n2 - 1 {
                    r2 += F(1+e, n2, m2 + 1)
                }
                r0 += (r1 * r2) % M
                r0 %= M
            }
        }
        r += (r0 * binom[n - 1][n1]) % M
        r %= M
    }
    r %= M

    tab[n][m][be] = r
    //# print('F', key, ':', r)

    return r
}



func T(be int, n int, m int) uint64 {
	b := 0
	e := 0
	if be == 2 {
		b = 1
		e = 1
	} else if be == 1 {
		e = 1
	}

	if m > n || be > m || n == 0 || (m == 0 && n >= 2) {
		return 0
	}

	if m == n || m <= (n - 2 + be) / 2 {
		return 0
	}

	if m == n-1 {
		if n == 1 {
			if be == 0 {
				return 1
			} else {
				return 0
			}
		}

		if be == 0 {
			return 0
		} else if be == 1 {
			return 1
		} else {
			return (pow2[n - 1] + M - 2) % M
		}
	}

	if m == n-2 {
		if be == 0 {
			return (pow2[n - 1] + M - 2) % M
		}
	}


	res := tab[n][m][be]
	if res != NO {
		return res
	}

	//assert n >= 3
	//assert 1 <= m <= n-1

	//# print('F', key)

	var (
		r, r0 uint64
	)

	if be == 0 {
		r = 2 * (tab[n - 1][m - 1][0] + tab[n - 1][m][1]) % M
	} else if be == 1 {
		r = F(1, n - 1, m - 1) + F(2, n - 1, m)
		if 2 <= m {
			r0 = tab[n - 2][m - 2][0] + tab[n - 2][m - 1][1]
		}
	} else if be == 2 {
		if 3 <= m {
			r0 = 2 * (tab[n - 2][m - 2][1] + tab[n - 2][m - 1][2]) % M
		}
	}

	r0 %= M
	r %= M
	r += (r0 * uint64(n-1)) % M
	r %= M

	//# print('C', r)
	for n1 := 2; n1 < n-2; n1++ {
		n2 := n - n1 - 1
		r0 = 0
		for m1 := b+1; m1 <= min(m,n1); m1++ {
			m2 := m - (m1 + 2)
			if e <= m2 && m2 <= n2 {
				r1 := tab[n1][m1][b]
				if r1 > 0 {
					r2 := tab[n2][m2][e]
					if m2 + 1 <= n2 {
						r2 += tab[n2][m2 + 1][1+e]
					}
					r0 += (r1 * r2) % M
					r0 %= M
				}
			}
			if e <= m2 + 1 && m2+1 <= n2 {
				r1 := tab[n1][m1][b+1]
				if r1 > 0 {
					r2 := tab[n2][m2+1][e]
					if m2 + 2 <= n2 {
						r2 += tab[n2][m2 + 2][1+e]
					}
					r0 += (r1 * r2) % M
					r0 %= M
				}
			}
		}
		m2 := m - (b + 2)
		if e <= m2 && m2 <= n2 {
			r1 := tab[n1][b][b]
			if r1 > 0 {
				r2 := tab[n2][m2][e]
				if m2 <= n2 - 1 {
					r2 += tab[n2][m2 + 1][1+e]
				}
				r0 += (r1 * r2) % M
				r0 %= M
			}
		}
		r += (r0 * binom[n - 1][n1]) % M
		r %= M
	}
	r %= M

	tab[n][m][be] = r
	//# print('F', key, ':', r)

	return r
}

func G(n, m int) uint64 {
    r := F(0, n, m)
    r += 2 * F(1, n, m)
    r = r % M
    r += F(2, n, m)
    r = r % M
    return r
}


func query0(n, k int) uint64 {
    var r uint64
    for m := k; m < n; m++ {
        r = (r + G(n, m)) % M
    }
    return r
}

func query1(n, k int) uint64 {
    var r uint64
    for m := 0; m < k; m++ {
        r = (r + G(n, m)) % M
    }
    return (fact[n] + M - r) % M
}

func query(n, k int) uint64 {
    if k <= n * 7 / 10 {
        return query1(n, k)
    }
    return query0(n, k)
}

func main() {
    _pows2()
    _factorials()
    _binomials()


    for i := 0; i < len(tab); i++ {
        for j := 0; j < len(tab[i]); j++ {
            tab[i][j][0] = NO
            tab[i][j][1] = NO
            tab[i][j][2] = NO
        }
    }
    tab[1][0][0] = 1


	for i := 0; i < 200; i++ {
		for j := 0; j < i; j++ {
			T(0, i, j)
			//F(1, i, j)
			//F(2, i, j)
		}
	}

    fmt.Println("start")
    res := query(100, 70*1)
    fmt.Println("result")
    fmt.Println(res)

    q := 0
    fmt.Scanf("%d", &q)
    for i := 0; i < q; i++ {
        var n, k int
        fmt.Scanf("%d %d", &n, &k)
        res := query(n, k)
        fmt.Println(res)
    }
}
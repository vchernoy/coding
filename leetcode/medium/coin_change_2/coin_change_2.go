package main

func change(amount int, coins []int) int {
	i := 0
	for _, coin := range coins {
		if coin <= amount {
			coins[i] = coin
			i += 1
		}
	}
	coins = coins[0:i]
	tab := map[int]map[int]int{}
	return _change(amount, coins, tab)
}

func _change(amount int, coins []int, tab map[int]map[int]int) int {
	if amount == 0 {
		return 1
	}
	if amount < 0 || len(coins) == 0 {
		return 0
	}
	n := len(coins)

	m, ok := tab[n]
	if ok {
		r, ok := m[amount]
		if ok {
			return r
		}
	} else {
		m = map[int]int{}
		tab[n] = m
	}
	r := 0
	for i, coin := range coins {
		r += _change(amount-coin, coins[0:i+1], tab)
	}
	m[amount] = r
	return r
}

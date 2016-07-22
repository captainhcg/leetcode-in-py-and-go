type N struct{
    Rom string
    Int int
}

func intToRoman(num int) string {
    cmap_list := [] N{
        N{"M", 1000}, N{"CM", 900}, N{"D", 500}, N{"CD", 400}, N{"C", 100},
        N{"XC", 90}, N{"L", 50}, N{"XL", 40}, N{"X", 10}, N{"IX", 9},
        N{"V", 5}, N{"IV", 4}, N{"I", 1},
    }
    s := ""
    for _, n := range cmap_list {
        for num >= n.Int {
            num -= n.Int
            s += n.Rom
        }
    }
    return s
}

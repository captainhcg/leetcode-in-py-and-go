func maxProfit(prices []int) int {
    first_buy, second_buy := -2147483648, -2147483648
    first_sell, second_sell := 0, 0
    max := func(a, b int) int {
        if a > b{
            return a
        }
        return b
    }
    for _, price := range prices{
        first_buy = max(first_buy, -price)
        first_sell = max(first_sell, price + first_buy)
        second_buy = max(second_buy, -price + first_sell)
        second_sell = max(second_sell, price + second_buy)
    }
    return second_sell
}

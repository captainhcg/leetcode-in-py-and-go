func maxProfit(prices []int) int {
    if len(prices) == 0 {
        return 0
    }
    max_profit := 0
    buy_price := prices[0]
    sell_price := prices[0]
    for _, price := range prices[1:]{
        if price < buy_price {
            buy_price = price
            sell_price = price
        } else if price > sell_price {
            sell_price = price
            profit := sell_price - buy_price
            if profit > max_profit {
                max_profit = profit
            }
        }
    }
    return max_profit
}

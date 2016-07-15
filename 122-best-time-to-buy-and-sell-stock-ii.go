func maxProfit(prices []int) int {
    profit := 0 
    for idx, price := range prices{
        if idx > 0 && price > prices[idx-1]{
            profit += price - prices[idx-1]
        }
    }
    return profit
}

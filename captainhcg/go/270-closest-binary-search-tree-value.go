func closestValue(root *TreeNode, target float64) int {
    closest := root.Val
    for root != nil {
        if abs(float64(root.Val) - target) < abs(float64(closest) - target){
            closest = root.Val
        }
        if float64(root.Val) < target{
            root = root.Right
        } else{
            root = root.Left
        }
    }
    return closest
}

func abs(v float64) float64{
    if v < 0{
        return -v
    }
    return v
}

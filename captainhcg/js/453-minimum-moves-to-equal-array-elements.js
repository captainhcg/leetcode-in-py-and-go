var minMoves = function(nums) {
    if(nums.length === 0){
        return 0
    }
    const min = Math.min.apply(null, nums);
    let ret = 0;
    for(const v of nums){
        ret += v - min;
    }
    return ret
};

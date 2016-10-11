var canPartition = function(nums) {
    if(nums.length === 0){
        return true;
    }
    const sum = nums.reduce((a, b) => a + b, 0);
    if(sum % 2 == 1){
        return false;
    }
    const dp = new Array((sum >> 1) + 1);
    dp.fill(false);
    dp[0] = true;
    for(var v of nums){
        for(var i=sum >> 1; i>=0; i--){
            if(dp[i])
                continue
            if(i-v >= 0)
                dp[i] = dp[i-v]
        }
        if(dp[sum])
            return true
    }
    return dp[sum >> 1];
};

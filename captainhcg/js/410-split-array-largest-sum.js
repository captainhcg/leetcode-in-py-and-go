var splitArray = function(nums, m) {
    if(nums.length === 1){
        return nums[0];
    }
    var min = Math.max.apply(null, nums);
    var max = nums.reduce(function(a, b){ return a+b}, 0)
    var l = min, r = max, valid = max;
    var checkValid = function(sum){
        var _sum = 0, _m = 1;
        for(var n of nums){
            if(_sum + n <= sum){
                _sum += n;
            } else {
                _m += 1
                if(_m > m){
                    return false
                }
                _sum = n;
            }
        }
        return true;
    }
    while(l <= r){
        var mid = Math.ceil((l + r) / 2);
        if(checkValid(mid)){
            r = mid - 1;
            valid = mid;
        } else {
            l = mid + 1;
        }
    }
    return valid;
};

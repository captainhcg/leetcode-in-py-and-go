var twoSum = function(nums, target) {
    var map = new Map();
    for(var idx = 0; idx < nums.length; idx += 1){
        var complement = target - nums[idx];
        if(map.has(complement)){
            return [map.get(complement), idx]
        }
        map.set(nums[idx], idx);
    }
};

var sums;
var countRangeSum = function(nums, lower, upper) {
    sums = Array(nums.length + 1).fill(0);
    for(var idx=0; idx<nums.length; idx+=1){
        sums[idx+1] = sums[idx] + nums[idx];
    }
    return mergeSort(0, nums.length, lower, upper)
};

var mergeSort = function(start, end, lower, upper){
    if(end <= start){
        return 0
    }
    var mid = Math.floor((start + end) / 2)
    var count = mergeSort(start, mid, lower, upper) + mergeSort(mid+1, end, lower, upper)
    var n = mid + 1, m = mid + 1, i = start;
    for(;i<=mid;i+=1){
        while(sums[n]-sums[i] < lower && n <= end){
            n++;
        }
        while(sums[m]-sums[i] <= upper && m <= end){
            m++;
        }
        count += m - n;
    }
    var tmp = [], l = start, r = mid+1;
    while(l <= mid && r <= end){
        if(sums[l] < sums[r]){
            tmp.push(sums[l++])
        } else {
            tmp.push(sums[r++])
        }
    }
    while(l <= mid){
        tmp.push(sums[l++])
    }
    while(r <= end){
        tmp.push(sums[r++])
    }
    for(var offset = 0; offset < tmp.length; offset++){
        sums[start + offset] = tmp[offset];
    }
    return count;
}

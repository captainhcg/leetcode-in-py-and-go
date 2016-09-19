var countSmaller = function(nums) {
    var arr = []
    nums.forEach(function(n, i){
        arr.push({val: n, idx: i, smaller: 0})
    });
    var tmpArr = [];
    var mergeSort = function(start, end){
        if(start >= end){
            return
        }
        var mid = Math.floor((start + end) / 2);
        mergeSort(start, mid);
        mergeSort(mid+1, end);
        var left = start, right = mid + 1, ptr = 0;
        while (left <= mid && right <= end){
            if (arr[left].val > arr[right].val){
                arr[left].smaller += end - right + 1
                tmpArr[ptr++] = arr[left++];
            } else {
                tmpArr[ptr++] = arr[right++];
            }
        }
        while (left <= mid){
            tmpArr[ptr++] = arr[left++];
        }
        while (right <= end){
            tmpArr[ptr++] = arr[right++];
        }
        for(var idx = 0; idx < end - start + 1; idx++){
            arr[start + idx] = tmpArr[idx];
        }
    }
    mergeSort(0, nums.length-1)
    ret = Array(nums.length);
    arr.forEach(function(obj){
        ret[obj.idx] = obj.smaller;
    });
    return ret;
};

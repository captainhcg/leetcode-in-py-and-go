var numberOfArithmeticSlices = function(A) {
    var cnt = 0;
    var start = 0;
    while(start < A.length - 2){
        var add = 1;
        var end = start + 2;
        while(end < A.length && A[end] - A[end-1] === A[end-1] - A[end-2]){
            cnt += add++;
            end++;
        }
        start = end - 1;
    }
    return cnt;
};

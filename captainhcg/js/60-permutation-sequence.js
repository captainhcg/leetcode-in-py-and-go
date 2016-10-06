var getPermutation = function(n, k) {
    k = k - 1;
    var ret = "";
    var candidates = [];
    var base = 1;
    for(var i=1; i<=n; i++){
        candidates.push(i);
        base *= i;
    }
    while(candidates.length){
        base = base / candidates.length
        var to_remove = Math.trunc(k/base);
        ret += candidates[to_remove].toString();
        candidates.splice(to_remove, 1);
        k = k % base;
    }
    return ret;
};

var combinationSum2 = function(candidates, target) {
    candidates.sort(function(a, b){return a - b;})
    var arr = [];
    var ret = [];
    var helper = function(idx, lastIdx, remaining){
        if(idx >= candidates.length){
            return
        }
        var v = candidates[idx];
        if(v > remaining){
            return;
        }
        if(idx == 0 || candidates[idx] != candidates[idx-1] || idx === lastIdx + 1){
            arr.push(v)
            if(remaining - v === 0){
                ret.push(arr.slice(0))
            } else {
                helper(idx + 1, idx, remaining - v);
            }
            arr.pop()
        }
        helper(idx + 1, lastIdx, remaining)
    }
    helper(0, -1, target)
    return ret;
};

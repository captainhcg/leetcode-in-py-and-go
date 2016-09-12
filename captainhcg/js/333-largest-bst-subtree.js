var maxlen = 0;
var makeRes = function(valid){
    return {valid: valid, len: 0, min: Number.POSITIVE_INFINITY, max: Number.NEGATIVE_INFINITY}
}
var largestBSTSubtree = function(root) {
    maxlen = 0;
    var helper = function(node){
        if(node === null){
            return makeRes(true);
        }
        var left = helper(node.left);
        var right = helper(node.right);
        if(!left.valid || !right.valid || left.max > node.val || right.min < node.val){
            return makeRes(false);
        }
        var curlen = 1 + left.len + right.len;
        if(curlen > maxlen){
            maxlen = curlen;
        }
        var res = makeRes(true);
        res.min = Math.min(node.val, left.min);
        res.max = Math.max(node.val, right.max);
        res.len = curlen;
        return res;
    }
    helper(root);
    return maxlen;
};

var pathSum = function(root, sum) {
    var ret = 0
    var checkSum = function(node, currentSum, incl) {
        if(!node)
            return;
        if(node.val + currentSum === sum)
            ret += 1;
        if(!incl)
            checkSum(node.left, 0);
        checkSum(node.left, node.val + currentSum, true);
        if(!incl)
            checkSum(node.right, 0);
        checkSum(node.right, node.val + currentSum, true);
    }
    checkSum(root, 0, false)
    return ret;
};

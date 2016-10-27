var thirdMax = function(nums) {
    var a = null, b = null, c = null;
    nums.forEach(function(v){
        if (a === null || v >= a){
            if (v != a){
                c = b;
                b = a;
                a = v;
            }
        } else if (b === null || v >= b){
            if (v != b){
                c = b;
                b = v;
            }
        } else if (c === null || v >= c){
            if (v != c){
                c = v;
            }
        }
        console.log(v, a, b, c)
    })
    if (c === null){
        return a
    }
    return c;
};

var longestPalindrome = function(s) {
    var map = new Map();
    for(var idx = 0; idx < s.length; idx++){
        var ch = s.charAt(idx);
        map.set(ch, (map.get(ch) || 0) + 1);
    }
    var carry = 0, len = 0;
    for(var cnt of map.values()){
        len += (cnt >> 1) << 1
        if(cnt & 1 === 1){
            carry |= 1;
        }
    }
    return len + carry;
};

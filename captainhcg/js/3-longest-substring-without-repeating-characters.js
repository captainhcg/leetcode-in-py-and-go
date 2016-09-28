var lengthOfLongestSubstring = function(s) {
    var lastMap = new Map();
    var maxLen = 0;
    var lastIdx = -1;
    for(var idx=0; idx < s.length; idx++){
        var ch = s[idx];
        if(lastMap.has(ch)){
            lastIdx = Math.max(lastIdx, lastMap.get(ch));
        }
        lastMap.set(ch, idx);
        maxLen = Math.max(maxLen, idx - lastIdx);
    }
    return maxLen;
};

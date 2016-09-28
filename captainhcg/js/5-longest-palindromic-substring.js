var longestPalindrome = function(s) {
    if(!s){
        return 0;
    }
    var i = 0, maxLen = 0, start = 0;
    for(;i<s.length;){
        var j = i;
        while(j<s.length && s[j] == s[i]){
            j++;
        }
        var left = i, right = j - 1;
        while(s[left] == s[right] && left >= 0 && right < s.length){
            if(right - left + 1 > maxLen){
                maxLen = right - left + 1;
                start = left;
            }
            left--;
            right++;
        }
        i = j;
    }
    return s.substr(start, maxLen);
};

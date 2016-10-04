var validWordAbbreviation = function(word, abbr) {
    var p1 = 0, p2 = 0;
    var cnt = 0;
    while(p1 < word.length && p2 < abbr.length){
        var ch2 = abbr.charAt(p2);
        if (ch2 >= "0" && ch2 <= "9"){
            if(ch2 === "0" && !cnt){
                return false
            }
            cnt = cnt * 10 + parseInt(ch2, 10);
            p2 += 1
        } else {
            if (cnt){
                p1 += cnt;
                cnt = 0;
            }
            if(p1 >= word.length || word.charAt(p1) != ch2){
                return false
            }
            p1 += 1;
            p2 += 1;
        }
    }
    if(cnt){
        p1 += cnt
    }
    return Boolean(p1 === word.length && p2 === abbr.length)
};

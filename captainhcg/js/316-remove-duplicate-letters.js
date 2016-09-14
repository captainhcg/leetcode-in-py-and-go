var removeDuplicateLetters = function(s) {
	if(s.length === 0){
		return ""
	}
    var arr = new Array(26);
    for(var i=0; i < 26; i+=1){
    	arr[i] = 0;
    }
    for(var j=0; j<s.length; j++){
    	arr[s[j].charCodeAt(0)-97] += 1;
    }
    var pos = 0;
    for(var j=0; j<s.length; j++){
    	if(s[j] < s[pos]){
    		pos = j;
    	}
    	var chint = s[j].charCodeAt(0)-97;
    	arr[chint] -= 1;
    	if(arr[chint] === 0 ){
    		break;
    	}
    }
    return s[pos] + removeDuplicateLetters(s.substr(pos+1).split(s[pos]).join(""));
};

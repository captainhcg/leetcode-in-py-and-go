var validWordSquare = function(words) {
    var check = function(row){
        for(var col=0; col<words[row].length;col++){
            if(!words[col] || words[row][col] != words[col][row]){
                return false;
            }
        }
        return true
    };
    for(var i=0; i < words.length; i++){
        if(check(i) === false){
            return false
        }   
    }
    return true
};

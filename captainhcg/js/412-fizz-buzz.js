var fizzBuzz = function(n) {
    var ret = []
    for(var i=1; i <= n; i++){
        if(i % 15 == 0){
            ret.push("FizzBuzz");
        } else if(i%3 == 0){
            ret.push("Fizz");
        } else if(i%5 == 0){
            ret.push("Buzz");
        } else {
            ret.push(i.toString());
        }
    }
    return ret
};

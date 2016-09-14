var isReflected = function(points) {
    if(points.length === 0)
        return true;
    var i = 0;
    var max = Number.NEGATIVE_INFINITY, maxIdx=0;
    var min = Number.POSITIVE_INFINITY, minIdx=0;
    var nodes = {}
    for(i = 0; i < points.length; i++){
        var cor = points[i];
        nodes[cor[0] + "," + cor[1]] = true
        if(cor[0] < min){
            min = cor[0];
            minIdx = i;
        }
        if(cor[0] > max){
            max = cor[0];
            maxIdx = i;
        }
    }
    var mid = (parseFloat(max) + parseFloat(min)) / 2
    for(i = 0; i < points.length; i++){
        var cor = points[i];
        var toMap = (cor[0] - (cor[0] - mid) * 2) + "," + cor[1];
        if(!nodes[toMap])
            return false;
    }
    return true;
};

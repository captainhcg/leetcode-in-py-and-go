var findMinArrowShots = function(points) {
    points.sort(function(a, b){
        return a[1] - b[1];
    })
    let lastEnd = Number.NEGATIVE_INFINITY;
    let ret = 0;
    for(const pt of points){
        if(pt[0] > lastEnd){
            ret += 1;
            lastEnd = pt[1];
        }
    }
    return ret;
};

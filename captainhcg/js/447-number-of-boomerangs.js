var numberOfBoomerangs = function(points) {
    let ret = 0;
    let getDis = function(p1, p2){
        return Math.pow(p1[0] - p2[0], 2) + Math.pow(p1[1] - p2[1], 2);
    }
    for(let i = 0; i < points.length; i++){
        const from = points[i];
        const dis = new Map();
        for(let j = 0; j < points.length;j++){
            if(j == i){
                continue;
            }
            const to = points[j];
            const distance = getDis(from, to);
            if(!dis.has(distance)){
                dis.set(distance, 1);
            }else{
                const nums = dis.get(distance);
                ret += nums << 1;
                dis.set(distance, nums + 1);
            }
        }
    }
    return ret;
};

var minArea = function(image, x, y) {
    var up = x, down = x, left = y, right = y;
    var y1, y2, x1, x2;
    var mid, found, idx;
    
    y1 = 0, y2 = x;
    while(y1 <= y2){
        mid = parseInt((y1 + y2) / 2);
        found = false;
        for(var idx = 0; idx < image[0].length; idx += 1){
            if(image[mid][idx] === '1'){
                found = true;
                break;
            }
        }
        if(found){
            up = mid;
            y2 = mid - 1;            
        } else {
            y1 = mid + 1;
        }
    }
    
    y1 = x, y2 = image.length-1;
    while(y1 <= y2){
        mid = parseInt((y1 + y2) / 2);
        found = false;
        for(idx = 0; idx < image[0].length; idx += 1){
            if(image[mid][idx] === '1'){
                found = true;
                break;
            }
        }
        if(found){
            down = mid;
            y1 = mid + 1;            
        } else {
            y2 = mid - 1;
        }
    }
    
    x1 = 0, x2 = y;
    while(x1 <= x2){
        mid = parseInt((x1 + x2) / 2);
        found = false;
        for(idx = 0; idx < image.length; idx += 1){
            if(image[idx][mid] === '1'){
                found = true;
                break;
            }
        }
        if(found){
            left = mid;
            x2 = mid - 1;            
        } else {
            x1 = mid + 1;
        }
    }
    
    x1 = y, x2 = image[0].length-1;
    while(x1 <= x2){
        mid = parseInt((x1 + x2) / 2);
        found = false;
        for(idx = 0; idx < image.length; idx += 1){
            if(image[idx][mid] === '1'){
                found = true;
                break;
            }
        }
        if(found){
            right = mid;
            x1 = mid + 1;            
        } else {
            x2 = mid - 1;
        }
    }
    return (down - up + 1) * (right - left + 1)
};

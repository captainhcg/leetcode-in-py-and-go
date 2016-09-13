var minPatches = function(nums, n) {
	var i = 0, added = 0, missing = 1;
	while(missing <= n){
		if(nums[i] <= missing){
			missing += nums[i]
			i += 1;
		} else {
			added += 1;
			missing += missing;
		}
	}
	return added;
};

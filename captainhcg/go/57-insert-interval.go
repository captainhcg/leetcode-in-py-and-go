func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func insert(intervals []Interval, newInterval Interval) []Interval {
	ret := make([]Interval, 0)
	idx := 0
	for idx < len(intervals) {
		inv := intervals[idx]
		if inv.End < newInterval.Start {
			ret = append(ret, inv)
			idx += 1
		} else {
			break
		}
	}

	overlapStart, overlapEnd := newInterval.Start, newInterval.End
	for idx < len(intervals) {
		inv := intervals[idx]
		if inv.Start <= overlapEnd {
			overlapStart = min(overlapStart, inv.Start)
			overlapEnd = max(overlapEnd, inv.End)
			idx += 1
		} else {
			break
		}
	}
	ret = append(ret, Interval{overlapStart, overlapEnd})

	for ; idx < len(intervals); idx += 1 {
		ret = append(ret, intervals[idx])
	}
	return ret
}

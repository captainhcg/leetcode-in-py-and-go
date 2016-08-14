func isStrobogrammatic(num string) bool {
    mirrors := map[byte]byte{
        '0': '0', '1': '1', '6': '9', '8': '8', '9': '6',
    }
    st, ed := 0, len(num) - 1
    for st <= ed{
    	mirror, valid := mirrors[num[st]]
    	if !valid || mirror != num[ed]{
    		return false
    	}
    	st += 1
    	ed -= 1
    }
    return true
}

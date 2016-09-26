func reverse(input []byte) string {
	i, j := 0, len(input)-1
	for i <= j {
		input[i], input[j] = input[j], input[i]
		i += 1
		j -= 1
	}
	return string(input)
}

func toHex(num int) string {
	res := make([]byte, 0)
	for idx := 0; idx < 8; idx += 1 {
		c := num & 15
		if c < 10 {
			res = append(res, byte(c+48))
		} else {
			res = append(res, byte(97+c-10))
		}
		num >>= 4
		if num == 0 {
			break
		}
	}
	return reverse(res)
}

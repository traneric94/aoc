package utils

type Number interface {
	int | int8 | int16 | int32 | int64 |
		uint | uint8 | uint16 | uint32 | uint64 | float32 | float64
}

func Min[K comparable, V Number](n1, n2 V) V {
	if n1 > n2 {
		return n2
	}
	return n1
}

func Max[K comparable, V Number](n1, n2 V) V {
	if n1 < n2 {
		return n2
	}
	return n1
}

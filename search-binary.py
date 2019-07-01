# binary search example

def search(l, e):
	if len(l) == 0:
		return False
	else:
		mid = len(l)//2
		if l[mid] == e:
			return True
		else:
			if e < l[mid]:
				return search(l[:mid], e)
			else:
				return search(l[mid+1:], e)
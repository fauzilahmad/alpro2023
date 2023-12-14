if __name__ == "__ main__":
	tinggi = int(input('masukan tinggi: '))
	
	for x in range(1, tinggi + 1):
		for y in range(tinggi-x+1):
			print('*', end='')
		print()
		
	print('selesai')

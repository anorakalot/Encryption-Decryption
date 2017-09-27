def main():
	'''import sys
	try:
		plain_text = str(sys.argv[1])
	except IndexError:
		print("in this program you need to run the characters you want to encrypt alongside the script name itself ex. python3 (scriptname) (characters to decrypt)")
		sys.exit()'''

	plain_text = str(input("put what you want to encrypt here \n..."))

	encrypted_text = ""

	for c in plain_text:
		x = ord(c)
		x += 124
		encrypted_text += chr(x)
	print(encrypted_text)

if __name__ == "__main__":
	main()


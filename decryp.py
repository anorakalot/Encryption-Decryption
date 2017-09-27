def main():	
	'''import sys
	try:
		encrypted_text =str(sys.argv[1])
	except IndexError:
		print("you need to run the characters you want to decrpyt alongside the script name as well ex. python3 (scriptname) (characters to decrypt)")
		sys.exit()'''
	encrypted_text = str(input("put what you want to decrypt here \n..."))
	decrypted_text = ""
	for c in encrypted_text:
		x = ord(c)
		x -= 124
		decrypted_text += chr(x)
	print(decrypted_text)

if __name__ == "__main__":
	main()


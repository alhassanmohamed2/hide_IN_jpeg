
import cryptocode
import os

incrupt_key = '''/A?D(G+KbPeShVmYq3t6w9z$C&E)H@McQfTjWnZr4u7x!A%D*G-JaNdRgUkXp2s5v8y/B?E(H+MbPeShVmYq3t6w9z$C&F)J@NcRfUjWnZr4u7x!A%D*G-KaPdSgVkYp2s5v8y/B?E(H+MbQeThWmZq4t6w9z$C&F)J@NcRfUjXn2r5u8x!A%D*G-KaPdSgVkYp3s6v9y$B?E(H+MbQeThWmZq4t7w!z%C*F)J@NcRfUjXn2r5u8x/A?D(G+KaPdSgVkYp3s6v9y$B&E)H@McQeThWmZq4t7w!z%C*F-JaNdRgUjXn2r5u8x/A?D(G+KbPeShVmYp3s6v9y$B&E)H@McQfTjWnZr4t7w!z%C*F-JaNdRgUkXp2s5v8x/A?D(G+KbPeShVmYq3t6w9z$B&E)H@McQfTjWnZr4u7x!A%D*F-JaNdRgUkXp2s5v8y/B?E(H+KbPeShVmYq3t6w9z$C&F)J@NcQfTjWnZr4u7x!A%D*G-KaPdSgUkXp2s5v8'''

method_input = input('''Do you want To Encrypt or Decrypt your information from a JPEG Image File?
Type E or D ?\n''')

if not (method_input in ["D","d","E","e"]):
	print("Enter Vaild Method")
	exit()

file_name = input("Type the file name\n")
while True:
	if file_name[-4:] == '.jpg':
		break
	else:
		print("File Name is not valid Enter it again")
		file_name = input("Type the file name\n")

is_file_exist = os.path.isfile(file_name)

if is_file_exist:
	if method_input in ['E','e']:

		information = input("Input you information to Encrypt It.\n")
		encoded_information = cryptocode.encrypt(information,incrupt_key)
		with open(file_name, 'ab') as img:
		    img.write(bytes(encoded_information,encoding='utf8'))

	elif method_input in ['D', 'd']:

		with open(file_name,'rb') as img:
			content = img.read()
			offset = content.index(bytes.fromhex('FFD9'))
			img.seek(offset + 2)
			informationa = img.read()
			informationa = informationa.decode("utf8")
			decoded_information = cryptocode.decrypt(informationa , incrupt_key)
			print( "No Encrypted Inforamtion Found!" if decoded_information == False else decoded_information )
			if decoded_information:
				with open('Inforamtion.txt', 'w') as file:
					file.write(decoded_information)

else:
	print("File Not found")
	exit()

import os,random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from tkinter import *
from PIL import Image, ImageTk

def encrypt(key,filename):
	chunksize = 64*1024
	outputFile = "(criptat)"+filename
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = ''

	for i in range(16):
		IV += chr(random.randint(0, 0xFF))
	
	encryptor = AES.new(key,AES.MODE_CBC, IV)

	with open(filename, 'rb') as infile:
		with open(outputFile, 'wb') as outfile:
			outfile.write(filesize)
			outfile.write(IV)

			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += ' ' * (16 - (len(chunk) % 16))

				outfile.write(encryptor.encrypt(chunk))
def decrypt(key,filename):
	chunksize = 64*1024
	outputFile = filename[9:]

	with open(filename, 'rb') as infile:
		filesize = long(infile.read(16))
		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)
def getKey(password):
	hasher = SHA256.new(password)
	return hasher.digest()


# Main Win Options
# --------------
root = Tk()
root.title("EncryptionGUI")
root.minsize(600,500)
root.maxsize(600,500)

c2 =" CLuca"

canvas = Canvas(root, width=600, height=500)
canvas.place(x=0, y=0)

# Widgets
# --------------
search = Entry(root,width=45,bd=3)
search.place(x=50,y=75)
passw = Entry(root, width=33, show='*',bd=3)
passw.place(x=173,y=118)
status = Entry(root,width=25,bd=3,bg="#CFB6B6")
status.insert(END,"############################################")
status.place(x=50,y=385)

def criptare():
	numefisier = search.get()
	#global numef
	#numef = chr(numefisier)

	parolafisier = passw.get()
	#global parolaf
	#parolaf = chr(parolafisier)
	
	encrypt(getKey(parolafisier), numefisier)
	
	if os.path.exists(numefisier):
  		os.remove(numefisier)

def decriptare():
	numefisier = search.get()
	parolafisier = passw.get()

	decrypt(getKey(parolafisier), numefisier)

	if os.path.exists(numefisier):
  		os.remove(numefisier)



# Labels
# --------------
File_Location_text = Label(root, text="File Name",bg="#C7D2D8", font=("Verdana",10,"bold")).place(x=50,y=35)
Status_text = Label(root, text="File Status",bg="#CFB6B6", font=("Helvetica",10,"bold")).place(x=50,y=350)
Password_text = Label(root, text="Password :",bg="#C7D2D8", font=("Verdana",10,"bold")).place(x=50,y=115)
copyright = Label(root, text=c2,bg="#C7D2D8", font=("Helvetica",12)).place(x=450,y=475)


#Buttons
# --------------
# Buton_Cautare = Button(root, text=" ... ",font=("Helvetica",15), activebackground="#D5D5D5").place(x=475,y=65)
Buton_Criptare = Button(root, text="Encrypt",bg="#DF2C2C", anchor=CENTER, font=("Helvetica",17,"bold"), activebackground="#FF0000", command=criptare).place(x=150,y=175)
Buton_Decriptare = Button(root, text="Decrypt",bg="#B9FF8E", anchor=CENTER, font=("Helvetica",17,"bold"), activebackground="#46FF00", command=decriptare).place(x=300,y=175)
#Buton_Enter = Button(root, text="Enter", anchor=CENTER, font=("Helvetica",10), activebackground="#D5D5D5").place(x=400,y=400)

# Other Things
# --------------


root.mainloop()



				





































import qrcode_module.qrcodegen as qr


print("-------QRCODE_GENERATOR---------\n")
addr =  input("Insert the url page you want to transform into QRcode: ")
filename = input("\nInsert the name of your QRcode file:")

qr.generateQRcode(addr,filename)

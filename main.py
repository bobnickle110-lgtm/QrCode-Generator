import qrcode


while True:
    UrlInput = input("Enter Your (Url/Data) To Generat QrCode (to quit Enter q)>>")

    if UrlInput == "q" or UrlInput == "Q":
        break

    Output = input("For Qrcode To Be Open In Browser Press (b) / To Save The Qrcode Press (s)  >>")

     # qrcode configuration
    qr = qrcode.QRCode(
         version = 1,
         error_correction= qrcode.constants.ERROR_CORRECT_L,
         box_size= 10,
         border= 4
    )
     # add data into qrcode
    qr.add_data(UrlInput)
    qr.make(fit=True)

    cleaned_Output = Output.strip().lower()

    if Output.strip().lower() == "b":
        #create the qrcode
        img = qr.make_image(fill_color = "black", back_color = "white")
        # show qrcode in browser
        img.show()
    elif Output.strip().lower() == "s":
        img = qr.make_image(fill_color = "black", back_color = "white")
        img.save("qrcode.png")
        break
    else:
        print("Try again ! correctly")


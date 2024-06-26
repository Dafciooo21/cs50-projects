file_name = input("File name: ").lower().strip()
extension_place = file_name.rfind(".")
extension_type = file_name[extension_place:]

if extension_type == ".gif":
    print("image/gif")

elif extension_type == ".jpg" or extension_type == ".jpeg":
    print("image/jpeg")

elif extension_type == ".png":
    print("image/png")

elif extension_type == ".pdf":
    print("application/pdf")

elif extension_type == ".txt":
    print("text/plain")

elif extension_type == "zip":
    print("application/zip")

else:
    print("application/octet-stream")

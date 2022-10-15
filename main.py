import os

print("AUTO RUN IS ENABLED.")
os.system("python src/manage.py runserver 0.0.0.0:3000")
  
while True:
  print("\n")
  option = ""
  optionb = ""
  optionc = ""
  option = input("Would you like to run the server? (Y/n)")
  if option == "Y":
    os.system("python src/manage.py runserver 0.0.0.0:3000")
  else:
    optionb = input("Would you like to migrate the server? (Y/n)")
    if optionb == "Y":
      os.system("python src/manage.py makemigrations api")
      os.system("python src/manage.py migrate")
    else:
      optionc = input("Would you like to create a superuser (Y/n)")
      if optionc == "Y":
        os.system("python src/manage.py createsuperuser")
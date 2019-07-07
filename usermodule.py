def email():
            import smtplib,webbrowser,getpass
            def get():
                      serviceprovider=['gmail','hotmail','yahoo','outlook']
                      while True:
                                print("*******************************")
                                mail=input("Email  : ")
           
                                if "@" in mail and ".com" in mail:
                                       symbolpos=mail.find("@")
                                       compos=mail.find(".com")
                                       sp=mail[symbolpos+1:compos]
                                       if sp in serviceprovider:
                                                  return mail,sp
                                                  break
                                       else:
                                            print("we do not provide service for "+ str(sp))
                                            print("we only provide for ")
                                            print(serviceprovider)
                                            continue
                                else:
                                     print("Invalid E-mail")
                                     continue
            def domain(serviceprovider):
                       if serviceprovider=="gmail":
                            return "smtp.gmail.com"
                       elif serviceprovider=="outlook" or serviceprovider=="hotmail":
                            return "smtp-mail.outlook.com"
                       elif serviceprovider=="yahoo":
                              return "smtp.mail.yahoo.com"
            print("######## WELCOME TO PY-MAIL ########")
            print("         ------------------         ")
            user_mail,serviceprovider=get()
            password = getpass.getpass()
            while True:
                   try:
                       smtpdomain=domain(serviceprovider)
                       connect=smtplib.SMTP(smtpdomain,587)
                       connect.ehlo()
                       connect.starttls()
                       connect.login(user_mail,password)
                   except:
                          if serviceprovider=="gmail":
                               print("Login unsuccessful")
                               print("*******************************")
                               print("Important Note!! There may be Two Reasons for Failure. ")
                               print("1)Wrong Username or Password")
                               print("2)Access Denied by Google")
                               print("Do you want to open Webpage from where you can enable this Access")
                               answer=input("( y or n ? ) :")
                               if answer=="y":
                                     webbrowser.open("https://myaccount.google.com/lesssecureapps")
                               else:
                                   print("you can go to webpage https://myaccount.google.com/lesssecureapps to enable Access")
                                   print("Please retype your E-mail and Password for Login")
                                   user_mail,serviceprovider=get()
                                   password = getpass.getpass()
                                   continue
                          else:
                               print("Wrong Username or Password")
                               print("Please retype your E-mail and Password for Login")
                               user_mail,serviceprovider=get()
                               password = getpass.getpass()
                               continue
                   else:
                        print("Login Successfull")
                        print("*******************************")
                        break
            print("Receiver's E-mail address : ")
            r_mail,sp=get()
            subject=input("Subject : ")
            Message=input("Message : ")
            connect.sendmail(user_mail,r_mail,("Subject: " +str(subject)+"\n\n" + str(Message)))
            print("E-mail send Successfully")
            connect.quit()
                
                
                


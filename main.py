import characters as c

#gets the site name from user
site = input("Enter the sitename: ")

#gets the username from user
username = input("Enter the Username: ")

#generates a random password
password = c.password_generator()

#appends sitename, username, password in the file to save them all
with open("password_list.txt", "a") as p:
    p.write(f"Site: {site} \nUsername: {username} \nPassword: {password} \n\n")

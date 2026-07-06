import characters as c

site = input("Enter the sitename: ")
username = input("Enter the Username: ")
password = c.password_generator()

with open("password_list.txt", "a") as p:
    p.write(f"Site: {site} \nUsername: {username} \nPassword: {password} \n\n")

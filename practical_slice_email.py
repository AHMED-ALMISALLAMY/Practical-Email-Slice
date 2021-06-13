Name = input("What's your name? ").strip().capitalize()
Email = input("What 's you email? ").strip()

username = Email[0:Email.index("@")]
Domain = Email[Email.index("@") + 1: ]

print(f"Hello {Name}, Your email is {Email}")

print(f"Your Username Is {username} \nand Your Website Is {Domain}")
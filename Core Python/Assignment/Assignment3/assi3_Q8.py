# Correct User ID and Password
correct_userid = "admin"
correct_password = "1234"

# User Input
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Verify Login
if userid == correct_userid and password == correct_password:

    captcha = random . randint(1000, 9999)
    print("Captcha:", captcha)

    user_captcha = int(input("Enter the above captcha: "))

    if user_captcha == captcha:
        print("Login Successful")
    else:
        print("Captcha Verification Failed")

else:
    print("Invalid User ID or Password")
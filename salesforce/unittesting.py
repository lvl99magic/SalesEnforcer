
# test #1 
#testing the opening of json file
if 1 == 0:
    import jsonOBj as jO
    filename = "login.json"

    loginInfo = jO.openJson(filename)
    username = loginInfo['username']
    print(loginInfo['username'],loginInfo['security_token'])


# list of login ids
login_ids = ['Tom','Joe','Bob','Admin','Mary']

#list of login id requests
new_ids = ['Joe','Chuck','Scott','Beth','TOM']

#convert list of login_ids to lowercase for comparing
lower_login_ids = set(lower_login_id.lower() for lower_login_id in login_ids)

#verify new_ids don't exist in login_ids
for new_id in new_ids:
    if new_id.lower() in lower_login_ids:
        print('Login id: '+ new_id + '- That login is taken, please try another')
    else:
        print('Login id: '+ new_id + '- That login id is available')





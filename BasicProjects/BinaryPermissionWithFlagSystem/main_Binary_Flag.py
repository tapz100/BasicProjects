username = input("Enter a user name:")
permissionProvided = input(f""" 
1-Read
2-Write
3-Read+Write
4-Execute
5-Full access
Select a permission for {username}:
""")
readAccess = "1" in permissionProvided or "5" in permissionProvided or (("3" in permissionProvided and "1" in permissionProvided) or ("3" in permissionProvided and "2" in permissionProvided))
writeAccess = "2" in permissionProvided or "5" in permissionProvided or (("3" in permissionProvided and "1" in permissionProvided) or ("3" in permissionProvided and "2" in permissionProvided))
readAndWriteAccess = (False,True)[(readAccess and writeAccess) or "5" in permissionProvided]
executeAccess = "4" in permissionProvided or "5" in permissionProvided
fullAccess = (False, True)[(readAccess and writeAccess and executeAccess) 
                           or(((readAccess and readAndWriteAccess) or (writeAccess and readAndWriteAccess)) and executeAccess) 
                           or "5" in permissionProvided]

getPermissionDetails =(f"""User-{username} has below permissions:
Read access = {readAccess}
Write access = {writeAccess}
Read and Write access = {readAndWriteAccess}
Execute access = {executeAccess} 
Full access = {fullAccess}
""")

print(getPermissionDetails)
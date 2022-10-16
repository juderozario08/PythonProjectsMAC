def xyz_there(string):
    dotXYZBool = False
    for i in range(len(string)):
        if string[i:i+3] == 'xyz':
            dotXYZBool = True
            if string[i-1:i] == '.':
                dotXYZBool = False
    return dotXYZBool
print(xyz_there(""))
    
  

pathlist = []
flaglist = []
with open("path.txt") as paths:
    for path in paths.readlines():
        pathlist.append(path.strip())
with open("flag.txt") as flags:
    for flag in flags.readlines():
        flaglist.append(flag.strip())
print(pathlist)
print(flaglist)
with open("flag_file.txt","w") as flag_file:
    for path in pathlist:
        for flag in flaglist:
            flag_file.write(path+flag+"\n")

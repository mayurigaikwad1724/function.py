def function_second():
    name=["supriya","mayuri","srushti","gauri"]
    name1=["supriya","riya","rutuja","priya"]
    i=0
    while i<len(name1):
        m=name1[i]
        if m not in name:
            name.append(m)
        i=i+1
    print(name)
function_second()
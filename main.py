#https://freedict.org/freedict-database.json
try:
    
    f = open("ayasir.txt", "x")
except:print("You already have a file named ", f.name ,"try another file name. ")

for i in range (61):
    with open("ayaz.txt", "a",encoding='utf-8') as f:
        f.write("Ali Yasir ırmak " + "\n ")


f= open("ayaz.txt",encoding='utf8')
print(f.read())

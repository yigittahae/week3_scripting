from ff import *

counter = 0
for i in yasmin:
  try:
        x=i['status']
        print(type(i))
        lasti = str(i)
        print(type(i))
        if x.startswith('big'):
            counter += 1
            #print(i)
            try:
                f = open("tugrul.txt", "x")
            except:
                print("You already have a file named ", f.name, "try another file name. ")

            with open("tugrul.txt", "a") as f:
                f.write(lasti+ '\n')
        else:
            pass
  except:
        pass

  print(counter)

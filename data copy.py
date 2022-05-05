import json
import yaml

f = open("data.json", "r+")
data = json.load(f)
def end():
    wr = input("read or write?\n>")
    ask(wr)

    
def again():
 wr = input('you can only asnwer with "r" or "w".\ndo you want to read[r] or write[w]?\n>')
 ask(wr)

def read():
    name = input("enter the name of the object.\n>")
    for warehouse in data['warehouse']:
        for warehouse2 in warehouse[name]:
         print(yaml.safe_dump(warehouse2,  allow_unicode=True, default_flow_style=False))
         
    
    end()


def info():
    global location, hallway, nickname
    nickname = input('nickname:')
    location = input("location:")
    hallway = input('hallway:')
   
    

    

def write():
    print("enter the the folowing information(nickname is required, others are optional. you can skip optional ones by pressing enter):")
    for warehouse in data["warehouse"]:
     info()
     warehouse[nickname] =[{}]
     f.seek(0)
     json.dump(data, f, indent=2)
     f.truncate()
     for warehouse2 in warehouse[nickname]:
      warehouse2["location"] = location
      warehouse2["hallway"] = int(hallway)
      f.seek(0)
      json.dump(data, f, indent=2)
      f.truncate()
      end()

        


def ask(wr):
    if wr == "r":
        read()
    else:
     if wr == "w":
        write()
     else: again()




wr = input("do you want to read[r] or write[w]?\n>")
ask(wr)
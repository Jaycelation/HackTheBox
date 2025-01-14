from pwn import *

def get_index(p, answer,x):
    p.sendline(f"{x}")
    answers = []
    answer = str(p.recvuntil(b'Which character (index) of the flag do you want? Enter an index: '))
    answer = answer.split("\\n")[0].split(": ")[1]
    answers.append(answer)
    return "".join(answers)

p = remote('94.237.50.242', '51836')
rcv = str(p.recvuntil(b'Which character (index) of the flag do you want? Enter an index: '))
answers = []
p.sendline(b'1')
answer = str(p.recvuntil(b'Which character (index) of the flag do you want? Enter an index: '))
answer = answer.split("\\n")[0].split(": ")[1]
answers.append(answer)
answer=''
try:
    for x in range(180):
        answer+=get_index(p, answer, x)
        
except:
    success(f"Flag is : {answer}")
    sys.exit(0)
#                       Write Up Baby Time Capsule
#   1. Phân tích
#   Nhìn vào hàm _get_new_pubkey trên server thì ta có thể thấy đây là một câu RSA
#   Thử gửi 1 số truy vấn trên server nc 94.237.49.214 51219 -> Thông tin của "time_capsule_hex", "pubkey_hex", "5" tương ứng với 
#   n, m, e
#   Sử dụng Factordb n nhưng không ra p, q vì n là số nguyên tố -> Khả năng cao là dạng crt(Chinese Remainder Theorem)
#   2. Giải
#   Sử dụng thư viện crt của sympy để giải quyết bài toán đồng dư (Tham khảo tại https://cryptohack.org/challenges/crt1)
#   +) Add 3 request vào list rem và num -> Decode về int
#   +) Sử dụng nthroot để tìm căn bậc 5 của kết quả (e = 5)
#   +) Decode lại với long to bytes
#   Flag: HTB{t3h_FuTUr3_15_bR1ghT_1_H0p3_y0uR3_W34r1nG_5h4d35!}
import sys, json
from Crypto.Util.number import long_to_bytes
from pwn import *
from sympy.ntheory.modular import crt
from sympy.simplify.simplify import nthroot

def main():
    conn = remote('94.237.49.214', 51219)
    rem = list()
    num = list()

    for i in range(3): 
        conn.sendline(b'y')  
        r = conn.recvline()
        req = json.loads(r[74:-1].decode())
        msg = req['time_capsule']  
        pub = req['pubkey'][0] 
        e = 5  

        rem.append(int(msg, 16))  
        num.append(int(pub, 16))   

    x = crt(num, rem, check=True)

    flag = nthroot(x[0], 5)
    
    print(f'\nFlag: {long_to_bytes(flag).decode()}')

if __name__ == "__main__":
    main()
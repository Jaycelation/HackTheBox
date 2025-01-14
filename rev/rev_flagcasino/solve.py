import random

# Mảng check từ mã nguồn
check = [
    0x244B28BE, 0x0AF77805, 0x110DFC17, 0x7AFC3A1, 0x6AFEC533,
    0x4ED659A2, 0x33C5D4B0, 0x286582B8, 0x43383720, 0x55A14FC,
    0x19195F9F, 0x43383720, 0x63149380, 0x615AB299, 0x6AFEC533,
    0x6C6FCFB8, 0x43383720, 0x0F3DA237, 0x6AFEC533, 0x615AB299,
    0x286582B8, 0x55A14FC, 0x3AE44994, 0x6D7DFE9, 0x4ED659A2,
    0x0CCD4ACD, 0x57D8ED64, 0x615AB299, 0x22E9BC2A
]

# Mô phỏng hàm rand với giá trị được seed bằng v4
def my_rand(seed):
    random.seed(seed)
    return random.randint(0, 0xFFFFFFFF)  # Sinh giá trị ngẫu nhiên trong phạm vi 32-bit

# Hàm tìm ký tự v4 sao cho rand(v4) trả về giá trị check
def find_char_for_check(check_value):
    for v4 in range(32, 127):  # Duyệt từ ký tự ' ' (32) đến '~' (126)
        if my_rand(v4) == check_value:
            return chr(v4)  # Trả về ký tự phù hợp
    return None

# Lặp qua các giá trị trong mảng check và tìm ký tự v4 cho mỗi giá trị
input_chars = []
for check_value in check:
    char = find_char_for_check(check_value)
    if char:
        input_chars.append(char)
    else:
        print("Không tìm thấy ký tự cho giá trị: ", check_value)
        break

# In ra các ký tự cần nhập vào
print("Các ký tự cần nhập là: ", ''.join(input_chars))

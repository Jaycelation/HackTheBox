def decode(ct_hex):
    ct = [int(ct_hex[i:i+2], 16) for i in range(0, len(ct_hex), 2)]
    msg = []
    for value in ct:
        inverse_123 = pow(123, -1, 256)
        char = (value - 18) * inverse_123 % 256
        msg.append(chr(char))
    return ''.join(msg)

ct = '6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921'
print(decode(ct))
def Calculate_Sum(header):
    "this calculates the two-byte sum of the fields in an IPv4 header"
    decimal_sum = 0
    for i in range(len(header)):
        if i == 5: continue # skip checksum
        decimal_sum = decimal_sum + int(header[i], 16)
    checksum = (decimal_sum // 0x10000) + (decimal_sum % 0x10000)
    checksum = ~checksum & 0xffff
    return hex(checksum)[2:]

MyHeader = ["4500","0073","0000","4000","4011",
            "b861","c0a8","0001","c0a8","00c7"]
print("The two-byte sum of the header data is", Calculate_Sum(MyHeader))
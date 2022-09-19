def Verify_Checksum(header):
    return Calculate_Sum(header) == header[5]

def calculate_checksum(header):
    "this calculates the two-byte sum of the fields in an IPv4 header"
    s = sum(int(i, 16) for i in header[:5]+header[6:])
    checksum = s % 0x10000
    checksum += s // 0x10000
    checksum = ~checksum & 0xffff
    return hex(checksum)[2:]

def verify_checksum(header):
    return calculate_checksum(header) == header[5]

MyHeader = ["4500","0073","0000","4000","4011",
            "b861","c0a8","0001","c0a8","00c7"]
print("The checksum is", calculate_checksum(MyHeader))
print("Checksum verification returns", verify_checksum(MyHeader))
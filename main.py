import socket
from io import BytesIO
import pickle
from data_packet import ForzaDataPacket


# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind(("192.168.0.101", 7777))
while True:
    with open('data.bin', 'rb') as f:
        print(f.read())
# while True:
#     data, addr = sock.recvfrom(324)
#     bytesio_o = BytesIO(data)
#     with open('data.bin', 'wb') as f:
#         f.write(bytesio_o.getbuffer())
# data = b'\x01\x00\x00\x00\xef\x0e3\x01\xf6\xff\xf9E\x8c\xc3|D\x14\xc4|D\x14t\x1a;p\xefq\xb8\x86\xe4\xc69\xed\xb22\xb9\xae_\x058a\xea\xbb9\x1e\xb3\t98\xe5\x8a6\x14\xd8d97{\xdd?\x96\xc1\xa7\xbc\xe1>\xc4<\xa8\xd6\xde>\xdc@\xda>\xb3\x0e\xc3>\xe7\x17\x9f>*\xf6\x7f?H\xb6+\xbf\x82\xad\x81\xbd\xe4\x14\xb8>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\xc2\xf5=\x90\xc2\xf5=\x00\x00\x00\x00\x00\x00\x00\x00\xd1\xe8\xae\xbd\x9b\xefB\xbeL\xf1]=+\x8f\xe2=cr\x80?h~2?\x8c\xad\xaa=*\x99\xc0>\xe0\x0b\xf3;\x00\xbbb;`9#<H\x06\x94\xbc\xb6\n\x00\x00\x05\x00\x00\x00\x85\x03\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00N^\x9b\xc5\x10\xed5C\xd0\xb1\nB"\xbe\xd09s\xab[\xbd}\xc8\x04\xba\x92\x9f*C\xac\xce&C\xda\x18\x16C\xda\x18\x16Ccf0\xc1\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00W\x04\xfcD\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'
#     a = ForzaDataPacket(data)
#     att = a.get_props()
#     b = a.to_list(att)
#     for i in zip(att, b):
#         print(i)
#     print('----------------------')
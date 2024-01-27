import socket

class wmm:
    def __init__(self, modemip, bufsize=256, port=52001):
        self.ipaddr = modemip
        self.port = port
        self.bufsize = bufsize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.sock.bind(("", self.port))

    def send(self, data):
        self.sock.sendto(bytes(data), (self.ipaddr, self.port))

    def send(self, data, dest):
        self.sock.sendto(bytes([dest]+data), (self.ipaddr, self.port))

    def establish_connection(self, ipaddr="0.0.0.0", port=5000, verbose=False):
        if verbose:
            print("Establishing Connection to Edge...")
        self.sock.sendto(bytes(self.endpoint_to_bytes(ipaddr,port)), (self.ipaddr, self.port))
        data, addr = self.sock.recvfrom(self.bufsize)
        if verbose:
            if data[20] == 0:
                print("Edge Connection Failed. Check Edge or Retry Connection.")
            else:
                print("Edge Connection Succeeded! {ipaddrs}:{ports} bound to {alias}".format(ipaddrs=ipaddr, ports=port, alias = data[20]))
        return data[20]

    def endpoint_to_bytes(self, ipaddr="0.0.0.0", port=5000):
        data = []
        index = 0
        for i in range(0,3):
            end_index = ipaddr.find('.', index)
            data.append(int(ipaddr[index:end_index]))
            index = end_index + 1

        data.append(int(ipaddr[index:]))

        data.append((port & 0xff00) >> 8)
        data.append((port & 0x00ff))
        return data

    def recv(self, cut_header=True):
        data, addr = self.sock.recvfrom(self.bufsize)
        if cut_header:
            return data[14:], addr, data[1]
        else:
            return data, addr, data[1]

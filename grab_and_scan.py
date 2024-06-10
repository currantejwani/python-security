from timer import timefunc
from port_scanner import Scanner
from banner_grabber import Grabber

@timefunc
def main():
    ip = '192.168.0.243'
    portrange = (1, 1001)
    scanner = Scanner(ip)
    scanner.scan(*portrange)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip, port)
            print(grabber.read())
            grabber.close()
        except Exception as e:
            print("Error", e)


if __name__ == '__main__':
    main()



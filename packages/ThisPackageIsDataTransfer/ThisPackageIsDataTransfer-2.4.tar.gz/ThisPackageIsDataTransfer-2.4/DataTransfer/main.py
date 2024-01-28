from optparse import OptionParser

from DataTransfer.network.network import SenderNetwork, ReceiverNetwork
from DataTransfer.transferer.sender import SenderTransferer
from DataTransfer.transferer.receiver import ReiceiverTransferer


def return_arguments():

    parser = OptionParser()

    parser.add_option('--sender', dest='sender', action='store_true', help='enable sender mode')
    parser.add_option('--receiver', dest='receiver', action='store_true', help='enable receiver mode')
    parser.add_option('-p', '--port', dest='port', type=int, help='specify the port number')
    parser.add_option('-i', '--ip', dest='ip', help='specify the ip address')
    parser.add_option('-m', '--max_receiver', dest='max_receiver', type=int, help='set the maximum number of receivers')
    parser.add_option('-l', '--limited_size', dest='limited_size', type=int, help='set the limited size of each file')
    options = parser.parse_args()[0]

    check_arguments(options, parser)

    return options


def check_arguments(options, parser):

    if not options.sender and not options.receiver:
        parser.error('[-] Role not found')

    if options.sender and options.receiver:
        parser.error('[-] One role only "--send" or "--receive"')

    if not options.port:
        parser.error('[-] Port not found')

    if not options.ip:
        parser.error('[-] Ip address not found')

    if not options.max_receiver and options.sender:
        parser.error('[-] Maximum receiver not found')


def run_sender(ip, port, max_receiver, limited_size):

    network = SenderNetwork(ip, port)
    sender = SenderTransferer(network, max_receiver, limited_size)
    sender.run()


def run_receiver(ip, port):

    network = ReceiverNetwork(ip, port)
    receiver = ReiceiverTransferer(network)
    receiver.run()


def main():

    options = return_arguments()

    ip = options.ip
    port = options.port
    max_receiver = options.max_receiver if options.max_receiver else 1
    limited_size = options.limited_size if options.limited_size else 8000000


    if options.sender:
        run_sender(ip, port, max_receiver, limited_size)

    elif options.receiver:
        run_receiver(ip, port)


if __name__ == '__main__':
    main()

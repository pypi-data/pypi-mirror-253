import os
import threading
import time 

from base64 import b64encode


class SenderTransferer:

    def __init__(self, network, maximum_receivers, limited_size):

        self._server = network.server
        self._network = network
        self._current_dir_path = os.getcwd()
        self._maximum_receivers = maximum_receivers
        self._limited_size = limited_size


    def _wait_for_previous_sending(self, interval):
        
        time.sleep(interval)


    def _read_file(self, path):

        with open(path, 'rb') as file:
            return b64encode(file.read()).decode()


    def _send_file(self, connection, file_path):

        file_name = file_path.replace(self._current_dir_path, '')
        file_content = self._read_file(file_path)

        self._network.send(connection, ('file', file_name, file_content))


    def _send_dir(self, connection, dir_path):

        dir_name = dir_path.replace(self._current_dir_path, '')
        self._network.send(connection, ('dir', dir_name))

    
    def _check_size(self, file_path):

        size = os.path.getsize(file_path)
        return True if size < self._limited_size else False


    def _transfer(self, connection, dir_path):

        for path in os.listdir(dir_path):

            full_path = os.path.join(dir_path, path)

            if os.path.isfile(full_path) :

                if self._check_size(full_path):
                    print('[>]', full_path)
                    self._send_file(connection, full_path)
                    self._wait_for_previous_sending(0.5)

            else:
                self._send_dir(connection, full_path)
                self._wait_for_previous_sending(0.5)
                child_dir_path = dir_path + '/' + path
                self._transfer(connection, child_dir_path)


    def _stop_transfer(self, connection):

        self._network.send(connection, ('break',))
        self._wait_for_previous_sending(0.5)

        connection.close()


    def _handle(self, connection):

        self._transfer(connection, self._current_dir_path) 
        self._stop_transfer(connection)

    
    def _init_handling_thread(self, connection):

        handling_thread = threading.Thread(target=self._handle, args=(connection,))
        handling_thread.start()


    def run(self):

        print('[+] Listening for incoming connecions...')

        num_receiver = 0
        while True:

            connection, _ = self._server.accept()

            print('[+] Got a new connection')
            self._init_handling_thread(connection)

            num_receiver = num_receiver + 1
            if num_receiver == self._maximum_receivers:
                break

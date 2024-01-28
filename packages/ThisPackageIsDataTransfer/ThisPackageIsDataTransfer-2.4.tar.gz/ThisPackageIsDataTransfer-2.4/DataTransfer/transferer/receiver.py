import os

from base64 import b64decode


class ReiceiverTransferer:

    def __init__(self, network):
        self.network = network
        self.current_dir_path = os.getcwd()


    def _write_file(self, file_name, file_content):

        file_path = self.current_dir_path + file_name
        with open(file_path, 'wb') as file:

            file.write(b64decode(file_content))


    def _make_dir(self, dir_name):

        dir_path = self.current_dir_path + '/' + dir_name
        if not os.path.exists(dir_path):

            os.mkdir(dir_path)
            

    def run(self):

        while True:

            content = self.network.receive()

            if content[0] == 'break':
                break

            elif content[0] == 'file':

                _, file_name, file_content = content

                self._write_file(file_name, file_content)
                print(f'[+] {file_name}')


            elif content[0] == 'dir':
                
                dir_name = content[1]
                self._make_dir(dir_name)

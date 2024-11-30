import argparse
import mailboxTools
from mfrc522 import SimpleMFRC522



valid_commands = ['log_out', 'q', 'add_id', 'get_id', 'search_id', 'delete_id', 'log_in']

def command_is_valid(command):
    if command in valid_commands:
        return True

    else:
        print('Valid commands are {}'.format(valid_commands))
        return False

def main():
    mfrc = SimpleMFRC522()
    while(1):
        try:
            id, not_id = mfrc.read()
            print(id)
            break
        except:
            continue

    mailbox_client = mailboxTools.mailboxClient(args.u, args.a, id)

    usr_input = ''
    command = ''

    while command != 'q':
        while not command_is_valid(usr_input):
            usr_input = input('Command: ')
            command = usr_input

#        if command == 'log_in':
#           try:
#                id, not_id = mfrc.read()
#                print(id)
#                mailbox_client.log_in(id)
#            except:
#                continue
 
        if command == 'log_out':
            break


        if command == 'add_id':
            address = args.a

            while(1):
                try:
                    id, not_id = mfrc.read()
                    break
                except:
                    continue

            try:
                mailbox_client.add_id(address, id)

            except Exception as e:
                print(e)

        if command == 'get_id':
            mailbox_client.get_id()

        if command == 'search_id':
            field = input('Search field (optional): ')
            field = field if field != '' else None

            text = input('Search text: ')
            text = text if text != '' else None

            mailbox_client.search_id(field, text)

        if command == 'delete_id':
            print('Please enter the ids you wish to delete')
            print("Enter 'done' when complete")
            ids = []
            delete_input = ''

            while delete_input != 'done':
                try:
                    delete_input = input('ID: ')

                    if delete_input == 'done':
                        break

                    ids.append(int(delete_input))

                except ValueError:
                    print("Please enter an integer or 'done' if complete")

            mailbox_client.delete_id(ids)

        print('')
        usr_input = ''
        print('logging out')
        main()
        
    return 0

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='mailClient',
            description='Script to send and read emails')

    parser.add_argument('-a', metavar='ip_addr:port_num', required=True,
            help="Address of the server in the format ip_addr:port_num")

    parser.add_argument('-u', metavar='username', required=True,
            help="Username to go by when sending emails")

    args = parser.parse_args()

    main()


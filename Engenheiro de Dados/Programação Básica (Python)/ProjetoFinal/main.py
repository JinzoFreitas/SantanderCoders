import locadora_do_zé
import os
import argparse

def args(sistema):
    parser = argparse.ArgumentParser()

    parser.add_argument('-add', '--register', nargs='+', help='Register n* movies in the collection')
    parser.add_argument('-rem', '--remove', nargs='+', help='Removes n* movies in the collection')
    parser.add_argument('-u', '--update', nargs='+', help='Updates n* movies titles in the collection')
    parser.add_argument('-q', '--query', help='Searches for movies in the collection containing the query')
    parser.add_argument('-s', '--status', nargs='+', help='Sets the status of n* movies in the collection')
    parser.add_argument('--reset', action='store_true', help='Clear the whole collection')
    parser.add_argument('-d', '--display', action='store_true', help='Shows all the movies in the collection')

    args = parser.parse_args()

    if args.register:
        sistema.register(args.register)
    if args.remove:
        sistema.remove(args.remove)
    if args.update:
        for i in range(0, len(args.update), 2):
            sistema.update(args.update[i], args.update[i+1])
    if args.query:
        sistema.search(args.query)
    if args.status:
        for i in range(0, len(args.status), 2):
            sistema.set_status(args.status[i], args.status[i+1])
    if args.reset:
        sistema.reset_collection()
    if args.display:
        sistema.show_collection()


def main():
    #clear screen
    os.system('clear')
    #instantiates the program
    sistema = locadora_do_zé.locadora()
    #gets all the args
    args(sistema)

if __name__=='__main__':
    main()

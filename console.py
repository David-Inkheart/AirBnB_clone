#!/usr/bin/python3
'''
program called console.py that contains
the entry point of the command interpreter
'''


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    '''
    commandline interface to manage data
    '''
    intro = None
    prompt = '(hbnb) '
    file = None

    ''' ------basic console commands----- '''

    def do_EOF(self, line):
        '''Clear the screen and return to prompt:  EOF'''
        print()
        return True

    def do_quit(self, arg):
        '''close the console, and exit:  QUIT'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

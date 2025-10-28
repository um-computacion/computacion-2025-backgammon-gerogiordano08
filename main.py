from cli.cli import CLI
from pygame_ui.app import UI 
def main():
    command_line_interface = CLI()
    command_line_interface.cmdloop()

if __name__ == '__main__':
    main()
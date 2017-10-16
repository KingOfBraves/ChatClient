import curses


def main(stdscr):
    newline = False
    userinput = ""
    chatlog = []
    # Clear screen
    begin_x = 0; begin_y = 0
    height = 24; width = 80
    stdscr = curses.newwin(height, width, begin_y, begin_x)
    myscreen = curses.initscr()
    stdscr.border(0)
    stdscr.addstr(0, 0, "Python curses in action!")
    stdscr.refresh()

    while not newline:
        newchar = stdscr.getch()
        if chr(newchar) == '\n':
            chatlog.append(userinput)
            userinput = ""
            clear_user_input(stdscr)
            update_screen(stdscr, chatlog)
        else:
            userinput = userinput + chr(newchar)
            stdscr.addstr(22, 1, ">" + userinput)
            stdscr.refresh()

def user_input():
    print "test"

def clear_user_input(stdscr):
    stdscr.addstr(22, 1, ">                     ")
    stdscr.refresh()

def update_screen(stdscr, chatlog):
    height = 1
    for chat in chatlog:
        stdscr.addstr(height, 1, chat)
        height = height + 1

if __name__ == '__main__':
    curses.wrapper(main)

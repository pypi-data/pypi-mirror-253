import threading
import textwrap3
import time
import os
import traceback
import queue
from io import StringIO

from prompt_toolkit import Application
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings

from chemscripts.mylogging import createLogger


class CustomStringIO(StringIO):
    def __init__(self, *args, func=None, cleanup: bool=False, **kwargs):
        self.func = func
        self.cleanup = cleanup
        super().__init__(*args, **kwargs)

    def write(self, *args, **kwargs):
        if self.cleanup:
            self.truncate(0)
            self.seek(0)
        super().write(*args, **kwargs)
        self.func(self.getvalue())


kb = KeyBindings()
@kb.add('c-c')
def exit_(event):
    event.app.exit()

left_panel = FormattedTextControl("")
right_panel = FormattedTextControl("")

left_window = Window(left_panel)
right_window = Window(right_panel)
root_container = VSplit([
    left_window,
    Window(width=1, char='|'),
    right_window,
])

layout = Layout(root_container)

app = Application(layout=layout, key_bindings=kb, refresh_interval=0.05, full_screen=True)

def run_app():
    app.run()


def get_terminal_size():
    try:
        # Get terminal size using the 'stty' command (Unix-based systems)
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(rows), int(columns)
    except:
        pass

    try:
        # Get terminal size using the 'ioctl' system call (Windows)
        import struct
        from fcntl import ioctl
        from termios import TIOCGWINSZ

        fd = os.open(os.ctermid(), os.O_RDONLY)
        size = struct.unpack('hh', ioctl(fd, TIOCGWINSZ, '1234'))
        os.close(fd)
        return size[0], size[1]
    except OSError:
        pass

    # Fallback in case both methods fail
    return 30, 120

NUM_LINES = int(get_terminal_size()[0])
WIDTH = int((get_terminal_size()[1] - 2) / 2)

def wrap_text(t: str) -> str:
    x = '\n'.join([
        textwrap3.fill(line, width=WIDTH)
        for line in t.splitlines()
    ])
    return '\n'.join(x.splitlines())


def custom_update(panel_name, show_part):
    if panel_name == 'left':
        panel = left_panel
    elif panel_name == 'right':
        panel = right_panel
    else:
        raise RuntimeError(f"Unknown panel '{panel_name}'")

    if show_part == 'top':
        cropping_function = lambda text: '\n'.join(text.splitlines()[:NUM_LINES])
    elif show_part == 'bottom':
        cropping_function = lambda text: '\n'.join(text.splitlines()[-NUM_LINES:])
    else:
        raise RuntimeError(f"Unknown cropping setting '{show_part}'")
    
    def update_function(newtext: str) -> None:
        panel.text = cropping_function(wrap_text(cropping_function(newtext)))
    return update_function


def execute_with_ui(main_function):
    logger_stream = CustomStringIO(func=custom_update(panel_name='right', show_part='bottom'))
    main_logger = createLogger("Main", logger_stream)
    stack_stream = CustomStringIO(func=custom_update(panel_name='left', show_part='top'), cleanup=True)

    app_thread = threading.Thread(target=run_app)
    app_thread.start()
 
    exception_queue = queue.Queue()
    def run_main():
        try:
            main_function(main_logger, stack_stream)
        except:
            exception_queue.put(traceback.format_exc())

    work_thread = threading.Thread(target=run_main)
    work_thread.start()
    work_thread.join()

    time.sleep(0.3)
    app.exit()
    app_thread.join()

    print(logger_stream.getvalue())

    if not exception_queue.empty():
        exception = exception_queue.get()
        print(f"Worker thread raised an exception:\n{exception}")

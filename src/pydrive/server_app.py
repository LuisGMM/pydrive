
from concurrent.futures import ThreadPoolExecutor

from pydrive.gui import gui_server


with ThreadPoolExecutor() as pool:
    pool.submit(gui_server.main)

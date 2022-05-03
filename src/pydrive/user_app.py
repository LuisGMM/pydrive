
from concurrent.futures import ThreadPoolExecutor
from pydrive.core import user


with ThreadPoolExecutor() as pool:
    pool.submit(user.main)

import numpy as np
import pandas as pd
import os
from time import sleep
from shutil import rmtree
from cache_decorator import Cache
from .utils import standard_test_dataframes

@Cache(
    cache_path="{cache_dir}/{_hash}.csv.xz",
    cache_dir="./test_cache",
    backup=False,
)
def cached_function(a):
    sleep(2)
    return pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))

def test_csv_xz():
    standard_test_dataframes(cached_function)
    if os.path.exists("./test_cache"):
        rmtree("./test_cache")

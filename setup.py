from cx_Freeze import setup, Executable
import os.path

executables = [
    Executable(
        "rc_profit_calc.py",
        base=None,
        targetName="Rollercoin Profit Calculator.exe"
        #icon="icon.ico"
    )
]

options = {
    'build_exe': {
        'packages': ["os"],
        'optimize': 2,
        'include_files': []
        }
    }

setup(
    options=options,
    name="Rollercoin Profit Calculator",
    version="0.0.3",
    description="Calculator that allows you to determine which cryptocurrency "
                "is the most profitable to mine on the rollercoin.com site",
    executables=executables
    )

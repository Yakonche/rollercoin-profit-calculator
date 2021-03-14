import os.path

from cx_Freeze import setup, Executable, build
from babel.messages import frontend as babel


class BuildWithCompile(build):
    def run(self):
        compiler = babel.compile_catalog(self.distribution)
        compiler.domain = ["rc_profit_calc"]
        compiler.directory = "./locale"
        compiler.run()
        super().run()


def list_mo_files(folder, domain):
    mo_files = []
    for locale in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, locale)):
            mo_files.append(os.path.join(folder, locale, "LC_MESSAGES", domain + ".mo"))
    return mo_files


SRC_PATH = os.path.dirname(__file__)

include_files = [
    (os.path.join(SRC_PATH, './locale'), 'locale/'),
]

for mo_file in list_mo_files("locale", "rc_profit_calc"):
    include_files.append(
        (os.path.join(SRC_PATH, mo_file), mo_file),
    )


executables = [
    Executable(
        "rc_profit_calc.py",
        base=None,
        targetName="Rollercoin Profit Calculator.exe",
        icon="icon.ico"
    )
]

options = {
    'build_exe': {
        'packages': ["os"],
        'optimize': 2,
        'include_files': include_files
    }
}

setup(
    options=options,
    name="Rollercoin Profit Calculator",
    version="0.0.5",
    description="Calculator that allows you to determine which cryptocurrency "
                "is the most profitable to mine on the rollercoin.com site",
    executables=executables,
    cmdclass={
        'build': BuildWithCompile,
        'compile_catalog': babel.compile_catalog,
        'extract_messages': babel.extract_messages,
        'init_catalog': babel.init_catalog,
        'update_catalog': babel.update_catalog
    }
)

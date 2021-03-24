import os.path

from distutils.cmd import Command
from cx_Freeze import setup, Executable, build
from babel.messages import frontend as babel

WIN_NT = os.name == "nt"

catalogs = [
    "en_US", "fr_FR", "de_DE", "es_ES", "pl_PL", "pt_PT", "tr_TR", "ru_RU",
    "fil_PH"
]


class CommandAdapter(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class InitAll(CommandAdapter):
    description = "Initialise all translation catalogs"

    def run(self):
        for catalog in catalogs:
            babel_ic = babel.init_catalog(self.distribution)
            babel_ic.initialize_options()

            babel_ic.locale = catalog
            babel_ic.input_file = "locale/rc_profit_calc.pot"
            babel_ic.output_dir = "locale"
            babel_ic.output_file = "locale/{}/LC_MESSAGES/rc_profit_calc.po".format(catalog)

            babel_ic.finalize_options()
            babel_ic.run()


class UpdateAll(CommandAdapter):
    description = "Update all translation catalogs"

    def run(self):
        for catalog in catalogs:
            babel_uc = babel.update_catalog(self.distribution)
            babel_uc.initialize_options()

            babel_uc.locale = catalog
            babel_uc.input_file = "locale/rc_profit_calc.pot"
            babel_uc.output_dir = "locale"
            babel_uc.output_file = "locale/{}/LC_MESSAGES/rc_profit_calc.po".format(catalog)

            babel_uc.finalize_options()
            babel_uc.run()


class CompileAll(CommandAdapter):
    description = "Compile all translation catalogs"

    def run(self):
        babel_cc = babel.compile_catalog(self.distribution)
        babel_cc.domain = ["rc_profit_calc"]
        babel_cc.directory = "./locale"
        babel_cc.run()


class BuildWithCompile(build):
    def run(self):
        babel_cc = babel.compile_catalog(self.distribution)
        babel_cc.domain = ["rc_profit_calc"]
        babel_cc.directory = "./locale"
        babel_cc.run()
        super().run()


class ExtractMessages(CommandAdapter):
    description = "Extract translation messages"

    def run(self):
        babel_em = babel.extract_messages(self.distribution)
        babel_em.initialize_options()

        babel_em.input_dirs = "."
        babel_em.output_file = "locale/rc_profit_calc.pot"

        babel_em.finalize_options()
        babel_em.run()


def list_mo_files(folder, domain):
    mo_files = []
    for locale in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, locale)):
            mo_files.append(os.path.join(folder, locale, "LC_MESSAGES",
            domain + ".mo"))
    return mo_files


SRC_PATH = os.path.dirname(__file__)

include_files = []
for mo_file in list_mo_files("locale", "rc_profit_calc"):
    include_files.append(
        (os.path.join(SRC_PATH, mo_file), mo_file),
    )

target_name = "Rollercoin Profit Calculator.exe" if WIN_NT else "rollercoin-profit-calculator"
executables = [
    Executable(
        "rc_profit_calc.py",
        base=None,
        targetName=target_name,
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
    version="0.1.2",
    description="Calculator that allows you to determine which cryptocurrency"
                " is the most profitable to mine on the rollercoin.com site, "
                "with an estimate by block, hour, day, month, year. 45 fiat "
                "currencies and 13 cryptocurrencies available.",
    executables=executables,
    cmdclass={
        'build': BuildWithCompile,
        'compile_catalogs': CompileAll,
        'extract_messages': ExtractMessages,
        'init_catalogs': InitAll,
        'update_catalogs': UpdateAll
    }
)

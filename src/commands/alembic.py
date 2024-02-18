from argparse import Namespace

from alembic.config import Config as AlembicConfig
from alembic.config import CommandLine
from src.config import Config


class CustomCommandLine(CommandLine):
    def run_cmd(self, config: Config, options: Namespace) -> None:
        config = AlembicConfig(Config().BASE_DIR / 'src' / 'sqlalchemy_db' / 'alembic.ini')
        config.set_main_option("script_location", "src.sqlalchemy_db:migrations")
        super().run_cmd(config, options)


def entrypoint(*argv):
    CustomCommandLine().main(argv=argv)

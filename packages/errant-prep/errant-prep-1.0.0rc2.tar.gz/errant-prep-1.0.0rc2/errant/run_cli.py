import os
from warnings import filterwarnings

import click

from nlp_evaluator.cli.initial import init
from nlp_evaluator.cli.submision import submission
from nlp_evaluator.cli.data import data

from errant.config import __version__
from loguru import logger


filterwarnings("ignore")

PRJ_DIR = os.getcwd()


@click.group()
def entry_point():
    pass


@click.command()
def version():
    print(f"version: {__version__}")
    return __version__


@click.command()
@click.option('--config_path', '-p',
              help="The path of config file",
              default="nlp-bench/config/config.yaml",
              type=str)
def evaluate(config_path):
    from nlp_evaluator.components import run_evaluation
    run_evaluation(config_path)


entry_point.add_command(version)
entry_point.add_command(init)
entry_point.add_command(evaluate)
entry_point.add_command(data)
entry_point.add_command(submission)
if __name__ == '__main__':
    entry_point()

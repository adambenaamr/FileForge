import os
import click
from ff.core import rename_media_files

# Ensures the CLI starting command is 'ff'
@click.command()

# Options and arguments for file renaming feature
@click.option('--rename', is_flag=True, help='Command to rename files iteritvely in a given directory')
@click.argument('input_directory') # Allows './' to mean the current working directory
@click.argument('output_directory') # Allows './' to mean the current working directory
@click.option('--starting', default=0, type=int, help='Starting index')
@click.option('--dry-run', is_flag=True, help='Show what would be renamed without performing any moves')

def main(rename, input_directory, output_directory, starting, dry_run) -> None:
  """
  FileForge CLI a python CLI tool for batch file renaming and other
  useful utilities when it comes to file organization
  """
  # Follows the form of: `ff ./ ./ --rename --starting=_____ --dry-run`
  input_directory = os.path.abspath(input_directory)
  output_directory = os.path.abspath(output_directory)

  if rename:
    rename_media_files(input_directory=input_directory, output_directory=output_directory, counter=starting, dry_run=dry_run)

if __name__ == "__main__":
  main()

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

def main(rename, input_directory, output_directory, starting) -> None:
  """
  FileForge CLI Tool
  """
  if rename:
    # Follows the form of: `ff ./ ./ --rename --starting=_____`
    input_directory = os.path.abspath(input_directory)
    output_directory = os.path.abspath(output_directory)
    
    rename_media_files(input_directory=input_directory, output_directory=output_directory, counter=starting)
  
  # input_directory = input("Enter the input directory path: ").strip()
  # output_directory = input("Enter the output directory path: ").strip()
  
  # if not os.path.isdir(input_directory):
  #   print("Error: Input directory does not exist.")
  # else:
  #   rename_media_files(input_directory, output_directory)
  #   print("Done.")

if __name__ == "__main__":
  main()

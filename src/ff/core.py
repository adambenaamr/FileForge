import os
import shutil
from natsort import natsorted
from .utils import OutputBox

def get_unique_filename(directory: str, base_name: str, extension: str) -> str:
  """
  Generates a unique filename within a specified directory by appending a counter.

  This function checks if a file with the given base name and extension already
  exists in the target directory. If it does, it iteratively appends an
  underscore and an incrementing integer (e.g., '_1', '_2') until a
  non-conflicting filename is found.
  
  :param directory: The filesystem path where the file will be located.
  :type directory: str
  
  :param base_name: The desired filename without the extension.
  :type base_name: str
  
  :param extension: The file extension, including the leading dot (e.g., '.txt').
  :type extension: str

  :return new_name: A string representing a unique filename that does not currently
  exist in the specified directory.
  """
  new_name: str = f'{base_name}{extension}'
  counter: int = 1

  while os.path.exists(os.path.join(directory, new_name)):
    new_name: str = f'{base_name}_{counter}{extension}'
    counter += 1
  
  return new_name

def rename_media_files(input_directory: str, output_directory: str, counter: int = 0, dry_run: bool = False) -> None:
  """
  Rename and move image and video files from a source to a destination.

  This function scans a directory for common media extensions, sorts them
  numerically (handling non-numeric filenames gracefully), and renames
  them using a standardized 'IMG_xxxx' or 'MOV_xxxx' prefix before
  moving them to the specified output directory.

  :param input_directory: The path to the folder containing the original media files.
  :type input_directory: str
  
  :param output_directory: The path where renamed files will be moved. Created if it doesn't exist.
  :type output_directory: str
  
  :param counter: The starting index for the file naming sequence. Defaults to 0.
  :type counter: int, optional

  :param dry_run: The flag used to show a preview of file changes without actually changing the files.
  :type dry_run: bool
  """
  image_extensions: set[str] = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.heic'}
  video_extensions: set[str] = {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.mpeg'}
  
  # Ensure output directory exists
  os.makedirs(output_directory, exist_ok=True)
  
  # Get files within directory in accordance to OS specifications (the way the OS decides to list the files)
  files: list[str] = [
    f for f in os.listdir(input_directory)
    if os.path.isfile(os.path.join(input_directory, f))
  ]

  # Order the files list alphabetically
  # Since OSes define capital letters as dominatant (i.e., 'S' will come before 'a')
  # this variable converts the files names to all lowercase letters
  # then organized them alphabetically
  files_sorted: list[str] = natsorted(sorted(files, key=str.lower))
  
  # Filter and sort numerically
  ordered_media: list = []
  
  for file in files_sorted:
    _, ext = os.path.splitext(file)
    
    if ext.lower() in image_extensions.union(video_extensions):
      ordered_media.append(file)
  
  def safe_int(name) -> (int | float):
    try:
      return int(os.path.splitext(name)[0])
    except ValueError:
      return float('inf')
  
  ordered_media.sort(key=safe_int)
  
  operations: list = []

  for file in ordered_media:
    old_path: str = os.path.join(input_directory, file)
    _, ext = os.path.splitext(file)
    ext = ext.lower()
      
    if ext in image_extensions:
      base_name: str = f'IMG_{counter:04d}' # TODO: change this so that there is a variable called 'digit' where the user can define how many digits of numbers they want after the base name
    elif ext in video_extensions:
      base_name: str = f'IMG_{counter:04d}' # TODO: change this so that there is a variable called 'digit' where the user can define how many digits of numbers they want after the base name
    else:
      continue
      
    final_name: str = get_unique_filename(output_directory, base_name, ext)
    final_path: str = os.path.join(output_directory, final_name)
    
    operations.append((old_path, final_path, file, final_name))
    
    counter += 1

  with OutputBox() as terminal_output:
    for old_path, final_path, original_file_name, new_file_name in operations:
      if dry_run:
        terminal_output.print(f'[DRY RUN] {original_file_name} -> {new_file_name}')
      else:
        shutil.move(old_path, final_path)
        terminal_output.print(f'Renamed: {original_file_name} -> {new_file_name}')

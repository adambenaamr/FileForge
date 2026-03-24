import os
import shutil

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
    new_name = f'{base_name}_{counter}{extension}'
    counter += 1
  
  return new_name

def rename_media_files(input_directory: str, output_directory: str, counter: int = 0):
  """
  Docstring for rename_media_files

  :param input_directory: Description
  :type input_directory: str
  
  :param output_directory: Description
  :type output_directory: str
  """
  image_extensions: set[str] = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
  video_extensions: set[str] = {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.mpeg'}
  
  # Ensure output directory exists
  os.makedirs(output_directory, exist_ok=True)
  
  # Get files in appearance order
  files = [
    files for files in os.listdir(input_directory)
    if os.path.isfile(os.path.join(input_directory, files))
  ]
  
  # Filter and sort numerically
  ordered_media: list = []
  
  for file in files:
    _, ext = os.path.splitext(file)
    
    if ext.lower() in image_extensions.union(video_extensions):
      ordered_media.append(file)
  
  def safe_int(name):
    try:
      return int(os.path.splitext(name)[0])
    except ValueError:
      return float('inf')
  
  ordered_media.sort(key=safe_int)
  
  counter = counter
  
  for file in ordered_media:
    old_path = os.path.join(input_directory, file)
    _, ext = os.path.splitext(file)
    ext = ext.lower()
      
    if ext in image_extensions:
      base_name: str = f"IMG_{counter:04d}"
    elif ext in video_extensions:
      base_name: str = f"MOV_{counter:04d}"
    else:
      continue
      
    final_name = get_unique_filename(output_directory, base_name, ext)
    final_path = os.path.join(output_directory, final_name)
      
    # Move and rename file
    shutil.move(old_path, final_path)
    print(f"Renamed: {file} -> {final_name}")
      
    counter += 1

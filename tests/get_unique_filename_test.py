import os
import shutil
import unittest
import tempfile

# Module to be tested
def get_unique_filename(self, directory: str, base_name: str, extension: str) -> str:
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

class TestGetUnitqueFilename(unittest.TestCase):
  def setUp(self) -> None:
    self.test_dir: str = tempfile.mkdtemp()
    
    os.makedirs(self.test_dir, exist_ok=True)
  
  # This function is used to clean up temp directories after each test
  def tearDown(self) -> None:
    shutil.rmtree(self.test_dir)
  
  def test_returns_base_name_when_no_conflict(self):
    result: str = get_unique_filename(self, self.test_dir, 'image', '.jpg')
    
    self.assertEqual(result, 'image.jpg')
  
  def test_appends_counter_when_file_exists(self):
    # Create an existing file in test directory
    open(os.path.join(self.test_dir, 'image.jpg'), 'w').close()

    result: str = get_unique_filename(self, self.test_dir, 'image', '.jpg')

    self.assertEqual(result, 'image_1.jpg')
  
  def test_increments_counter_multiple_times(self):
    # Create multiple existing files
    filenames: list[str] = ['image.jpg', 'image_1.jpg', 'image_2.jpg']

    for name in filenames:
      open(os.path.join(self.test_dir, name), 'w').close()
    
    result: str = get_unique_filename(self, self.test_dir, 'image', '.jpg')

    self.assertEqual(result, 'image_3.jpg')
  
  def test_handles_different_extensions(self):
    open(os.path.join(self.test_dir, 'image.png'), 'w').close()

    result: str = get_unique_filename(self, self.test_dir, 'image', '.png')

    self.assertEqual(result, 'image_1.png')
  
  def test_non_sequential_existing_files(self):
    # Missing image_1.jpg on purpose
    filenames: list[str] = ['image.jpg', 'image_2.jpg']

    for name in filenames:
      open(os.path.join(self.test_dir, name), 'w').close()

    result: str = get_unique_filename(self, self.test_dir, 'image', '.jpg')

    self.assertEqual(result, 'image_1.jpg')

if __name__ == '__main__':
  unittest.main()

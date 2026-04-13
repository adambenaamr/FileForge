from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console: Console = Console()

class OutputBox:
  """
  A context manager that captures console output and displays it inside a styled Rich
  Panel.

  This class temporarily redirects printed output to an internal buffer
  while inside the context. When the context exits, all captured content
  is rendered within a `rich.panel.Panel` using the specified title.

  It is useful for grouping related console output into a visually distinct
  box, improving readbility in CLI applications.
  
  :param title: The title displayed at the top of the panel. Defaults to app
  name `FileForge`.
  :type title: str, optional

  Methods
  -------
  :param print: Print content to the internal console. Accepts the same arguments
  as `rich.console.Console.print`.
  :type str: *args, **kwargs

  Example
  -------
  >>> with OutputBox('Results') as box:
  ... box.print('Processing...')
  ... box.print('Done!)
  # Output is diplayed inside a panel titled "Results".
  """
  def __init__(self, title: str = 'FileForge') -> None:
    self.title: str = title
    self.console: Console = Console()
    self.lines: list = []
  
  def __enter__(self):
    # Start capturing output (statically generated)
    self.capture = self.console.capture()
    
    self.capture.__enter__()
    return self
  
  def __exit__(self, exc_type, exc, tb):
    # Stop capturing and render inside a panel
    self.capture.__exit__(exc_type, exc, tb)
    
    content = '\n'.join(str(line) for line in self.lines)
    
    console.print(Panel(content, title=self.title, expand=True))
  
  def print(self, *args, **kwargs):
    self.lines.append(*args, **kwargs)
    self.console.print(*args, **kwargs)
  # def status(self, message: str, style: str = 'bold green') -> None:
  #   self.lines.append(Text(message, style=style))

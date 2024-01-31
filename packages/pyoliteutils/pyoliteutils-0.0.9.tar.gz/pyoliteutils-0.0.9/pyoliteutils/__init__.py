async def install(): 
    import micropip
    await micropip.install(["matplotlib", "pandas"])

from .pyoliteutils import load_file_into_in_mem_filesystem
from .mermaid import mm
from .lessonsurvey import lessonsurvey

from . import _version
__version__ = _version.get_versions()['version']

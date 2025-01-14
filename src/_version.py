import re
from typing import cast, Match

__version__: str = '0.5.2'

result = cast(Match[str], re.match(r'(\d+\.\d+\.\d+).*', __version__))
__version_info__ = tuple(result.group(1).split('.'))
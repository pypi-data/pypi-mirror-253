import os
from typing import (
    List
)


__sep__ = '\t'
__encoding__: str = 'utf-8'
__index__: bool = False

def _get_folder_names(
    base_folder_path: str
) -> List[str]:
    return [f.name for f in os.scandir(base_folder_path) if f.is_dir()]
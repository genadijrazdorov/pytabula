from .table import Table, MutableTable
from . import abc


__pytabula__ = """
━━━━ ━━━━ ┏┓━ ━━━━ ┓━━ ━━━ ┓━ ━━━━
━━━━ ━━━━ ┛┗┓ ━━━━ ┃━━ ━━━ ┃━ ━━━━
┏━━┓ ┓━┏┓ ┓┏┛ ━━┓━ ┗━┓ ┓┏┓ ┃━ ━━┓━
┃┏┓┃ ┃━┃┃ ┃┃━ ━┓┃━ ┏┓┃ ┃┃┃ ┃━ ━┓┃━
┃┗┛┃ ┗━┛┃ ┃┗┓ ┗┛┗┓ ┗┛┃ ┗┛┃ ┗┓ ┗┛┗┓
┃┏━┛ ━┓┏┛ ┗━┛ ━━━┛ ━━┛ ━━┛ ━┛ ━━━┛
┃┃━━ ━┛┃━ ━━━ ━━━━ ━━━ ━━━ ━━ ━━━━
┗┛━━ ━━┛━ ━━━ ━━━━ ━━━ ━━━ ━━ ━━━━
""".strip().splitlines()

__pytabula__ = Table([row.split() for row in __pytabula__], columns="pytabula")

__version__ = "0.0.0"
__version_tuple__ = (0, 0, 0)

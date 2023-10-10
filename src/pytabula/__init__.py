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

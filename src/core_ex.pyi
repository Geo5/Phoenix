from typing_extensions import deprecated as warn_deprecated

from wx.__version__ import VERSION_STRING

__version__ = VERSION_STRING
Port: Final[str] = ...
Platform: Final[str] = ...
PlatformInfo: Final[tuple[str, ...]] = ...

# Make the type checker understand the runtime wx deprecation warnings statically.
# This simple version does accept more parameters at runtime.
deprecated = warn_deprecated("")
deprecatedMsg = warn_deprecated

EmptyString: Final[Literal[""]] = ""

import re

from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


OUTPUT_RE = re.compile(
    r"<stdin>:(?P<line>\d+):((?P<col>\d+):)?\s*"
    r".*?((?P<error>error)|(?P<warning>warning|note)):\s*"
    r"(?P<message>.+)",
    re.MULTILINE,
)


class Rust(Linter):
    cmd = 'cargo clippy ${args} -'
    regex = r''
    multiline = False
    defaults = {
        'selector': 'source.rust',
        'args': [],
    }

import re

from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


OUTPUT_RE = re.compile(
    r"((?P<error>error)|(?P<warning>warning)): (?P<message>.+)\n"
    r" +--> (?P<file>(\w+/)*\w+.rs):(?P<line>\d+):(?P<col>\d+)\n"
    r"(.+\|.*\n)+"
    r"( += note: .+\n)*"
    r"( += help: for further information visit (?P<help_link>\S+)\n)?"
    r"(help: try this:\n(.+\|.*\n)+)?"
    r"\n\n"
)


class Rust(Linter):
    cmd = 'cargo clippy ${args}'
    regex = OUTPUT_RE
    multiline = True
    defaults = {
        'selector': 'source.rust',
        'args': [],
    }

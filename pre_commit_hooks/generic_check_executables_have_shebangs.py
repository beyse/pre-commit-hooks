"""Check that executable text files have a shebang."""
import argparse
import shlex
import sys
from typing import Optional
from typing import Sequence


def check_has_shebang(path: str) -> int:
    print('You are ine check_has_shebang')
    with open(path, 'rb') as file_handler:
        first_bytes = file_handler.read(2)

    if first_bytes != b'#!':
        quoted = shlex.quote(path)
        print(
            '{}: [TEST] marked executable but has no (or invalid) shebang!\n'.format(path),
            "  If it isn't supposed to be executable, try: ",
            '`chmod -x {}`\n'.format(quoted),
            '  If it is supposed to be executable, double-check its shebang.',
            file=sys.stderr,
        )
        return 1
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    print('Test 123')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)
    
    retv = 0

    if sys.platform.startswith('win32'):
        print('!!! You are on windows')
        return retv
    else:
        print('!!! You are on a different OS')
        
    
    for filename in args.filenames:
        retv |= check_has_shebang(filename)

    return retv


if __name__ == '__main__':
    sys.exit(main())

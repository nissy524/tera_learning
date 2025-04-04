from pathlib import Path

path=Path.cwd()
APPLE=path / 'APPLE'

APPLE_g=APPLE.iterdir()
for x in APPLE_g:
    print(x)
#実行しても表示されない

from pathlib import Path

files=[x.name for x in (path.cwd()/'APPLE').iterdir()]
print(files)



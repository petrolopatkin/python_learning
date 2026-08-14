from pathlib import Path
# Path.cwd to see in which directory we are working right now
print(Path.cwd())
#Path().iterdir() to see all files in current direcotry
for p in Path('Study').iterdir():
    print(p)
# .suffix to see an extention of a file
myfile = Path("pathlib.py")
print(myfile.suffix)
# .stem to see file name without an extention
myfile = Path("Study") / "pathlib.py"
print(myfile.stem)
# / to join a new file into directory
mydir = Path("Study") / "test_dir"
new_file = mydir / "new_file.txt"
print(new_file)
# join.path() to do the same thing as the last one
mydir = Path("test_dir")
new_file = mydir.joinpath("new_file.txt")
print(new_file)
# .exists() to see if a file exists
print(myfile.exists())
print(mydir.exists())
print(new_file.exists())
# .parent to see a parent directory of a file
print(myfile.parent)
print(mydir.parent)
print(new_file.parent)
# to create an absolute path(2 ways to do that)
print(myfile.parent.absolute())
print(myfile.absolute().parent)
# .glob() to search a directory
for p in Path.home().glob("*vscode*"):
    print(p)
# .open() to open file
settings_file = Path.home() / "AppData" / "Roaming" / "Code" / "User" / "settings.json"
with settings_file.open(encoding="utf-8") as f:
    print(f.read())
#.mkdir to make a directory
p = Path("Study") / "test_dir2"
p.mkdir()
#.rmdir to remove directory(only empty directory)
p = Path("Study") / "test_dir2"
p.rmdir()
#.touch to create a file
p = Path("Study") / "temp_file.txt"
p.touch()
#.rename() to rename a file
p = Path("Study") / "temp_file.txt"
p.rename("TempFile.txt")
#.unlink() to remove an existing file
p = Path("Study") / "temp_file.txt"
p.unlink()
from random import randint, seed
import codecs, os, inspect
try:
    import disnake

    def get_username(user, display_name=False, bot=False):
        """
        user: disnake.User (or disnake.Member)
        gets user username
        >>> get_username(user)
            it returns:
                username#discriminator (old usernames system)
                username
        >>> get_username(user, display_name=True)
            it returns:
                username#discriminator (SERVER display name)
                username (SERVER display name)
        >>> get_username(user, bot=True):
            it returns
                username#discriminator BOT
                username#discriminator
                username
        >>> get_username(user, display_name=Treu, bot=True)
            it returns:
                username#discriminator (SERVER display name) BOT
                username#discriminator (SERVER display name)
                username (SERVER display name)
        """
        h = user.name
        if user.discriminator!=0:
            h+=f"#{user.discriminator}"
        if display_name:
            h+=f" ({user.display_name})"
        if bot and user.bot:
            h+=" BOT"
        return h

    def is_online(guild, user_id):
        """
        guild: disnake.Guild

        returns True if member is not offline (online, idle, etc.)
        else returns False

        also returns False if member was not found on guild
        """
        member = guild.get_member(user_id)

        memberOnline = False

        if member != None:
            memberOnline = (member.status != disnake.Status.offline)
        return memberOnline

except ModuleNotFoundError:
    pass

def get__file__():
    if not __name__ == "__main__":
        for frame_info in inspect.stack()[1:]:  # Iterate through stack frames
            frame = frame_info.frame
            if frame.f_globals["__name__"] != "<frozen importlib._bootstrap>":
                return frame.f_code.co_filename

    return __file__

def openfile(fp):
    """
    returns file with utf-8 encoding
    """
    return codecs.open(fp, encoding="utf-8")

def editfile(fp):
    """
    returns file with utf-8 encoding and uses write mode
    """
    return codecs.open(fp, "w", encoding="utf-8")

def smthfile(fp, readingmode):
    """
    returns file with utf-8 encoding and uses write mode you want to use
    """
    return codecs.open(fp, readingmode, encoding="utf-8")

def get_folder_path(*args, create_folders=True):
    """
    returns folder that is in same folder as python file
    for example if your python file is "D:/kreisi program/main.py"
    get_folder_path("folder 1", "folder 2") will return
    "D:/kreisi program/folder 1/folder 2"
    if any folder doesn't exist it will be created
    do get_folder_path(..., create_folders=False) if you won't
    """
    folder_dir = os.path.dirname(get__file__())
    for f in args[1:]:
        folder_dir = os.path.join(folder_dir, f)
        if create_folders and not os.path.exists(folder_dir):
            os.makedirs(folder_dir)
    return folder_dir

def get_file_path(folder, filename, create_file=True):
    """
    returns "folder where python file is/folder/filename"
    for example if your python file is "D:/kreisi program/main.py"
    get_file_path("folder", "opinion on mars.txt") will return
    "D:/kreisi program/folder/opinion on mars.txt"
    if file or folder doesn't exist it will be created
    do get_folder_path(folder, filename, create_file=False) if you won't
    """
    folder_dir = get_folder_path(folder, create_folders=create_file)

    filepath = os.path.join(folder_dir, filename)
    if create_file and not os.path.exists(filepath):
        with open(filepath, "w") as f: pass

    return filepath

def add_line(fp, line):
    """
    adds line to the of the file
    for example if file already has 2 strings
    add_line("opinion on mars.txt", "MARS IS A STUPID PLANET!!!!!!")
    will do

    already existsing string in file 1
    already existsing string in file 2
    MARS IS A STUPID PLANET!!!!!!
    """
    with smthfile(fp, "a+") as file:
        file.seek(0)
        if file.read():
            file.seek(0, 2)
            file.write("\n")
        file.write(line)

def remove_line(fp, line):
    """
    removes line to the of the file
    for example if file is from previous example
    remove_line("opinion on mars.txt", "already existsing string in file 1")
    will do

    already existsing string in file 2
    MARS IS A STUPID PLANET!!!!!!
    """
    typingemoji=""
    for every in openfile(fp).read().split("\n"):
        if every != line:
            typingemoji+=f"{every}\n"
    editfile(fp).write(typingemoji[:-1])

def isWord(word):
    """
    >>> isWord("wuGGygames")
    True
    >>> isWord("wuggy games")
    False
    """
    h = 0
    for every in word:
        if any(every.lower()==_ for _ in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz"):
            h += 1
    return (len(word)==h)

def isLetter(letter):
    """
    >>> isLetter("a")
    True
    >>> isLetter("5")
    False
    >>> isLetter("ab")
    False
    """
    return any(_==letter.lower() for _ in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz")

def hAutoCorrect(hInput):
    """
    just ever use ammeter /hautocorrect
    """
    hAutoCorrected=""
    up=True
    for hInputFor in hInput:
        if up==True and isLetter(hInputFor):
            hAutoCorrected+="h"+hInputFor.upper()
            up=False
        elif (not up and isLetter(hInputFor)): hAutoCorrected+=hInputFor.lower()
        else:
            hAutoCorrected+=hInputFor
            up=True
    return hAutoCorrected

def generate_ip(name):
    seed(name)
    return f"{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}"
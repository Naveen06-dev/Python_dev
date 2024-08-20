def print_name_on_whiteboard(name):
    letters = {
        'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
        'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
        'C': [" CCC ", "C    ", "C    ", "C    ", " CCC "],
        'D': ["DDD  ", "D  D ", "D   D", "D  D ", "DDD  "],
        'E': ["EEEEE", "E    ", "EEE  ", "E    ", "EEEEE"],
        'F': ["FFFFF", "F    ", "FFFF ", "F    ", "F    "],
        'G': [" GGG ", "G    ", "G  GG", "G   G", " GGG "],
        'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
        'I': [" III ", "  I  ", "  I  ", "  I  ", " III "],
        'J': ["  JJJ", "    J", "    J", "J   J", " JJJ "],
        'K': ["K  K ", "K K  ", "KK   ", "K K  ", "K  K "],
        'L': ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
        'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
        'N': ["N   N", "N N N", "N  NN", "N   N", "N   N"],
        'O': [" OOO ", "O   O", "O   O", "O   O", " OOO "],
        'P': ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
        'Q': [" QQQ ", "Q   Q", "Q Q Q", " Q  Q", "  QQ "],
        'R': ["RRRR ", "R   R", "RRRR ", "R R  ", "R  RR"],
        'S': [" SSS ", "S    ", " SSS ", "    S", " SSS "],
        'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
        'U': ["U   U", "U   U", "U   U", "U   U", " UUU "],
        'V': ["V   V", "V   V", " V V ", " V V ", "  V  "],
        'W': ["W   W", "W W W", "W W W", "W W W", " W W "],
        'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
        'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
        'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
        ' ': ["     ", "     ", "     ", "     ", "     "]
    }
    
    name = name.upper()
    
    lines = [""] * 5
    for char in name:
        if char in letters:
            art = letters[char]
            for i in range(5):
                lines[i] += art[i] + "  "
    
   
    for line in lines:
        print(line)

name=input("Enter the name:")
print_name_on_whiteboard("name")

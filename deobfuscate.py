import dis
import base64, marshal, zlib
import sys
import os
import re
from pystyle import *
def art():
    banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣷⣀⣀⣀⣀⠀⠀⠀⠀⣀⣀⣀⣀⣠⣤⡤
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⣿⣿⣿⣿⣿⣿⡿⠟⣻⣿⣿⣿⣿⣿⣥⣄⣀⣀⣀⡀
⠀⢀⣴⣶⣶⣦⣤⣄⠀⢷⣼⣿⣿⡿⠻⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀made by kuyo | https://kuyo.lol
⢀⣿⡿⢻⣿⣿⠿⠟⠀⠀⠟⠛⢿⠿⠿⠷⡶⠚⢻⣿⣿⣿⣿⣿⣋⣁⠀⠀⠀⠀https://github.com/kuyo1337
⠹⡟⠀⠸⡿⠁⠀⠀⠀⠀⠈⢄⠈⠀⠀⠀⠁⢀⣾⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀ press "enter" to countinue
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠶⣤⣤⣶⣟⣿⣻⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⡾⣿⣿⡣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠟⢻⣿⣿⢿⣿⣿⡝⠻⢷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⢸⡿⠁⠀⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    Anime.Fade(Center.Center(banner), Colors.white_to_black, Colorate.Vertical, enter=True)

def art2():
    print("""
 __                           .__         .__   
|  | ____ __ ___.__. ____     |  |   ____ |  |  
|  |/ /  |  <   |  |/  _ \    |  |  /  _ \|  |  
|    <|  |  /\___  (  <_> )   |  |_(  <_> )  |__
|__|_ \____/ / ____|\____/ /\ |____/\____/|____/
     \/      \/            \/                   
        """)
def handleb64(file_content):
    match = re.search(rb"base64\.b64decode\((?:b)?[\"']([A-Za-z0-9+/=\n\r]+)[\"']\)", file_content)
    if not match:
        raise ValueError("[-] No base64.b64decode(...) pattern found.")
    return match.group(1).replace(b'\n', b'').replace(b'\r', b'')

def decode(encoded):
    decoded = base64.b64decode(encoded)
    try:
        decompressed = zlib.decompress(decoded)
        data = marshal.loads(decompressed)
        return data, "marshal ← zlib ← base64"
    except:
        pass
    try:
        decompressed = zlib.decompress(base64.b64decode(encoded))
        data = marshal.loads(decompressed)
        return data, "marshal ← base64 ← zlib"
    except:
        pass

    raise ValueError("[-] Could not decode with known sequences.")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <obfuscated_file.py>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print("[-] File not found.")
        sys.exit(1)

    with open(file_path, 'rb') as f:
        content = f.read()

    try:
        encoded = handleb64(content)
        data, sequence = decode(encoded)

        print(f"[+] Detected decode sequence: {sequence}")

        byte_string = b'a\r\r\n\x00\x00\x00\x00\xf6\x971a\x00\x00\x00\x00'
        output_file = 'kuyo1337.pyc'
        with open(output_file, 'wb') as pyc:
            pyc.write(byte_string)
            marshal.dump(dis.Bytecode(data).codeobj, pyc)

        print(f"[+] Decompiled .pyc saved to: {output_file}")

    except Exception as e:
        print(f"[-] Error during deobfuscation: {e}")
        sys.exit(1)
if __name__ == "__main__":
    art()
    art2()
    main()

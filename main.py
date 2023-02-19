import asyncio
import edge_tts

def read_file(file_path):
    with open(file_path, "r") as file:
        contents = file.read()
    return contents

file_name = input("Choose the file name:")
file_path = file_name+".txt"
file_contents = read_file(file_path)

VOICE = ["zh-TW-HsiaoChenNeural", "en-IE-EmilyNeural", "en-US-AriaNeural","en-US-ChristopherNeural","en-US-SteffanNeural","en-GB-SoniaNeural","en-AU-NatashaNeural","en-GB-LibbyNeural","en-US-RogerNeural","en-IN-PrabhatNeural","en-US-JennyNeural","en-US-MichelleNeural","en-US-GuyNeural","en-US-EricNeural","en-US-AnaNeural"]
n = len(VOICE)

print("Choose the voice:\n1. Chen\n2. Emily\n3. Aria\n4. Christopher\n5. Steffan\n6. Sonia\n7. Natasha\n8. Libby\n9. Roger\n10. Prabhat\n11. Jenny\n12. Michelle\n13. Guy\n14. Eric\n15. Ana")

option_num = input()

if option_num.isnumeric() and 1 <= int(option_num) <= n:
    selected_voice = VOICE[int(option_num) - 1]
else:
    selected_voice = VOICE[1]

OUTPUT_FILE = file_name+"v"+option_num+".mp3"

async def _main() -> None:
    communicate = edge_tts.Communicate(file_contents, selected_voice)
    await communicate.save(OUTPUT_FILE)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(_main())

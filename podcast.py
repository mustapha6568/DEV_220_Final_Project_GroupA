import os


# Open the WAV file
def retrieve_and_play(roleid:list):
    
    try:
        
        wav = f"{os.getcwd()}"+"\Audio_files"+f"\{roleid[0][0]}\{roleid[0]}.wav"
        return wav
    except KeyboardInterrupt or ValueError:
        print("File stopped")


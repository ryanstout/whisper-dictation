import typing as t
import platform
from Foundation import NSURL
from AVFoundation import AVAudioPlayer

player_cache = {}

def play_sound(sound_type: t.Literal["start", "stop"]):
    if sound_type == "start":
        play_caf("/System/Library/PrivateFrameworks/SocialUI.framework/Versions/A/Resources/dt-begin.caf")
    else:
        play_caf("/System/Library/PrivateFrameworks/SocialUI.framework/Versions/A/Resources/dt-cancel.caf")

def play_caf(file_path):
    # Guard clause to ensure macOS
    if platform.system() != "Darwin":
        print("This function is intended for macOS machines only.")
        return

    # Create AVAudioPlayer instance only if it hasn't been created for the file path
    if file_path not in player_cache:
        file_url = NSURL.fileURLWithPath_(file_path)
        player, error = AVAudioPlayer.alloc().initWithContentsOfURL_error_(file_url, None)

        if error:
            print(f"Error initializing player: {error}")
            return
        player_cache[file_path] = player
    else:
        player = player_cache[file_path]

    player.stop()
    player.setCurrentTime_(0)
    player.play()
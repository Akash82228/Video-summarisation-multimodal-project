from pydub import AudioSegment
from pydub.playback import play

def convert_mp4_to_mp3_pydub(input_path, output_path):
    try:
        # Load video file
        audio = AudioSegment.from_file(input_path)

        # Export AudioSegment as MP3
        audio.export(output_path, format="mp3")

        print(f"Conversion successful. MP3 file saved at: {output_path}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
# convert_mp4_to_mp3_pydub("video.mp4", "output.mp3")
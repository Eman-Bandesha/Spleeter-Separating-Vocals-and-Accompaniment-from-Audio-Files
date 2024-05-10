from spleeter.separator import Separator
separator = Separator('spleeter:2stems')

audio_file_path = "testing_beliver.mp3"
output_dir = "output"
separator.separate_to_file(audio_file_path, output_dir)


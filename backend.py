from spleeter.separator import Separator
from pathlib import Path

def split_audio(input_path, output_dir, stems=2):
    
    stem_config = f'spleeter:{stems}stems'
    separator = Separator(stem_config)
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    separator.separate_to_file(str(input_path), str(output_dir))
    return str(output_dir)

def batch_process(files, output_dir, stems=2):
    for file in files:
        split_audio(file, output_dir / Path(file).stem, stems=stems)

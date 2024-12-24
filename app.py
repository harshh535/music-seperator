import streamlit as st
from pathlib import Path
from zipfile import ZipFile
import shutil
from backend import split_audio, batch_process

st.title("Music Stem Splitter 🎵")
st.write("Upload an audio file to separate it into stems (e.g., vocals, drums, bass).")

uploaded_files = st.file_uploader(
    "Upload Audio File(s)", type=["mp3", "wav", "flac"], accept_multiple_files=True
)
stems_option = st.radio("Select Stem Configuration:", options=[2, 4], index=0)

if uploaded_files:
    with st.spinner("Processing audio..."):
        
        temp_dir = Path("temp")
        output_dir = Path("output")
        temp_dir.mkdir(exist_ok=True, parents=True)
        output_dir.mkdir(exist_ok=True, parents=True)

       
        file_paths = []
        for uploaded_file in uploaded_files:
            temp_path = temp_dir / uploaded_file.name
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.read())
            file_paths.append(temp_path)

    
        if len(file_paths) > 1:
            batch_process(file_paths, output_dir, stems=stems_option)
        else:
            split_audio(file_paths[0], output_dir / Path(file_paths[0]).stem, stems=stems_option)
        zip_path = output_dir.with_suffix(".zip")
        with ZipFile(zip_path, 'w') as zipf:
            for root, _, files in os.walk(output_dir):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), output_dir))
        st.success("Processing complete! 🎉")
        st.download_button(
            "Download Stems",
            data=zip_path.open("rb"),
            file_name=zip_path.name,
            mime="application/zip",
        )
if st.button("Clear Temporary Files"):
    shutil.rmtree(temp_dir, ignore_errors=True)
    shutil.rmtree(output_dir, ignore_errors=True)
    st.info("Temporary files cleared.")

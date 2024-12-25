# music-segmentor:-
This project is a Music Stem Splitter tool designed to separate audio tracks into individual stems (e.g., vocals, drums, bass, others) using an open-source machine learning model, Spleeter. It features a user-friendly web interface built with Streamlit, allowing users to upload audio files, process them, and download the separated stems.

---------------------------------------------------------------------------
Prerequisites:-
ensure the following are installed (python and installer pip ):


1)Python (3.8 or later)
2)pip
-------------------------
Dependencies insatllation:-
Install all the requirements specified in requirements.txt by using command:-
         pip install -r requirements.txt
---------------------------------------------

Directory Structure:
backend.py: Contains the core logic for stem separation.
app.py: Streamlit application for user interaction.

-------------------------------------------------------
How to run the project:-
        Running the Application:
                 Start the Streamlit server using streamlit run app.py.
        Using the UI:
                Upload audio files through the "Upload Audio File(s)" button.
        Select your preferred stem configuration (2-stem or 4-stem).
                  Process the files by waiting for the backend to complete stem separation.
                  Download the output stems as a ZIP file.
        Batch Processing:
                  Upload multiple files in one go for simultaneous processing.
---------------------------------------------------------
A bit description of tools used :-
(Source:OPENAI)
Spleeter: A powerful open-source library by Deezer, enabling fast and accurate music source separation into different stems. It handles the core audio processing in the backend.  
2. Streamlit: A Python-based framework for building interactive web applications with ease. It powers the user interface, making the tool accessible through a browser.
3. Python: The primary programming language used for the project, enabling seamless integration of machine learning models and web interfaces.
4. Pandas: Facilitates data manipulation and file handling, ensuring smooth management of audio files and outputs.
5. NumPy: Provides support for numerical computations, which are crucial for audio processing tasks.
6. pathlib: Simplifies file path manipulations, ensuring the system handles file directories and naming consistently.
7. Zipfile Module: Compresses separated stems into a ZIP format, facilitating easy downloads for users.
8. SoundFile: Handles reading and writing of audio files in various formats, ensuring compatibility during processing. 

                  
         

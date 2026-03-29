# Josh ASR Project

This project is focused on Automatic Speech Recognition (ASR) tasks, including dataset preparation, model inference, error analysis, and evaluation. The repository contains scripts and data for working with audio datasets, running ASR models (such as Whisper), and analyzing results.

## Project Structure

- **build_dataset.py**: Script to build and preprocess the dataset.
- **calculate_wer.py**: Calculates Word Error Rate (WER) for ASR predictions.
- **cleanup_pipeline.py**: Cleans up and processes data pipelines.
- **download_data.py**: Downloads required audio and transcript data.
- **download_gcs_dataset.py**: Downloads datasets from Google Cloud Storage.
- **error_analysis.py**: Performs error analysis on ASR outputs.
- **run_whisper.py**: Runs the Whisper ASR model on the dataset.

### Data Folders
- **data/**: Contains the main dataset, including:
  - `dataset.csv`: Main dataset metadata.
  - `error_samples.csv`: Samples with errors for analysis.
  - `predictions.csv`: Model predictions.
  - `audio/`: Audio files.
  - `metadata/`: Additional metadata files.
  - `transcripts/`: Ground truth transcripts (JSON format).
- **q3_data/**: Contains scripts and data for Question 3 analysis.
  - `q3_spelling.py`, `unique_words.csv`
- **q4_data/**: Contains scripts and data for Question 4 analysis.
  - `ft_results.csv`, `q4_lattice.py`, `Question 4 - Task.csv`

## Usage

1. **Set up the environment**
   - Create and activate a Python virtual environment.
   - Install required dependencies (see below).

2. **Download and prepare data**
   - Use `download_data.py` or `download_gcs_dataset.py` to fetch datasets.
   - Run `build_dataset.py` to preprocess and organize data.

3. **Run ASR and analysis**
   - Use `run_whisper.py` to generate ASR predictions.
   - Evaluate results with `calculate_wer.py` and `error_analysis.py`.

## Requirements

- Python 3.8+
- Recommended: virtual environment (venv, conda, etc.)
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
  *(If requirements.txt is not present, install packages as needed for Whisper, pandas, numpy, etc.)*

## Notes
- Data files and scripts for specific questions (Q3, Q4) are in their respective folders.
- For large datasets, ensure sufficient disk space and memory.

## License

This project is for educational and research purposes.

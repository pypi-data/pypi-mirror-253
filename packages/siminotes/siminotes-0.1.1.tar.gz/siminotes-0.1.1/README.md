# SimiNotes - CLI Tool for Similar Note Retrieval

SimiNotes is a command-line interface (CLI) tool written in Python that enables users to discover similar notes within their
notes collection. The tool utilizes sentence embeddings with sbert to compare a given query against a corpus of user notes.

## Features

- **Embedding:** Utilizes sbert to generate vector embeddings for notes.
- **Similarity Search:** Finds notes similar to a given query based on embeddings.
- **Configurable:** Allows users to configure directories, file extensions, and exclusion criteria.

## Installation

Before using this CLI tool, ensure that you have Python and pip installed. Additionally, install the PyTorch library by
following the steps below:

1. Download and install Python and pip from the [official site](https://www.python.org/).
2. Install the PyTorch library separately based on your requirements. For the CPU version, use the following command:

    ```bash
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
    ```

Now, install the SimiNotes CLI tool:

```bash
pip install siminotes
```

## Configuration

Before using the CLI, configure some essential values, such as the notes directory and exclusions. SimiNotes uses a
configuration file (`config.txt`) to set preferences. Configure the tool by creating the file in the appropriate configuration
directory.

### Configuration Directory

- Linux:

```plaintext
~/.config/siminotesconfig/
```

- macOS:

```plaintext
~/.siminotesconfig/
```

- Windows:

For Windows, use AppData\Roaming for per-user configuration:

```plaintext
AppData\Roaming\Siminotes\
```

Alternatively, place `config.txt` in the home directory:

```plaintext
~/.siminotesconfig/
```

### Configuration File (`config.txt`)

Create a `config.txt` file in the configuration directory. Below is an example configuration:

```plaintext
notes_dir = /path/to/your/notes
exclude_dir = directory1,directory2
exclude_file = file1,file2
note_extension = .md
```

Configuration Parameters:

- notes_dir: Path to the directory containing your notes.

- exclude_dir: Comma-separated directories to exclude from the search. Paths should be relative to notes_dir.

- exclude_file: Comma-separated files to exclude from the search. Paths should be relative to notes_dir.

- note_extension: The extension of your note files (e.g., .md).

## Usage

Now let's use our cli,

### Command-Line Arguments

- Query via Text:

```bash
siminotes text "Your Query Text"
```

- Query via File:

```bash
siminotes file filename
```

Both will result in,

```
Top files which are similar to given query:
Value range from -1 to 1, where going toward 1 means note is close to query

/... with score 0.43386968970298767

/... with score 0.42138463258743286

...

```

## Troubleshooting

If you encounter any errors or problems with this tool, please open an issue in the repository.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to contribute to SimiNotes by creating issues or submitting pull requests.

## Acknowledgments

[Sentence-BERT](https://www.sbert.net/index.html) for sentence embeddings.

## Future:

- I feel like simple dot product hits are enough to find similar notes but in future if there is need to 
improve results then consider this roop
[Retrieve and Rerank](https://www.sbert.net/examples/applications/retrieve_rerank/README.html)
[Vid Tut](https://youtu.be/zMDBc_Q9Ark?feature=shared)

- If it is taking more memory, then we can quantise the vectors into int8
[Quantisation Guide](https://www.sbert.net/examples/training/distillation/README.html#quantization)
[Github Repo to check](https://github.com/davidberenstein1957/fast-sentence-transformers)

import sys
from pathlib import Path
from pickle import HIGHEST_PROTOCOL, dump, load

from . import collect_files, embedding, utils

CONFIG_DIR = utils.get_config_dir()


def main():
    # getting the query
    query = ""
    if len(sys.argv) != 3 or sys.argv[1] not in ["file", "text"]:
        print("USAGE:\nEither provide query text or file name to read text from")
        print("File Example: siminotes file filename")
        print('Query Example: siminotes text "Query Text"')
        return

    config = dict()
    config_file_path = f"{CONFIG_DIR}/config.txt"

    try:
        with open(config_file_path, "r") as f:
            config = dict()
            for line in f.readlines():
                c = line.strip().split("=")
                if c[0] == "exclude_dir" or c[0] == "exclude_file":
                    config[c[0]] = c[1].split(",")
                else:
                    config[c[0]] = c[1]
    except FileNotFoundError:
        print(f"Error: Config file not found at {config_file_path}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # find if there is cache data or not
    print("Finding cache data and building corpus to compare against")
    cache_data = dict()
    if Path(f"{CONFIG_DIR}/cache_data.pickle").exists() == True:
        with open(f"{CONFIG_DIR}/cache_data.pickle", "rb") as f:
            cache_data = load(f)

    print("Checking for new/update and embedding it")
    cache_data, changed = collect_files.extract_data_from_md(
        config["notes_dir"],
        config["exclude_dir"],
        config["exclude_file"],
        config["note_extension"],
        cache_data,
    )

    if len(cache_data) == 0:
        raise Exception("You don't have any notes in md files")

    # don't have to worry about writing as pickle won't duplicate it
    # https://docs.python.org/3/library/pickle.html#comparison-with-marshal first point
    if changed == True:
        with open(f"{CONFIG_DIR}/cache_data.pickle", "wb") as f:
            dump(cache_data, f, protocol=HIGHEST_PROTOCOL)

    if sys.argv[1] == "text":
        query = sys.argv[2]
    elif sys.argv[1] == "file":
        with open(sys.argv[2], "r") as queryFile:
            query = queryFile.read().strip()

        if (
            Path(sys.argv[2]).absolute().is_relative_to(Path(config["notes_dir"]))
            == True
        ):
            del cache_data[Path(sys.argv[2]).absolute()]

    # after getting the embedding of notes
    print("Embedding the query")
    query_embed = embedding.embed(query, True)

    # now getting similarity with this
    print("Finding similarity")
    corpus = [cache_data[key][0] for key in cache_data]
    hit = embedding.similarity(query_embed, corpus)

    # then printing the similarity score with filename and returning
    files = list(cache_data.keys())
    print("\n\n======================\n\n")
    print("Top files which are similar to given query:")
    print(
        "Value range from -1 to 1, where going toward 1 means note is close to query\n"
    )
    for score, id in zip(hit[0], hit[1]):
        print(f"{str(files[id]).replace(config['notes_dir'], '')} with score {score}\n")

    return

from datetime import datetime
from pathlib import Path

from torch import Tensor

from . import embedding


def extract_data_from_md(
    path_string: str,
    exclude_dir: list[str],
    exclude_file: list[str],
    note_extension: str,
    cache_data: dict[Path, tuple[Tensor, datetime]],
):
    changed = False
    md_files = [
        path
        for path in Path(path_string).rglob(f"*{note_extension}")
        if path.is_file()
        and str(path.relative_to(path_string)) not in exclude_file
        and not any(ed in str(path.parent) for ed in exclude_dir)
    ]
    # this takes care of deletion
    # but for case where we delete and add new note, change will become True
    # with help of below
    if len(md_files) != len(cache_data.keys()):
        changed = True

    new_cache_data = dict()
    updates_new = dict()
    for note in md_files:
        if note not in cache_data:
            updates_new[note] = note.read_text()
        elif datetime.fromtimestamp(note.stat().st_mtime) > cache_data[note][1]:
            updates_new[note] = note.read_text()
        else:
            new_cache_data[note] = cache_data[note]

    if len(updates_new) > 0:
        changed = True
        # now creating embedding of new and update
        updates_new_embedding = embedding.embed(list(updates_new.values()), True)

        # then updating the cache data and returning it
        for i, key in enumerate(updates_new):
            new_cache_data[key] = (
                updates_new_embedding[i],
                datetime.fromtimestamp(key.stat().st_mtime),
            )

    return new_cache_data, changed

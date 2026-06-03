from pathlib import Path


def delete_all_files(folder_path: str) -> None:
    folder = Path(folder_path)

    for path in folder.iterdir():
        if path.is_file():
            path.unlink()
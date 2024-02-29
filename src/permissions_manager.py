import os

def grant_write_permission(file_path):
    try:
        # Grants write permission to the specified file
        os.chmod(file_path, 0o755)
    except Exception as e:
        # Raises an error if there's an issue granting write permission
        raise RuntimeError(f"Error granting write permission: {e}")

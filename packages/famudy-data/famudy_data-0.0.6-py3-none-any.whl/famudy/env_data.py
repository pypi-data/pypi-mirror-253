from pathlib import Path

from environs import Env

env = Env(expand_vars=True)
env_file_path = Path(f"{Path.home()}/.config/famudy/.env")
if env_file_path.exists():
    env.read_env(str(env_file_path), recurse=False)

with env.prefixed("FAMUDY_"):
    FAMUDY_PROCESSED_CAPTURE_DATA_PATH = env("PROCESSED_CAPTURE_DATA_PATH",
                                             f"<<<Define FAMUDY_PROCESSED_CAPTURE_DATA_PATH in {env_file_path}>>>")
    FAMUDY_REMOTE_PROCESSED_CAPTURE_DATA_PATH = env("REMOTE_PROCESSED_CAPTURE_DATA_PATH",
                                                    f"<<<Define FAMUDY_REMOTE_PROCESSED_CAPTURE_DATA_PATH in {env_file_path}>>>")

    FAMUDY_PROCESSED_CAPTURE_DATA_PATH_NEW = env("PROCESSED_CAPTURE_DATA_PATH_NEW",
                                                 f"<<<Define FAMUDY_PROCESSED_CAPTURE_DATA_PATH_NEW in {env_file_path}>>>")
    FAMUDY_REMOTE_PROCESSED_CAPTURE_DATA_PATH_NEW = env("REMOTE_PROCESSED_CAPTURE_DATA_PATH_NEW",
                                                        f"<<<Define FAMUDY_REMOTE_PROCESSED_CAPTURE_DATA_PATH_NEW in {env_file_path}>>>")

    FAMUDY_FLAME_MODEL_PATH = env("FLAME_MODEL_PATH", f"<<<Define FAMUDY_FLAME_MODEL_PATH in {env_file_path}>>>")

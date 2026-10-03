import pathlib

class project_dir:
    ROOT_DIR = pathlib.Path(__file__).parent.parent.absolute()

    DATA_DIR = ROOT_DIR/'data'

    RAW_DIR = DATA_DIR/'raw'
    PROCESSED_DIR = DATA_DIR/'processed'
    FEATURED_DIR = DATA_DIR/'featured'

    MODEL_DIR = ROOT_DIR/'models'


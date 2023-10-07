import os


# load_dotenv()
ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


# Define the folder for storing database
SOURCE_DIRECTORY = f"{ROOT_DIRECTORY}/SOURCE_DOCUMENTS"

PERSIST_DIRECTORY = f"{ROOT_DIRECTORY}/DB"


MAX_NEW_TOKENS = 1000


MODELS_PATH = "./models"


N_GPU_LAYERS = 100  # Llama-2-70B has 83 layers
N_BATCH = 512


# Context Window and Max New Tokens
CONTEXT_WINDOW_SIZE = 2048
# CONTEXT_WINDOW_SIZE = 4096
MAX_NEW_TOKENS = int(CONTEXT_WINDOW_SIZE / 4)  # int(CONTEXT_WINDOW_SIZE/4)

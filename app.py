import os
import pandas as pd

DATA_DIR = "data"

prospects = pd.read_json(os.path.join(DATA_DIR, "prospects.json"), orient="index")
vagas = pd.read_json(os.path.join(DATA_DIR, "vagas.json"), orient="index")
applicants = pd.read_json(os.path.join(DATA_DIR, "applicants.json"), orient="index")

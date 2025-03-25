import os

local = os.getcwd()
pasta_downloads = os.path.join(local, "data", "raw")
os.makedirs(pasta_downloads, exist_ok=True)
import os 
from huggingface_hub import snapshot_download

model_list = ["Qwen/Qwen-VL", 
              "Qwen/Qwen-VL-Chat-Int4", 
              "google/paligemma-3b-mix-224"]

class ModelRegistry: 
    def __init__(self, local_dir:str='./model'): 
        if not os.path.exists(local_dir): 
            os.mkdir(local_dir)

        
    def _download_model_to_local(self, model_id:str, local_dir:str): 
        # Create a sub-dir for specific model
        model_name = model_id.split("/")[1]
        # model_name = model_name.replace("-", "_")
        local_dir = os.path.join(local_dir, model_name)
        os.mkdir(local_dir)

        snapshot_download(repo_id=model_id, 
                        local_dir=local_dir, 
                        resume_download=True)
        

    def _remove_model_from_local(self, model_id: str, local_dir:str): 
        model_name = model_id.split("/")[1]
        # model_name = model_name.replace("-", "_")
        local_dir = os.path.join(local_dir, model_name)
        os.rmdir(local_dir)
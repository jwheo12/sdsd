import gdown

file_ids = [""]
file_names = [""]
save_dir = "/workspace/sdsd/stable-diffusion-webui/models/Stable-diffusion"

base_url = "https://drive.google.com/uc?id="
for file_id, file_name in zip(file_ids, file_names):
    url = base_url + file_id
    output = f"{save_dir}/{file_name}"
    gdown.download(url, output, quiet=False)

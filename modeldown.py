import os
import gdown

file_ids = ["1NcOMBevPqxKMDnWkLX4rkXBVXGZtS7wL",
            "1mOsJK_RqmD2eSUPIRbMjROA-9yaeu0vA",
            "1QmbsH-W9-fvDEyAxma0uNekxkflrMe5i"]
file_names = ["xRicaMix_v5.6_2.5D.safetensors",
              "henmixReal_v22.safetensors",
              "chilloutmix_NiPrunedFp32Fix.safetensors"]
save_dir = "/workspace/sdsd/stable-diffusion-webui/models/Stable-diffusion"

base_url = "https://drive.google.com/uc?id="
for file_id, file_name in zip(file_ids, file_names):
    url = base_url + file_id
    output = f"{save_dir}/{file_name}"
    
    # 파일이 이미 존재하는지 확인
    if os.path.exists(output):
        print(f"Skipping {file_name} - File already exists")
        continue
    
    gdown.download(url, output, quiet=False)

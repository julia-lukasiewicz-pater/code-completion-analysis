import os
import shutil
import zipfile


raw_folder_path = "../data/raw"
destination_folder = "../data/processed/processed_dataset"
subfolders = ["f", "fc", "r", "rc"]


with zipfile.ZipFile(os.path.join(raw_folder_path, 'raw_dataset.zip'), 'r') as zip_ref:
    zip_ref.extractall(raw_folder_path)


if not os.path.exists(destination_folder):
	os.makedirs(destination_folder)
	print(f"Folder '{destination_folder}' created.")

for subfolder in subfolders:
	subfolder_path = os.path.join(raw_folder_path, 'raw_dataset', subfolder)
	if os.path.exists(subfolder_path):
		files = os.listdir(subfolder_path)
		files.sort()

	for idx, filename in enumerate(files, start=1):
		
		old_file_path = os.path.join(subfolder_path, filename)
            
		with open(old_file_path, 'r', encoding = 'utf-8') as f:
			lines = f.readlines()               
			lines[0] = '<fim_prefix>' + lines[0].lstrip()
			lines[-1] = '<fim_suffix>' + lines[-1].rstrip()
			h = int(0.6 * len(lines))
			lines[h] = "<fim_middle>" + lines[h]
			new_lines = lines[:h] + [lines[-1]] + lines[h:-1]
			tagged_text = '\n'.join(new_lines)
			new_filename = f"{subfolder}_{idx}.txt"            
			new_file_path = os.path.join(destination_folder, new_filename)
                
		with open(new_file_path, 'w', encoding = 'utf-8') as g:
			g.write(tagged_text)

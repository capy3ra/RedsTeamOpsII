import os
import re
from urllib.parse import quote

directory = "RedTeamOpsII-main/2. C2 Infrastructure"

for filename in os.listdir(directory):
    if filename.endswith(".md"):
        file_path = os.path.join(directory, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        updated_content = re.sub(r'!\[\[(.*?)\]\]', lambda match: f'![{match.group(1)}](../{quote(match.group(1))})', content)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

print("File markdown đã được cập nhật.")

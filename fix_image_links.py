import os
import re

def fix_image_links():
    # 遍历content目录下的所有markdown文件
    for root, dirs, files in os.walk('content'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 移除/Notes-for-GradEntranceExam前缀
                image_pattern = re.compile(r'!\[([^\]]*)\]\(/Notes-for-GradEntranceExam/([^)]+)\)')
                new_content = image_pattern.sub(r'![\1](/\2)', content)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'Fixed image links in {file_path}')

if __name__ == '__main__':
    fix_image_links()
    print('Image links fixed successfully!')

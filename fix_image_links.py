import os
import re

# 定义要处理的目录
content_dir = 'content'

# 匹配图片链接的正则表达式，支持不同深度的相对路径
image_pattern = re.compile(r'!\[([^\]]*)\]\((../../../|../../|../)([^)]+)\)')

# 遍历content目录下的所有Markdown文件
def fix_image_links(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f'Processing {file_path}')
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 替换图片链接
                new_content = image_pattern.sub(r'![\1](/\3)', content)
                
                # 如果内容有变化，写入文件
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'Updated {file_path}')
                else:
                    print(f'No changes needed for {file_path}')

if __name__ == '__main__':
    fix_image_links(content_dir)
    print('Image link fixing completed!')

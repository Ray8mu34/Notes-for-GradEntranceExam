import os
import re

# 定义要处理的目录
content_dir = 'content'

# 匹配图片链接的正则表达式
image_pattern = re.compile(r'!\[([^\]]*)\]\((/)([^)]+)\)')

# 遍历所有Markdown文件
def fix_image_links():
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 替换图片链接，添加Notes-for-GradEntranceExam前缀
                new_content = image_pattern.sub(r'![\1](/Notes-for-GradEntranceExam/\3)', content)
                
                # 如果内容有变化，写入文件
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'Fixed image links in: {file_path}')

if __name__ == '__main__':
    fix_image_links()
    print('Image link fixing completed!')

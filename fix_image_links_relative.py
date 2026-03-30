#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复Markdown文件中的图片链接，将绝对路径改为相对路径
"""

import os
import re

def fix_image_links_in_file(file_path):
    """修复单个文件中的图片链接"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 匹配图片链接模式: ![alt](/控制理论笔记/...)
        # 替换为: ![alt](./...)
        pattern = r'!\[([^\]]*)\]\(/控制理论笔记/([^)]+)\)'
        replacement = r'![\1](./\2)'
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"已修复: {file_path}")
            return True
        else:
            print(f"无需修改: {file_path}")
            return False
            
    except Exception as e:
        print(f"处理文件时出错 {file_path}: {e}")
        return False

def main():
    # 处理控制理论笔记
    file_path = 'content/控制理论笔记/index.md'
    if os.path.exists(file_path):
        fix_image_links_in_file(file_path)
    else:
        print(f"文件不存在: {file_path}")

if __name__ == '__main__':
    main()

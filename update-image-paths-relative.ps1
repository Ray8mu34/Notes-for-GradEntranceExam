# PowerShell 脚本：将笔记中的图片链接从绝对路径改为相对路径

# 定义需要修改的文件和路径映射
$filesToUpdate = @(
    @{
        Path = "content\控制理论习题\index.md"
        OldPath = "/控制理论题目/assets/教材做题/"
        NewPath = "./"
    },
    @{
        Path = "content\控制理论笔记\index.md"
        OldPath = "/控制理论笔记/assets/控制理论公式结论汇总/"
        NewPath = "./"
    },
    @{
        Path = "content\微积分笔记\index.md"
        OldPath = "/微积分笔记/assets/微积分公式结论汇总/"
        NewPath = "./"
    }
)

# 遍历每个文件并进行修改
foreach ($file in $filesToUpdate) {
    $fullPath = Join-Path $PSScriptRoot $file.Path
    
    if (Test-Path $fullPath) {
        Write-Host "正在处理文件: $($file.Path)"
        
        # 读取文件内容
        $content = Get-Content -Path $fullPath -Raw
        
        # 替换路径
        $newContent = $content -replace [regex]::Escape($file.OldPath), $file.NewPath
        
        # 写入修改后的内容
        Set-Content -Path $fullPath -Value $newContent -Force
        
        Write-Host "✓ 已成功修改路径: $($file.OldPath) -> $($file.NewPath)"
    } else {
        Write-Host "✗ 文件不存在: $($file.Path)"
    }
}

Write-Host "\n所有文件处理完成！"

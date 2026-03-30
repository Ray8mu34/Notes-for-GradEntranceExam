# 简单的PowerShell脚本：更新图片路径

# 控制理论习题
$file1 = "content\控制理论习题\index.md"
if (Test-Path $file1) {
    Write-Host "处理控制理论习题..."
    $content1 = Get-Content $file1 -Raw
    $content1 = $content1 -replace "./assets/教材做题/", "/控制理论题目/assets/教材做题/"
    Set-Content $file1 -Value $content1 -Force
    Write-Host "完成控制理论习题"
}

# 控制理论笔记
$file2 = "content\控制理论笔记\index.md"
if (Test-Path $file2) {
    Write-Host "处理控制理论笔记..."
    $content2 = Get-Content $file2 -Raw
    $content2 = $content2 -replace "./assets/控制理论公式结论汇总/", "/控制理论笔记/assets/控制理论公式结论汇总/"
    Set-Content $file2 -Value $content2 -Force
    Write-Host "完成控制理论笔记"
}

Write-Host "所有文件处理完成！"

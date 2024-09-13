@echo off
setlocal enabledelayedexpansion

for %%f in (queries\*.sql) do (
    echo %%f

    mysql -h 127.0.0.1 -P 33061 -u root -p"c6h5bwInqtKJKmiuPcBQ0A" censo < "%%f"

    if !errorlevel! neq 0 (
        exit /b 1
    )
)

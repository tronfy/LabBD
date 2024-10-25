@echo off
setlocal enabledelayedexpansion

@REM copy files in mysql-files to C:\ProgramData\MySQL\MySQL Server 8.0\Uploads
xcopy mysql-files\*.* C:\ProgramData\MySQL\MySQL Server 8.0\Uploads /Y

@REM Run all queries
for %%f in (queries\*.sql) do (
    echo %%f

    mysql -h 127.0.0.1 -P 3306 -u root -p"aluno" labbd < "%%f"

    if !errorlevel! neq 0 (
        exit /b 1
    )
)

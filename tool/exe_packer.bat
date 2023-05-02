@echo off

set "src=..\kcauto\__main__.py"
set "target_path=..\kcauto.exe"

for /f "delims=" %%i in ('python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"') do set "python_site_package=%%i"

echo The Python site-packages directory is: %python_site_package%

pyinstaller -F %src% -p ..\kcauto\ -p %python_site_package%

move /y ".\dist\__main__.exe" "%target_path%"

rmdir /s /q ".\dist"
rmdir /s /q ".\build"

del .\__main__.spec

pause
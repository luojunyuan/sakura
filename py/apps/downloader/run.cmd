:: run.cmd

setlocal
REM set PYTHON=..\..\..\..\Python\python.exe
set PYTHON=C:\Users\ljy77\AppData\Local\Programs\Python\Python38\python.exe
:: vid of youtube vidio
set VIDS=XGZ2S6pTkO8 lmOZEAAEMK0

%PYTHON% . %VIDS% --debug
:: I dont know the use of  %*
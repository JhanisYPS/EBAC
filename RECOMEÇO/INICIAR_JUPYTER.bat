@echo off
echo ========================================
echo  Iniciando Jupyter Lab com todos os kernels
echo ========================================
echo.
cd /d "C:\Users\janainaps\Documents\EBAC"
call .venv\Scripts\activate.bat
echo Ambiente ativado!
echo.
echo Abrindo Jupyter Lab...
echo Depois que abrir no navegador:
echo 1. Abra o notebook: Variaveis e Tipos de Dados.ipynb
echo 2. Clique no kernel (canto superior direito)
echo 3. Selecione "Java"
echo.
jupyter lab
pause

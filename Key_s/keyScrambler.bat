@echo off
setlocal EnableDelayedExpansion

:: author ccd3048 Red Team Delta
for %%l in (fr-FR de-DE es-ES ru-RU it-IT) do (
    powershell -command "Set-WinUserLanguageList -LanguageList %%l -Force"
    timeout /t 5
    powershell -command "Set-WinUserLanguageList -LanguageList en-US -Force"
    timeout /t 60
)
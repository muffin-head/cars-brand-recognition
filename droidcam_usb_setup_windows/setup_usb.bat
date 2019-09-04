@echo off
echo Dev47Apps setup_usb..

adb\adb.exe start-server
for /f %%i in ('adb\adb.exe -d get-state') do set state=%%i

if "%state%"=="device" (
	echo Waiting for device to be connected...
	"%~dp0adb\adb.exe" -d wait-for-device
) else (
	echo .
	echo Device not found.
	echo .
	echo * Make sure USB Debugging is enabled on the device, and its in PTP mode [pull down notification and tap USB Options].
	echo .
	echo * Make sure you Allowed USB Debugging if a confirmation dialog appeared on your device.
	echo .
	echo * Make sure you installed the ADB drivers for your device.
	echo   Try this auto installer: http://adbdriver.com/upload/adbdriver.zip
	echo   or check the Android website for links: http://developer.android.com/adb/extras/oem-usb.html#Drivers.
	echo .
	goto end
)

echo.
set /p port=Enter DroidCam port setting from the phone (or press enter to use default 4747):
if "%port%"=="" (set port=4747)

adb\adb.exe -d forward tcp:%port% tcp:%port%

echo OK. You can connect over USB by using IP 127.0.0.1 and port %port%

:end
pause>nul

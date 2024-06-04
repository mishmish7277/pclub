cd %USERPROFILE%\Desktop
echo hello desktop > desktop.txt
cd %USERPROFILE%\Downloads
echo hello downloads > downloads.txt
move %USERPROFILE%\Desktop\desktop.txt %USERPROFILE%\Downloads
move %USERPROFILE%\Downloads\downloads.txt %USERPROFILE%\Desktop
cd %USERPROFILE%\Desktop
mkdir netstat
cd netstat
netstat -n > output.txt
find ":80" output.txt
del output.txt
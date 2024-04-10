rem for /r %%f in (*) do echo %%f
python remove_stubs.py
stubgen ./chemparse -v -o .
pause
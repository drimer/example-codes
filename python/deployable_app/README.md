INSTRUCTIONS

These are the steps I've followed to generate these files (excluding the typical
steps for creating a Python `virtualenv` for the app:

1) Run the commands:
    $ easy_install PasteScript
    $ paster create -t basic_package verycomplexapp
    $ cd verycomplexapp/

2) Edit manually `setup.py` to specify the entry point:

    entry_points={
        'console_scripts': (
          'command_1 = verycomplexapp.main:run_command_1',
        )
    }

3) Add the file `myfirstapp/main.py` and write it just with the function
`run_command_1()`.

4) Now, to install it in the system, I run:

    $ sudo python setup.py install

5) Trying to run the new command:

    $ run_command_1

5) It works!
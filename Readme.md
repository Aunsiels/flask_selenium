# Installation

## Packages

```bash
pip3 install -r requirements.txt
```

## Selenium - Firefox Driver

You need to download the geckodriver on this [page](https://github.com/mozilla/geckodriver/releases).

Then, decompress it:

```bash
tar -xvzf geckodriver*
```

make it executable:

```bash
chmod +x geckodriver
```

and add it to path:

```bash
export PATH=$PATH:/path_to_the_location_containing_the_geckodriver_directory
```

## Configure Pycharm for the tests

Open Pycharm. Import the project. On the top right hand corner, click on "Edit Configurations...". On the new window, click on the Plus, "Python tests", "pytest".

On the new page, check the "Module name" box, then write "app" in the field below. If you have a problem with the PATH variable (i.e. geckodriver is not found), you can configure the Environment Variables in the dedicated field by writting: PATH=$PATH:/path\_to\_the\_location\_containing\_the\_geckodriver\_directory (no export). Click on OK.

Finally, select your new configuration on the top right hand corner and run the tests.



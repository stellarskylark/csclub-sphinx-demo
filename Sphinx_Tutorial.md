---
layout: post
title: Sphinx Tutorial for OBU CS Club
---
# Setup Tasks

  1. Download `astroengisci/csclub-sphinx-demo` from GitHub
  2. Install the Sphinx package in Python according to the installation
     tutorial.
     
     # windows
        1. Install Python from here [Python](https://www.python.org/downloads/)
          note: When installing make sure to check the PATH option so that pip can be invoked from the command line.
        2. Open Command Prompt (cmd) and type in:
        
           ``pip install -U sphinx``
        3. open folder in CMD with CD ex:
          `` cd Downloads\csclub-sphinx-demo ``
     
  3. You're going to be using the terminal/command prompt in this 
     presentation. ***STAY CALM, EVERYTHING WILL BE ALRIGHT***
     
# Creating your Sphinx Documentation Build

  1. Create a `/docs` folder in the cloned repository
  2. Run `sphinx-quickstart` in the `docs` folder. You can use the
     default values for all except:
     - `autodoc` should be included (select `y`)
     - `viewcode` should be included (select `y`)
  3. Run `make html` or, on Windows, `\.make.bat`
  4. Edit `conf.py` to change the source path to the folder containing
     your project's actual code (`..` in this case). Uncomment the lines that import
     os and 
  5. Make a new folder `ref` in `docs`
  6. In the `docs` folder, run `sphinx-apidoc .. -o ref`. This will
     automatically generate reference files for every Python module
     in `..` (the directory above the current one) and stuff them in
     `docs`.
  7. Add `ref/modules` to the table of contents in `index.rst`
  8. Rebuild the documentation.
  9. You're done!
  
# Other Fun Stuff

## Changing the theme
In `conf.py` change `html_theme` at (likely around line 79) to the
Sphinx theme of your choice.

## Autosummary tables

  1. Edit `conf.py` to include the `sphinx.ext.autosummary` extension.
  2. Edit `ref/modules.rst` to use the `.. autosummary::` directive
     rather than the `.. toctree::` directive. 
     - Add the `:toctree:` option to this directive. 
     - Remove the  `:maxdepth:` option.

# cookiecutter-dmarticle

The repository contains `cookiecutter` ([more details](https://cookiecutter.readthedocs.io/en/latest/)) template for LaTeX article for Discrete Mathematics Journal ([site](http://www.mathnet.ru/php/journal.phtml?jrnid=dm&option_lang=eng)).

Template supports two languages: Russian (ru) and English (en).

How to use this template:
1. Install python interpreter
2. Install cookiecutter from the command line using pip:
   ```bash
   pip install cookiecutter
   ```
3. Make a directory for your project.
4. Go to this directory and run the command from the console:
   ```bash
   cookiecutter https://github.com/gf2crypto/cookiecutter-dmarticle.git
   ```
5. Input parameters:
     - **project_name**, the name of your projects (only Latin chars is supported);
     - **language**, language of your article ('en' or 'ru')
     - **create_gitignore**, is it needed to create `.gitignore` file for git projects or not: 'yes' or 'no'.
6. Read comments from tex-files and README. Enjoy!

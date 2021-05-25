**This repository is meant to keep a record of new redditors**

It is built with `Python 3 <https://www.python.org/>`_, `Halo <https://github.com/manrajgrover/halo/>`_, `PRAW <https://github.com/praw-dev/praw/>`_, `PyYAML <https://github.com/yaml/pyyaml/>`_ and `PyGithub <https://github.com/PyGithub/PyGithub/>`_.

It checks the `/users/new <https://www.reddit.com/users/new/>`_ endpoint and updates the `redditors.yaml <https://github.com/IThinkImOKAY/redditors/blob/main/redditors.yaml/>`_ file with new users.

The following data is stored:

- Account Username

- Account ``created_utc`` attribute

- Account's ID

**Setting it up yourself is easy:**

.. code-block:: bash

   git clone https://github.com/IThinkImOKAY/redditors

   cd redditors
   
   pip3 install -r requirements.txt -y
   
You will need to edit the ``config.yaml`` file to fit your needs:

- ``githubRepo`` is your repository's route (ie: ``IThinkImOKAY/redditors``)

- ``githubToken`` is your GitHub access token (requires ``repo`` scope)

- ``redditID`` is your reddit client ID

- ``redditSecret`` is your reddit client secret

- ``redditAgent`` is your reddit user agent

- ``redditUsername`` is your reddit username

- ``redditPassword`` is your reddit password

- Then, simply run the py file:

.. code-block:: bash

   python3 main.py

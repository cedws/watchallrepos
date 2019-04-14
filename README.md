# watchallrepos
A Python script to watch your repositories (and any that you have push access to) if didn't enable the option to auto-subscribe when starting to use GitHub. The script won't *unsubscribe* you from anything, so if you don't want to watch forked repos, pass the correct parameter (`-s`).

# Usage
- Install the dependencies: `pip install -r requirements.txt`
- See a list of parameters: `./watchallrepos.py -h`
- [Create a personal access token (requires full repo and notification permissions)](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
- Run the script: `GITHUB_PA_TOKEN=<TOKEN> ./watchallrepos.py`
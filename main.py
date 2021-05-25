import time, random, yaml, praw, github, halo, prawcore

spinner = halo.Halo(text='Starting Up', spinner={'interval': 100,'frames': ['-', '+', '*', '+', '-']})
spinner.start()

with open('config.yaml') as cy:
    config = yaml.safe_load(cy)
    githubRepo = config['githubRepo']
    githubToken = config['githubToken']
    redditID = config['redditID']
    redditSecret = config['redditSecret']
    redditAgent = config['redditAgent']
    redditUsername = config['redditUsername']
    redditPassword = config['redditPassword']
    spinner.succeed(text='Loaded YAML File')
    
g = github.Github(githubToken)
reddit = praw.Reddit(client_id=redditID,
                     client_secret=redditSecret,
                     user_agent=redditAgent,
                     username=redditUsername,
                     password=redditPassword)

def update_repo():
    repo = g.get_repo(githubRepo)
    file = repo.get_contents('redditors.yaml')
    repo.update_file('redditors.yaml', "Add New Users", open('redditors.yaml').read(), file.sha)
    spinner.succeed(text='Updated GitHub YAML File')
    return

with open('redditors.yaml') as yamlusers:
    data = yaml.safe_load(yamlusers) or {}
    spinner.succeed(text='Loaded User YAML File')

while True:
    try:
        for new_user in reddit.redditors.new():
            new_user = new_user.display_name.split('u_',1)[1]
            user = reddit.redditor(new_user)
            if new_user not in data:
                spinner.info(text=f'Adding /u/{new_user} To YAML File')
                data[new_user] = {'id':user.id,'created_utc':user.created_utc}
                with open('redditors.yaml','w') as yml:
                    yaml.dump(data,yml)
                    spinner.succeed(text='Dumped YAML')
                if random.randint(1,10) == 10:
                    update_repo()
    except prawcore.PrawcoreException as redditError:
        spinner.warn(text=str(redditError))
        time.sleep(60)
    except github.GithubException as githubError:
        spinner.warn(text=str(githubError))
        time.sleep(60)
    except Exception as e:
        spinner.fail(text=str(e))
        print(traceback.format_exc())
        time.sleep(10)
    except KeyboardInterrupt:
        update_repo()
        spinner.warn(text='Shutting Down')
        quit()

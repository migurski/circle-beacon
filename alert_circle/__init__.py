from __future__ import print_function
from argparse import ArgumentParser
import requests, uritemplate

# https://circleci.com/docs/api/
BUILDS_URL = 'https://circleci.com/api/v1.1/project/{vcs_type}/{username}/{project}/tree/{branch}{?circle-token}{&filter,limit}'
RETRY_URL = 'https://circleci.com/api/v1.1/project/{vcs_type}/{username}/{project}/{build_num}/retry{?circle-token}'

parser = ArgumentParser(description='Retry the latest successful build in Circle CI.')

parser.add_argument('owner', help='Github repository owner')
parser.add_argument('repo', help='Github repository name')
parser.add_argument('branch', help='Github branch name')
parser.add_argument('token', help='Circle CI API token')

def main():
    cli = parser.parse_args()
    
    args = {'circle-token': cli.token}
    args.update(vcs_type='github', username=cli.owner, project=cli.repo,
                branch=cli.branch, filter='successful', limit=1)

    url1 = uritemplate.expand(BUILDS_URL, args)
    got = requests.get(url1)
    
    build = got.json()[0]
    print('Found previous build #{build_num} for {vcs_url}'.format(**build))
    
    args.update(build_num=build['build_num'])
    url2 = uritemplate.expand(RETRY_URL, args)
    
    posted = requests.post(url2)
    print('Retrying at {build_url}'.format(**posted.json()))

if __name__ == '__main__':
    exit(main())
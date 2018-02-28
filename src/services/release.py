import random
import string
import os

from git import Repo

from src.services.config import Config

class ReleaseService:

    @classmethod
    def cut(cls, release, major=None, minor=None, patch=None):
        repo = cls.__init_repo(release)
        git = repo.git

        next_tag = cls.__get_next_tag(repo.tags, major, minor, patch)

        git.checkout('develop')
        git.merge('origin/master')
        git.tag(next_tag)

    @classmethod
    def release(cls, release):
        repo = cls.__init_repo(release)
        git = repo.git

        last_tag = cls.__get_last_tag(repo.tags)

        git.checkout('master')
        git.merge('develop')
        git.tag(next_tag)

    @classmethod
    def __get_next_tag(cls, tags, major, minor, patch):
        last_tag = cls.__get_last_tag(tags)
        last_major, last_minor, last_patch = last_tag.split('.')

        if not minor and not patch:
            major = int(last_major) + 1
            minor = last_minor
            patch = last_patch
        elif minor:
            major = last_major
            minor = int(last_minor) + 1
            patch = last_patch
        elif patch:
            major = last_major
            minor = last_minor
            patch = int(last_patch) + 1

        tag_strings = map(lambda t: str(t), [major, minor, patch])

        return '.'.join(tag_strings)

    @classmethod
    def __get_last_tag(cls, tags):
        sort_key = lambda t: t.path.split('/')[-1]
        sorted_tags = iter(sorted(tags, key=sort_key, reverse=True))

        try:
            return next(sorted_tags).path.split('/')[-1]
        except Exception:
            return '0.0.0'

    @classmethod
    def __init_repo(cls, release):
        alphabet = (string.ascii_uppercase +
            string.ascii_lowercase + string.digits)
        write_dir = ''.join(
            random.choice(alphabet) for _ in range(16)
        )
        url_with_cred = cls.__get_url_cred(release.repo_url)

        repo = Repo.clone_from(
            url_with_cred,
            '/tmp/{dir}'.format(dir=write_dir),
            branch='develop'
        )

        with repo.config_writer() as cw:
            cw.set_value('user', 'email', Config['git']['email'])
            cw.set_value('user', 'name', Config['git']['author'])

        return repo

    @classmethod
    def __get_url_cred(cls, url):
        host= url.split('www.')[1].split('.git')[0]
        token = os.environ['AHOY_TOKEN_GIT']

        return '{proto}://{token}:x-oauth-basic@{host}.git'.format(
            proto='https',
            token=token,
            host=host
        )


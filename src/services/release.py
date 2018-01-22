import random, string

from git import Repo

class ReleaseService:

    @classmethod
    def cut(cls, release, major=None, minor=None, patch=None):
        alphabet = (string.ascii_uppercase +
            string.ascii_lowercase + string.digits)
        write_dir = ''.join(
            random.choice(alphabet) for _ in range(16)
        )

        repo = Repo.clone_from(
            release.repo_url,
            '/tmp/{dir}'.format(dir=write_dir),
            branch='develop'
        )
        git = repo.git

        sort_key = lambda t: t.path.split('/')[-1]
        tags = iter(sorted(repo.tags, key=sort_key, reverse=True))

        next_tag = cls.__get_next_tag(tags, major, minor, patch)

        git.checkout('master')
        git.merge('develop')
        git.tag(next_tag)

    @classmethod
    def __get_next_tag(cls, tags, major, minor, patch):

        try:
            last_tag = next(tags).path.split('/')[-1]
        except Exception:
            last_tag = '0.0.0'

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

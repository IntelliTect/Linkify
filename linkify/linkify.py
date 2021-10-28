import logging
import re
import sys
from typing import Tuple
import warnings

import bs4

from .db_context import DbContext
from .env import LINK_PATTERN
from .posts import Post


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs/log.txt')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)


RE_LINK_PATTERN = re.compile(LINK_PATTERN)


class Linkify:
    def fix_post_links(self, post: Post) -> Tuple[bool, Post]:
        post_content_changes, updated_post_content = self.fix(post.post_content, post.post_id)
        post_content_filtered_changed, updated_post_content_filtered = self.fix(post.post_content_filtered, post.post_id)
        post = Post(
            post.post_id,
            post.post_type,
            updated_post_content,
            updated_post_content_filtered,
        )
        changes_made = post_content_changes or post_content_filtered_changed
        return changes_made, post

    @classmethod
    def fix(cls, content: str, post_id: str) -> Tuple[bool, str]:
        soup = bs4.BeautifulSoup(content, "html.parser")
        changes_made = False

        for link in soup.find_all("a"):
            href = link.get("href")
            if href is not None:
                replaced, relative_href = cls.fix_link(href, post_id)
                changes_made = changes_made or replaced
                if replaced:
                    link["href"] = relative_href

        for img in soup.find_all("img"):
            src = img.get("src")
            if src is not None:
                replaced, relative_src = cls.fix_link(src, post_id)
                changes_made = changes_made or replaced
                if replaced:
                    img["src"] = relative_src

        updated_content = soup.decode(pretty_print=False, formatter="html")
        return changes_made, updated_content

    @staticmethod
    def fix_link(link: str, post_id: str) -> Tuple[bool, str]:
        if RE_LINK_PATTERN.match(link):
            relative_link = re.sub(RE_LINK_PATTERN, "", link)
            logger.info(f"post_id={post_id} replacing: {link} -> {relative_link}")
            return True, relative_link
        return False, link


def main():
    dry_run = len(sys.argv) < 2 or sys.argv[1] != "commit"
    logging.info(f"dry_run={dry_run}")

    with DbContext() as db_context:
        posts = db_context.query_posts()

    warnings.filterwarnings("ignore", category=bs4.MarkupResemblesLocatorWarning)
    linkify = Linkify()
    updated_posts: list[Post] = []
    for post in posts:
        changes_mades, updated_post = linkify.fix_post_links(post)
        if changes_mades:
            updated_posts.append(updated_post)
    warnings.resetwarnings()

    with DbContext() as db_context:
        for post in updated_posts:
            db_context.update_post(post, dry_run)

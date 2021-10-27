import logging
import re
import sys
from typing import Tuple

import bs4

from .db_context import DbContext
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


INTELLITECT_LINK_PATTERN = re.compile(r"http[s]?:\/\/intellitect\.com")


class Linkify:
    def fix_post_links(self, post: Post) -> Post:
        updated_post_content = self.fix(post.post_content)
        updated_post_content_filtered = self.fix(post.post_content_filtered)
        post = Post(
            post.post_id,
            post.post_type,
            updated_post_content,
            updated_post_content_filtered,
        )
        return post

    @classmethod
    def fix(cls, content: str) -> str:
        soup = bs4.BeautifulSoup(content, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")
            if href is not None:
                replaced, relative_href = cls.fix_link(href)
                if replaced:
                    link["href"] = relative_href

        for img in soup.find_all("img"):
            src = img.get("src")
            if src is not None:
                replaced, relative_src = cls.fix_link(src)
                if replaced:
                    img["src"] = relative_src

        updated_content = soup.decode(pretty_print=False, formatter="html")
        return updated_content

    @staticmethod
    def fix_link(link: str) -> Tuple[bool, str]:
        if INTELLITECT_LINK_PATTERN.match(link):
            relative_href = re.sub(INTELLITECT_LINK_PATTERN, "", link)
            return True, relative_href
        return False, link


def main():
    dry_run = len(sys.argv) < 2 or sys.argv[1] != "commit"
    logging.info(f"dry_run={dry_run}")

    with DbContext() as db_context:
        posts = db_context.query_posts()

    linkify = Linkify()
    updated_posts: list[Post] = []
    for post in posts:
        updated_post = linkify.fix_post_links(post)
        if updated_post != post:
            updated_posts.append(updated_post)

    with DbContext() as db_context:
        for post in updated_posts:
            db_context.update_post(post, dry_run)

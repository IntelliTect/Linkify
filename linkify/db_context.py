import logging

from .connection import Connection
from .posts import Post


logger = logging.getLogger(__name__)


class DbContext:
    def __enter__(self):
        connection = Connection()
        connection.connect()
        self.connection = connection
        return self

    def __exit__(self, _, __, ___):
        self.connection.disconnect()

    def query_posts(self) -> list[Post]:
        query = (
            "SELECT ID, post_type, post_content, post_content_filtered "
            "FROM wp_posts "
            "WHERE post_title = %s "
            "ORDER BY ID "
        )
        self.connection.cursor.execute(query, ("Demystifying the SDET Unicorn",))
        posts: list[Post] = [
            Post(*post)
            for post
            in self.connection.cursor
        ]
        return posts

    def update_post(self, post: Post, dry_run=True):
        query = (
            "UPDATE wp_posts "
            "SET post_content = %s, post_content_filtered = %s "
            "WHERE ID = %s"
        )
        self.connection.cursor.execute(query, (post.post_content, post.post_content_filtered, post.post_id))
        if dry_run:
            logger.info(f"[DRY RUN] updating={post.post_id}")
            self.connection.connection.rollback()
        else:
            logger.info(f"updating={post.post_id}")
            self.connection.connection.commit()

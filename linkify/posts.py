import dataclasses


@dataclasses.dataclass
class Post:
    post_id: str
    post_type: str
    post_content: str
    post_content_filtered: str

    def __repr__(self) -> str:
        return f"post_id={self.post_id} ({self.post_type})"

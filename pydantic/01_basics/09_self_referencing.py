from pydantic import BaseModel
from typing import List, Optional




class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None # replies (Optional means might be there and might not be there) but if they're there then they're a type of list of type 'Comment' which by default should be 'None'



# This is required after using the model for self-referencing, otherwise there will be crazy amount of performance degradation
Comment.model_rebuild()


comment = Comment(
    id=2,
    content="First Comment",
    replies=[
        Comment(id=2, content="Reply-1"),
        Comment(id=3, content="Reply-2", replies=[
            Comment(id=4, content="nested reply")
        ]),
    ]
)

print(comment)
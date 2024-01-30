from datetime import datetime
from typing import List, Optional

from pydantic import Field

from ..models import CamelModel
from ..types import ObjectId


class JobDescription(CamelModel):
    default: str = Field(..., description="Description of the postion")
    original: Optional[str] = Field(
        None, description="Original description of the position"
    )


class JobPost(CamelModel):
    job_post_id: ObjectId = Field(..., description="Internal job post ID")
    company_id: ObjectId = Field(..., description="Internal company ID")
    url: str = Field(..., description="Job post URL")
    published: datetime = Field(..., description="When the job post was published")
    location: Optional[str] = Field(None, description="Location of the position")
    job_description: Optional[str] = Field(
        None, description="Description of the position"
    )
    language: Optional[str] = Field(
        None, description="Original language of the job post"
    )
    title: str = Field(..., description="Position title")
    added: datetime = Field(..., description="When the job post was added to delphai")
    deactivated: Optional[datetime] = Field(
        None, description="When the job post deactivated"
    )
    is_active: bool = Field(..., description="Whether the job post is active or not")
    description: Optional[JobDescription] = None


class JobPosts(CamelModel):
    results: List[JobPost]
    total: int = Field(..., description="Number of results")

from typing import List, Literal
from pydantic import BaseModel
import uuid


class SlideContentUpdate(BaseModel):
    index: int
    content: dict


class EditPresentationRequest(BaseModel):
    presentation_id: uuid.UUID
    slides: List[SlideContentUpdate]
    export_as: Literal["pptx", "pdf"] = "pptx"


# --- Sigyn fork : rendu direct depuis des slides PRE-CONSTRUITES (bypass etape A + B) -------
from typing import Optional  # noqa: E402


class PrebuiltSlide(BaseModel):
    index: int
    layout_id: Optional[str] = None
    content: dict


class RenderFromSlidesRequest(BaseModel):
    template: str = "general"
    title: Optional[str] = None
    slides: List[PrebuiltSlide]
    export_as: Literal["pptx", "pdf"] = "pptx"

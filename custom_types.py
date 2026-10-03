import pydantic

class RAGChunkAndSrc(pydantic.BaseModel):
    chunk: list[str]
    source_id: str = None
    

class RAGUpsertResult(pydantic.BaseModel):
    ingested: int
    
class RAGSearchResult(pydantic.BaseModel):
    context: list[str]
    source: list[str]
    
class RAGQueryResult(pydantic.BaseModel):
    answer: str
    source: list[str]
    num_context: int
    
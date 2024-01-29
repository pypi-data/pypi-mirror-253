import warnings

from sentence_transformers import SentenceTransformer, util
from torch import Tensor, stack, topk

# to remove typed storage warning
warnings.filterwarnings(
    "ignore", category=UserWarning, message="TypedStorage is deprecated"
)

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed(query: list[str] | str, convert_to_tensor: bool = False):
    return model.encode(
        query,
        show_progress_bar=True,
        convert_to_tensor=convert_to_tensor,
        normalize_embeddings=True,
    )


def similarity(query: Tensor, corpus: list[Tensor]):
    top_k = min(5, len(corpus))
    hits = util.dot_score(query, stack(corpus))
    return topk(hits[0], k=top_k)

from contextvars import ContextVar

feedback_ctx = ContextVar("feedback_ctx", default=None)

class FeedbackContextManager:
    def __init__(self, message_id: str):
        feedback_ctx.set(message_id)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        feedback_ctx.set(None)


def parent(message_id: str) -> FeedbackContextManager:
    return FeedbackContextManager(message_id)

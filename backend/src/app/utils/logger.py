import structlog


def setup_logger():
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.JSONRenderer()
        ],
        wrapper_class=structlog.BoundLogger,
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory()
    )
    return structlog.get_logger()

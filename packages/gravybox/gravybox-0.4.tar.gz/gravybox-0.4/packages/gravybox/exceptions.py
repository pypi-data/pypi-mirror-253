from gravybox.betterstack import collect_logger

logger = collect_logger()


class UpstreamAPIFailure(Exception):
    def __init__(self, query, upstream_api, upstream_status_code, upstream_content):
        super().__init__("upstream api failure")
        logger.warning(
            "upstream api failure",
            extra={"query": query,
                   "upstream_api": upstream_api,
                   "status_code": upstream_status_code,
                   "content": upstream_content
                   }
        )

import asyncio
from enum import Enum
import random

from centrifuge.codes import _ErrorCode


def _backoff(step: int, min_value: float, max_value: float):
    """
    Implements exponential backoff with jitter.
    Using full jitter technique - see https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/
    """
    if step > 31:
        step = 31
    interval = random.uniform(0, min(max_value, min_value * 2 ** step))
    return min(max_value, min_value + interval)


def _code_message(code: Enum):
    return str(code.name).lower().replace("_", " ")


def _code_number(code: Enum):
    return int(code.value)


def _is_token_expired(code: int):
    return code == _ErrorCode.TOKEN_EXPIRED.value


async def _wait_for_future(future, timeout):
    """
    asyncio.wait_for() cancels the future if the timeout expires. This function does not.
    """
    future_task = asyncio.ensure_future(future)
    # Create a task that completes after a timeout
    timeout_task = asyncio.ensure_future(asyncio.sleep(timeout))

    # Wait for either the future to complete or the timeout
    done, pending = await asyncio.wait(
        {future_task, timeout_task},
        return_when=asyncio.FIRST_COMPLETED
    )

    # Cancel the timeout task if it's still pending (i.e., the future completed first)
    if timeout_task in pending:
        timeout_task.cancel()

    # Check if the future is done
    if future_task in done:
        # The future completed within the timeout
        return True
    else:
        # The future did not complete within the timeout
        return False

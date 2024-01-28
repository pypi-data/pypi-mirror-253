# The MIT License (MIT)
# Copyright © 2023 Yuma Rao
# Copyright © 2023 philanthrope

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import math
import asyncio
from redis import asyncio as aioredis
import bittensor as bt

# Constants for storage limits in bytes
STORAGE_LIMIT_SUPER_SAIYAN = 1024**6 * 1  # 1 EB
STORAGE_LIMIT_DIAMOND = 1024**5 * 1  # 1 PB
STORAGE_LIMIT_GOLD = 1024**4 * 100  # 100 TB
STORAGE_LIMIT_SILVER = 1024**4 * 10  # 10 TB
STORAGE_LIMIT_BRONZE = 1024**4 * 1  # 1 TB

# Requirements for each tier. These must be maintained for a miner to remain in that tier.
SUPER_SAIYAN_STORE_SUCCESS_RATE = 0.999  # 1/1000 chance of failure
SUPER_SAIYAN_RETIREVAL_SUCCESS_RATE = 0.999  # 1/1000 chance of failure
SUPER_SAIYAN_CHALLENGE_SUCCESS_RATE = 0.999  # 1/1000 chance of failure

DIAMOND_STORE_SUCCESS_RATE = 0.99  # 1/100 chance of failure
DIAMOND_RETRIEVAL_SUCCESS_RATE = 0.99  # 1/100 chance of failure
DIAMOND_CHALLENGE_SUCCESS_RATE = 0.99  # 1/100 chance of failure

GOLD_STORE_SUCCESS_RATE = 0.975  # 1/50 chance of failure
GOLD_RETRIEVAL_SUCCESS_RATE = 0.975  # 1/50 chance of failure
GOLD_CHALLENGE_SUCCESS_RATE = 0.975  # 1/50 chance of failure

SILVER_STORE_SUCCESS_RATE = 0.95  # 1/20 chance of failure
SILVER_RETRIEVAL_SUCCESS_RATE = 0.95  # 1/20 chance of failure
SILVER_CHALLENGE_SUCCESS_RATE = 0.95  # 1/20 chance of failure

SUPER_SAIYAN_TIER_REWARD_FACTOR = 1.0  # Get 100% rewards
DIAMOND_TIER_REWARD_FACTOR = 0.888  # Get 88.8% rewards
GOLD_TIER_REWARD_FACTOR = 0.777  # Get 77.7% rewards
SILVER_TIER_REWARD_FACTOR = 0.555  # Get 55.5% rewards
BRONZE_TIER_REWARD_FACTOR = 0.444  # Get 44.4% rewards

SUPER_SAIYAN_TIER_TOTAL_SUCCESSES = 10**5  # 100,000
DIAMOND_TIER_TOTAL_SUCCESSES = 10**4 * 5  # 50,000
GOLD_TIER_TOTAL_SUCCESSES = 10**3 * 5  # 5,000
SILVER_TIER_TOTAL_SUCCESSES = 10**3  # 1,000


def wilson_score_interval(successes, total, confidence=0.95):
    if total == 0:
        return 0, 1

    z_dict = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}

    z = z_dict.get(confidence, 1.96)

    p = successes / total
    denominator = 1 + z**2 / total
    centre_adjusted_probability = p + z**2 / (2 * total)
    adjusted_standard_deviation = math.sqrt(
        (p * (1 - p) + z**2 / (4 * total)) / total
    )

    lower_bound = (
        centre_adjusted_probability - z * adjusted_standard_deviation
    ) / denominator
    upper_bound = (
        centre_adjusted_probability + z * adjusted_standard_deviation
    ) / denominator

    return max(0, lower_bound), min(upper_bound, 1)


async def reset_storage_stats(stats_key: str, database: aioredis.Redis):
    """
    Asynchronously resets the storage statistics for a miner.

    This function should be called periodically to reset the statistics for a miner while keeping the tier and total_successes.

    Args:
        ss58_address (str): The unique address (hotkey) of the miner.
        database (redis.Redis): The Redis client instance for database operations.
    """
    await database.hmset(
        stats_key,
        {
            "store_attempts": 0,
            "store_successes": 0,
            "challenge_successes": 0,
            "challenge_attempts": 0,
            "retrieve_successes": 0,
            "retrieve_attempts": 0,
        },
    )


async def rollover_storage_stats(database: aioredis.Redis):
    """
    Asynchronously resets the storage statistics for all miners.
    This function should be called periodically to reset the statistics for all miners.
    Args:
        database (redis.Redis): The Redis client instance for database operations.
    """
    miner_stats_keys = [stats_key async for stats_key in database.scan_iter("stats:*")]
    tasks = [reset_storage_stats(stats_key, database) for stats_key in miner_stats_keys]
    await asyncio.gather(*tasks)


async def miner_is_registered(ss58_address: str, database: aioredis.Redis):
    """
    Checks if a miner is registered in the database.

    Parameters:
        ss58_address (str): The key representing the hotkey.
        database (redis.Redis): The Redis client instance.

    Returns:
        True if the miner is registered, False otherwise.
    """
    return await database.exists(f"stats:{ss58_address}")


async def register_miner(ss58_address: str, database: aioredis.Redis):
    """
    Registers a new miner in the decentralized storage system, initializing their statistics.
    This function creates a new entry in the database for a miner with default values,
    setting them initially to the Bronze tier and assigning the corresponding storage limit.
    Args:
        ss58_address (str): The unique address (hotkey) of the miner to be registered.
        database (redis.Redis): The Redis client instance for database operations.
    """
    # Initialize statistics for a new miner in a separate hash
    await database.hmset(
        f"stats:{ss58_address}",
        {
            "store_attempts": 0,
            "store_successes": 0,
            "challenge_successes": 0,
            "challenge_attempts": 0,
            "retrieve_successes": 0,
            "retrieve_attempts": 0,
            "total_successes": 0,
            "tier": "Bronze",  # Init to bronze status
            "storage_limit": STORAGE_LIMIT_BRONZE,  # in GB
        },
    )


async def update_statistics(
    ss58_address: str, success: bool, task_type: str, database: aioredis.Redis
):
    """
    Updates the statistics of a miner in the decentralized storage system.
    If the miner is not already registered, they are registered first. This function updates
    the miner's statistics based on the task performed (store, challenge, retrieve) and whether
    it was successful.
    Args:
        ss58_address (str): The unique address (hotkey) of the miner.
        success (bool): Indicates whether the task was successful or not.
        task_type (str): The type of task performed ('store', 'challenge', 'retrieve').
        database (redis.Redis): The Redis client instance for database operations.
    """
    # Check and see if this miner is registered.
    if not await miner_is_registered(ss58_address, database):
        bt.logging.debug(f"Registering new miner {ss58_address}...")
        await register_miner(ss58_address, database)

    # Update statistics in the stats hash
    stats_key = f"stats:{ss58_address}"

    if task_type in ["store", "challenge", "retrieve"]:
        await database.hincrby(stats_key, f"{task_type}_attempts", 1)
        if success:
            await database.hincrby(stats_key, f"{task_type}_successes", 1)

    # Transition retireval -> retrieve successes (legacy)
    legacy_retrieve_successes = await database.hget(stats_key, "retrieval_successes")
    if legacy_retrieve_successes is not None:
        await database.hset(
            stats_key, "retrieve_successes", int(legacy_retrieve_successes)
        )
        await database.hdel(stats_key, "retrieval_successes")

    # Transition retireval -> retrieve attempts (legacy)
    legacy_retrieve_attempts = await database.hget(stats_key, "retrieval_attempts")
    if legacy_retrieve_attempts is not None:
        await database.hset(
            stats_key, "retrieve_attempts", int(legacy_retrieve_attempts)
        )
        await database.hdel(stats_key, "retrieval_attempts")

    # Update the total successes that we rollover every epoch
    if await database.hget(stats_key, "total_successes") is None:
        store_successes = int(await database.hget(stats_key, "store_successes"))
        challenge_successes = int(await database.hget(stats_key, "challenge_successes"))
        retrieval_successes = int(await database.hget(stats_key, "retrieve_successes"))
        total_successes = store_successes + retrieval_successes + challenge_successes
        await database.hset(stats_key, "total_successes", total_successes)
    if success:
        await database.hincrby(stats_key, "total_successes", 1)


async def compute_tier(stats_key: str, database: aioredis.Redis, confidence=0.95):
    if not await database.exists(stats_key):
        bt.logging.warning(f"Miner key {stats_key} is not registered!")
        return

    # Retrieve statistics from the database
    challenge_successes = int(
        await database.hget(stats_key, "challenge_successes") or 0
    )
    challenge_attempts = int(await database.hget(stats_key, "challenge_attempts") or 0)
    retrieval_successes = int(await database.hget(stats_key, "retrieve_successes") or 0)
    retrieval_attempts = int(await database.hget(stats_key, "retrieve_attempts") or 0)
    store_successes = int(await database.hget(stats_key, "store_successes") or 0)
    store_attempts = int(await database.hget(stats_key, "store_attempts") or 0)
    total_successes = int(await database.hget(stats_key, "total_successes") or 0)

    # Calculate Wilson score intervals for each task type
    challenge_success_rate_lower, _ = wilson_score_interval(
        challenge_successes, challenge_attempts, confidence
    )
    retrieval_success_rate_lower, _ = wilson_score_interval(
        retrieval_successes, retrieval_attempts, confidence
    )
    store_success_rate_lower, _ = wilson_score_interval(
        store_successes, store_attempts, confidence
    )
    bt.logging.trace(
        f"Miner {stats_key} success rates: challenge={challenge_success_rate_lower}, retrieve={retrieval_success_rate_lower}, store={store_success_rate_lower}"
    )

    # Use the lower bounds of the intervals to determine the tier
    tier = "Bronze"  # Default tier

    if (
        challenge_success_rate_lower >= SUPER_SAIYAN_CHALLENGE_SUCCESS_RATE
        and retrieval_success_rate_lower >= SUPER_SAIYAN_RETIREVAL_SUCCESS_RATE
        and store_success_rate_lower >= SUPER_SAIYAN_STORE_SUCCESS_RATE
        and total_successes >= SUPER_SAIYAN_TIER_TOTAL_SUCCESSES
    ):
        tier = "Super Saiyan"
    elif (
        challenge_success_rate_lower >= DIAMOND_CHALLENGE_SUCCESS_RATE
        and retrieval_success_rate_lower >= DIAMOND_RETRIEVAL_SUCCESS_RATE
        and store_success_rate_lower >= DIAMOND_STORE_SUCCESS_RATE
        and total_successes >= DIAMOND_TIER_TOTAL_SUCCESSES
    ):
        tier = "Diamond"
    elif (
        challenge_success_rate_lower >= GOLD_CHALLENGE_SUCCESS_RATE
        and retrieval_success_rate_lower >= GOLD_RETRIEVAL_SUCCESS_RATE
        and store_success_rate_lower >= GOLD_STORE_SUCCESS_RATE
        and total_successes >= GOLD_TIER_TOTAL_SUCCESSES
    ):
        tier = "Gold"
    elif (
        challenge_success_rate_lower >= SILVER_CHALLENGE_SUCCESS_RATE
        and retrieval_success_rate_lower >= SILVER_RETRIEVAL_SUCCESS_RATE
        and store_success_rate_lower >= SILVER_STORE_SUCCESS_RATE
        and total_successes >= SILVER_TIER_TOTAL_SUCCESSES
    ):
        tier = "Silver"

    # Update the tier in the database
    await database.hset(stats_key, "tier", tier)

    # Update storage limit based on tier
    if tier == "Super Saiyan":
        storage_limit = STORAGE_LIMIT_SUPER_SAIYAN
    elif tier == "Diamond":
        storage_limit = STORAGE_LIMIT_DIAMOND
    elif tier == "Gold":
        storage_limit = STORAGE_LIMIT_GOLD
    elif tier == "Silver":
        storage_limit = STORAGE_LIMIT_SILVER
    else:  # Bronze
        storage_limit = STORAGE_LIMIT_BRONZE

    current_limit = await database.hget(stats_key, "storage_limit")
    if current_limit.decode() != storage_limit:
        await database.hset(stats_key, "storage_limit", storage_limit)
        bt.logging.trace(
            f"Storage limit for {stats_key} set from {current_limit} -> {storage_limit} bytes."
        )


async def compute_all_tiers(database: aioredis.Redis):
    # Iterate over all miners
    """
    Asynchronously computes and updates the tiers for all miners in the decentralized storage system.
    This function should be called periodically to ensure miners' tiers are up-to-date based on
    their performance. It iterates over all miners and calls `compute_tier` for each one.
    Args:
        database (redis.Redis): The Redis client instance for database operations.
    """
    miners = [miner async for miner in database.scan_iter("stats:*")]
    tasks = [compute_tier(miner, database) for miner in miners]
    await asyncio.gather(*tasks)

    # Reset the statistics for the next epoch
    bt.logging.info("Resetting statistics for all hotkeys...")
    await rollover_storage_stats(database)


async def get_tier_factor(ss58_address: str, database: aioredis.Redis):
    """
    Retrieves the reward factor based on the tier of a given miner.
    This function returns a factor that represents the proportion of rewards a miner
    is eligible to receive based on their tier.
    Args:
        ss58_address (str): The unique address (hotkey) of the miner.
        database (redis.Redis): The Redis client instance for database operations.
    Returns:
        float: The reward factor corresponding to the miner's tier.
    """
    tier = await database.hget(f"stats:{ss58_address}", "tier")
    if tier == b"Super Saiyan":
        return SUPER_SAIYAN_TIER_REWARD_FACTOR
    elif tier == b"Diamond":
        return DIAMOND_TIER_REWARD_FACTOR
    elif tier == b"Gold":
        return GOLD_TIER_REWARD_FACTOR
    elif tier == b"Silver":
        return SILVER_TIER_REWARD_FACTOR
    else:
        return BRONZE_TIER_REWARD_FACTOR

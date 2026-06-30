import logging

import httpx

from app.core.config import settings

logger = logging.getLogger(__name__)


def get_recommendations(user_id: int, limit: int) -> list[dict] | None:
    try:
        url = f"{settings.RECOMMENDER_URL}/recommend/reels"
        params = {"user_id": user_id, "limit": limit}
        response = httpx.get(
            url,
            params=params,
            timeout=settings.RECOMMENDER_TIMEOUT,
        )
        if response.status_code == 200:
            data = response.json()
            return data.get("items", [])  # expects list of {"reel_id": int, "reason": str}
        else:
            logger.error(f"Recommender service returned status {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"Failed to fetch recommendations: {e}")
        return None

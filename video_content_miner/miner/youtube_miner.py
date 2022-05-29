import re
from typing import Any, Dict, List

from youtube_transcript_api import YouTubeTranscriptApi

class YoutubeMiner:
    @staticmethod
    def get_video_id(url: str) -> str:
        # https://www.youtube.com/watch?v=ngCos392W4w
        # https://www.youtube.com/watch?v=8ncJcZf3Bmg&list=PL2TI5gWVjce_zDEN0zHr-Hif7_6mjtZtS
        video_id_with_noise = re.search("v=.+", url).group()
        video_id = re.sub("(^v=|&.+$)", "", video_id_with_noise)

        return video_id

    @staticmethod
    def get_transcript(video_id: str) -> List[Dict[str, Any]]:
        return YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'zh-TW'])

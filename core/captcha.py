import asyncio
from capmonster_python import TurnstileTask

CAPTCHA_PARAMS = {
    'website_key': '0x4AAAAAAAx1CyDNL8zOEPe7',
    'website_url': 'https://app.nodepay.ai/login'
}

class CaptchaService:
    def __init__(self, api_key):
        self.capmonster = TurnstileTask(api_key)

    def get_captcha_token(self):
        task_id = self.capmonster.create_task(
            **CAPTCHA_PARAMS
        )
        return self.capmonster.join_task_result(task_id).get("token")

    async def get_captcha_token_async(self):
        return await asyncio.to_thread(self.get_captcha_token)

    # Add alias for compatibility
    async def solve_captcha(self):
        return await self.get_captcha_token_async()

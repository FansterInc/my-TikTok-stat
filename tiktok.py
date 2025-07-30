from TikTokApi import TikTokApi

def get_tiktok_stats(username):
    with TikTokApi() as api:
        user = api.user(username)
        stats = user.info_full()["userInfo"]["stats"]
        return {
            "followers": stats["followerCount"],
            "likes": stats["heartCount"],
            "videos": stats["videoCount"]
        }
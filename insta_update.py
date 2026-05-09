import instaloader
import json
import os

def fetch_instagram_posts(username, count=6):
    # ブラウザ（MacのChrome）を名乗る設定を追加してブロックを回避します
    loader = instaloader.Instaloader(
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
    
    try:
        print(f"{username} の投稿を取得中...")
        profile = instaloader.Profile.from_username(loader.context, username)
        
        posts_data = []
        
        for post in profile.get_posts():
            if len(posts_data) >= count:
                break
            
            if not post.is_video:
                posts_data.append({
                    "url": post.url,
                    "link": f"https://www.instagram.com/p/{post.shortcode}/",
                    "date": post.date_utc.strftime("%Y-%m-%d")
                })
        
        # 取得件数を確認
        print(f"取得件数: {len(posts_data)}")

        with open('posts.json', 'w', encoding='utf-8') as f:
            json.dump(posts_data, f, ensure_ascii=False, indent=4)
            
        print("成功: posts.json を更新しました。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        # 失敗した場合は空のリストで上書きしてエラーを防ぐ
        with open('posts.json', 'w', encoding='utf-8') as f:
            json.dump([], f)

if __name__ == "__main__":
    fetch_instagram_posts("yasuz.kitchen")

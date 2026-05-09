import instaloader
import json
import os

def fetch_instagram_posts(username, count=6):
    # インスタローダーの初期化
    loader = instaloader.Instaloader()
    
    try:
        print(f"{username} の投稿を取得中...")
        # プロフィール情報の読み込み
        profile = instaloader.Profile.from_username(loader.context, username)
        
        posts_data = []
        
        # 投稿を新しい順にスキャン
        for post in profile.get_posts():
            if len(posts_data) >= count:
                break
            
            # 動画を除外（画像のみを対象）
            if not post.is_video:
                posts_data.append({
                    "url": post.url,
                    "link": f"https://www.instagram.com/p/{post.shortcode}/",
                    "date": post.date_utc.strftime("%Y-%m-%d")
                })
        
        # posts.json という名前で保存
        with open('posts.json', 'w', encoding='utf-8') as f:
            json.dump(posts_data, f, ensure_ascii=False, indent=4)
            
        print(f"成功: {len(posts_data)}件の投稿を posts.json に書き出しました。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        # エラーが起きてもワークフローを止めないよう、最低限の空リストを作る
        if not os.path.exists('posts.json'):
            with open('posts.json', 'w') as f:
                json.dump([], f)

if __name__ == "__main__":
    # 対象のアカウント名
    fetch_instagram_posts("yasuz.kitchen")

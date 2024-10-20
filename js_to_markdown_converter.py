import json
from datetime import datetime
import re
from loguru import logger

logger.add("debug.log", rotation="500 MB")

def extract_json_objects(js_content):
    # 最初の '[' と最後の ']' を探す
    start = js_content.find('[')
    end = js_content.rfind(']')
    if start == -1 or end == -1:
        raise ValueError("有効なJSONアレイが見つかりません")
    
    # JSONアレイを抽出
    json_array = js_content[start:end+1]
    
    # JSONとして解析
    return json.loads(json_array)

def parse_js_to_markdown(js_content):
    logger.info("JSコンテンツの解析を開始")
    
    try:
        json_objects = extract_json_objects(js_content)
        logger.success(f"{len(json_objects)}個のJSONオブジェクトの解析に成功しました")
    except json.JSONDecodeError as e:
        logger.error(f"JSONの解析に失敗しました: {str(e)}")
        raise
    except ValueError as e:
        logger.error(f"JSONの抽出に失敗しました: {str(e)}")
        raise

    markdown_output = ""
    logger.info(f"合計 {len(json_objects)} 件のツイートを処理します")

    for i, tweet_obj in enumerate(json_objects, 1):
        logger.debug(f"ツイート {i}/{len(json_objects)} を処理中")
        tweet_data = tweet_obj.get('tweet', {})
        
        # created_atを抽出
        created_at = tweet_data.get('created_at', '')
        if created_at:
            # 日付をフォーマット
            date_obj = datetime.strptime(created_at, "%a %b %d %H:%M:%S +0000 %Y")
            formatted_date = date_obj.strftime("%Y年%m月%d日")
        else:
            formatted_date = "日付不明"
            logger.warning(f"ツイート {i} の日付が見つかりません")

        # full_textを抽出
        full_text = tweet_data.get('full_text', '')
        if full_text:
            # URLを除去（簡易的な方法）
            full_text = re.sub(r'https?://\S+', '', full_text)
            full_text = full_text.strip()
        else:
            full_text = "テキスト不明"
            logger.warning(f"ツイート {i} のテキストが見つかりません")

        # マークダウン形式で出力を作成
        markdown_output += f"## {formatted_date}\n\n{full_text}\n\n"

    logger.success("全てのツイートの処理が完了しました")
    return markdown_output

# ファイル名
js_filename = r"data\tweets.js"

# ファイルを読み込んで処理
try:
    logger.info(f"{js_filename} の読み込みを開始")
    with open(js_filename, 'r', encoding='utf-8') as file:
        js_content = file.read()
    logger.success(f"{js_filename} の読み込みが完了しました")
    
    markdown_content = parse_js_to_markdown(js_content)
    
    # 結果をファイルに保存
    output_filename = "tweets_markdown.md"
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    logger.success(f"マークダウンファイルが {output_filename} として保存されました")

except FileNotFoundError:
    logger.error(f"エラー: {js_filename} が見つかりません")
except json.JSONDecodeError as e:
    logger.error(f"JSONの解析に失敗しました: {str(e)}")
except ValueError as e:
    logger.error(f"JSONの抽出に失敗しました: {str(e)}")
except Exception as e:
    logger.error(f"予期せぬエラーが発生しました: {str(e)}")

finally:
    logger.info("処理を終了します")
    print("詳細なログは debug.log ファイルを確認してください")

import pandas as pd
import folium


# 事故の種類（死者数や負傷者数）に基づいてポップアップの色を決定する関数を定義
def get_popup_color(row):
    # 死者数が1人以上の場合は赤色
    if row["死者数"] > 0:
        return "red"
    # 負傷者数が1人以上の場合は青色
    elif row["負傷者数"] > 0:
        return "blue"
    # それ以外の場合は緑色
    else:
        return "green"


# 交通事故データが含まれるCSVファイルを読み込む
file_path = "data/2023_traffic_accident_all.csv"
data = pd.read_csv(file_path)

# 事故の平均位置を中心とする地図を作成
map_center = [data["緯度"].mean(), data["経度"].mean()]
traffic_map = folium.Map(location=map_center, zoom_start=12)

# 各事故データに基づいてマーカーを追加
for index, row in data.iterrows():
    # ポップアップの色を事故の種類に基づいて設定
    color = get_popup_color(row)
    # ポップアップに表示するテキストを作成
    popup_text = (
        f"事故内容: {row['事故内容']}<br>"
        f"死者数: {row['死者数']}<br>"
        f"負傷者数: {row['負傷者数']}"
    )
    # マーカーを地図に追加し、ポップアップと色を設定
    folium.Marker(
        location=[row["緯度"], row["経度"]],
        popup=folium.Popup(popup_text, max_width=250),
        icon=folium.Icon(color=color),
    ).add_to(traffic_map)

# 完成した地図をHTMLファイルとして保存
map_file_path = "traffic_accident_map.html"
traffic_map.save(map_file_path)

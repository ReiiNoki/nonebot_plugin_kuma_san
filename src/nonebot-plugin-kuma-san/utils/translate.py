dict_jp_cn = {
    "わかばシューター": "新叶射击枪",
    "スプラシューター": "斯普拉射击枪",
    "N-ZAP85": "N-ZAP85",
    "シャープマーカー": "窄域标记枪",
    "ボールドマーカー": "广域标记枪",
    "プロモデラーMG": "专业模型枪MG",
    "プライムシューター": "顶尖射击枪",
    ".52ガロン": ".52加仑",
    ".96ガロン": ".96加仑",
    "ジェットスイーパー": "喷射清洁枪",
    "L3リールガン": "L3卷线枪",
    "H3リールガン": "H3卷线枪",
    "ボトルガイザー": "开瓶喷泉枪",
    "スプラローラー": "斯普拉滚筒",
    "ダイナモローラー": "电动马达滚筒",
    "ヴァリアブルローラー": "可变式滚筒",
    "カーボンローラー": "碳纤维滚筒",
    "スプラチャージャー": "斯普拉蓄力狙击枪",
    "スプラスコープ": "斯普拉准星枪",
    "スクイックリンα": "鱿快洁α",
    "14式竹筒銃・甲": "14式竹筒枪·甲",
    "ソイチューバー": "高压油管枪",
    "リッター4K": "公升4K",
    "4Kスコープ": "4K准星枪",
    "バケットスロッシャー": "飞溅泼桶",
    "ヒッセン": "洗笔筒",
    "スクリュースロッシャー": "回旋泼桶",
    "オーバーフロッシャー": "满溢泡澡泼桶",
    "エクスプロッシャー": "爆炸泼桶",
    "バレルスピナー": "桶装旋转枪",
    "スプラスピナー": "斯普拉旋转枪",
    "ハイドラント": "消防栓旋转枪",
    "クーゲルシュライバー": "圆珠笔",
    "ノーチラス47": "鹦鹉螺号47",
    "スプラマニューバー": "斯普拉机动枪",
    "デュアルスイーパー": "双重清洁枪",
    "クアッドホッパーブラック": "四重弹跳手枪 黑",
    "ケルビン525": "开尔文525",
    "スパッタリー": "溅镀枪",
    "パラシェルター": "遮阳防空伞",
    "キャンピングシェルター": "露营防空伞",
    "スパイガジェット": "特工配件",
    "ホットブラスター": "火热爆破枪",
    "ロングブラスター": "远距离爆破枪",
    "ノヴァブラスター": "新星爆破枪",
    "クラッシュブラスター": "冲涂爆破枪",
    "ラピッドブラスター": "快速爆破枪",
    "Rブラスターエリート": "快速爆破枪 精英",
    "パブロ": "巴勃罗",
    "ホクサイ": "北斋",
    "トライストリンガー": "三发猎鱼弓",
    "LACT-450": "LACT-450",
    "ライブワイパー": "雨刷刮水刀",
    "ドライブワイパー": "工作刮水刀",
    "プロモデラーRG": "专业模型枪RG",
    "バケットスロッシャーデコ": "飞溅泼桶 装饰",
    "パブロ・ヒュー": "巴勃罗・新艺术",
    "スパッタリー・ヒュー": "溅镀枪・新艺术",
    "プライムシューターコラボ": "顶尖射击枪 联名",
    "ノヴァブラスターネオ": "新星爆破枪 新型",
    "もみじシューター": "枫叶射击枪",
    "カーボンローラーデコ": "碳纤维滚筒 装饰",
    "スプラシューターコラボ": "斯普拉射击枪 联名",
    "スペースシューター": "太空射击枪",
    "スプラスピナーコラボ": "斯普拉旋转枪 联名",
    "R-PEN/5H": "R-PEN/5H",
    "ワイドローラー": "宽滚筒",
    "ランダム": "随机",
    "海女美術大学": "海女美术大学",
    "チョウザメ造船": "鲟鱼造船厂",
    "ザトウマーケット": "座头购物中心",
    "スメーシーワールド": "醋饭海洋世界",
    "マサバ海峡大橋": "真鲭跨海大桥",
    "キンメダイ美術館": "金眼鲷美术馆",
    "マヒマヒリゾート＆スパ": "鬼头刀SPA度假区",
    "ユノハナ大渓谷": "温泉花大峡谷",
    "ゴンズイ地区": "鳗鲶区",
    "ヤガラ市場": "烟管鱼市场",
    "マテガイ放水路": "竹蛏疏洪道",
    "ナメロウ金属": "鱼肉碎金属",
    "クサヤ温泉": "臭鱼干温泉",
    "ヒラメが丘団地": "比目鱼住宅区",
    "難破船ドン・ブラコ": "漂浮落难船",
    "ムニ・エール海洋発電所": "麦年海洋发电所",
    "シェケナダム": "鲑坝",
    "アラマキ砦": "新卷堡"
}


def translate(text) -> str:
    value = dict_jp_cn.get(text)
    return value


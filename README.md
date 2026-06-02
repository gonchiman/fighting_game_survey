# fighting_game_survey

Steam Charts の月別データを使って、対戦格闘ゲームのプレイヤー人口を分析するための Python プロジェクトです。

最初の分析対象は **Street Fighter 6** です。

## 目的

主目的は、Street Fighter 6 の Steam 上の月間平均プレイヤー数を取得し、次の観点で分析することです。

1. 月別の `Avg. Players` の推移を見る
2. `Avg. Players` から月間推定プレイ時間を計算する
3. 月間推定プレイ時間の累積グラフを作成する
4. アップデート、大会、セール、新キャラクター追加などのイベントとプレイヤー人口の変化を比較する

発展課題として、主要格闘ゲーム複数タイトルの `Avg. Players` の総和を分析できる構成にします。

## ディレクトリ構成

```text
fighting_game_survey/
├── data/
│   ├── events/          # 手入力するイベント表
│   ├── processed/       # 加工済みCSV
│   └── raw/             # 必要なら取得元データを保存
├── plots/               # 生成したグラフ画像
├── scripts/
│   └── analyze_sf6.py   # SF6分析の実行スクリプト
├── src/
│   └── fighting_game_survey/
│       ├── analysis.py
│       ├── constants.py
│       ├── date_utils.py
│       ├── events.py
│       ├── plots.py
│       └── steam_charts_client.py
├── pyproject.toml
└── requirements.txt
```

## セットアップ

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pip install -e .
```

## SF6 の分析を実行する

```bash
python scripts/analyze_sf6.py
```

実行すると、次のファイルを生成します。

```text
data/processed/street_fighter_6_monthly.csv
plots/street_fighter_6_avg_players.png
plots/street_fighter_6_cumulative_estimated_play_hours.png
plots/street_fighter_6_cumulative_avg_players.png
```

## イベント表について

`data/events/street_fighter_6_events.csv` にイベントを追加すると、グラフ上に縦線として表示できます。

形式は次の通りです。

```csv
date,event,category,note
2024-05-22,Example event,update,Replace this row with a confirmed SF6 event
```

レポートで使う場合は、イベント情報の出典も別途記録してください。

## 分析上の注意

`Avg. Players` は平均同時接続プレイヤー数です。ユニークユーザー数ではありません。

また、`Avg. Players` をそのまま累積した値は直感的な意味が弱いため、レポート本体では次の指標を主に使う方針です。

```text
月間推定プレイ時間 = Avg. Players × その月の時間数
累積推定プレイ時間 = 月間推定プレイ時間の累積
```

ただし、課題で「累積グラフ」が求められているため、補助的に `Avg. Players` の累積グラフも出力します。

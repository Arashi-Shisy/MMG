# MMGとは
## 開発の目的
* 能力開発部のキャリアクエスト求人には必須項目として開発経験が存在する。
* 実務での開発経験がないため、年数でのアピールが不可能
* 要求定義工程からテストまでの開発プロジェクト工程を一人で実施し、現状の知識レベルの証跡としたい

## 構成
* documentsディレクトリ
    * 要求定義から詳細設計までの、上流工程での成果物を格納
* systemsディレクトリ
    * 開発したアプリケーションを格納
    * 内部のディレクトリ構成は/documents/01_要求用件定義/03_ソフトウェア_ミドルウェア構成図.png参照
* testsディレクトリ
    * 自動テストのテストコードと、手動テストの項目書及び結果エビデンスを格納

## 0418時点未達成項目
* 会員登録メールやアラートバッチなど、メール関連の機能の実装
    * メールサーバがないので、どこまで実装するか要検討
* 目標一覧画面を未実装
    * トップページで代用可能なため今は未実装
* ミドルウェア構築
    * 近日着手予定
* いくつか抜けている要求/要件あり
    * 求人が埋まってしまう可能性を考慮して、デッドラインを定義してそちらを優先した
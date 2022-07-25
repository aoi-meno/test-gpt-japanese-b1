# test-gpt-japanese-b1
日本語のGPTモデルテスト

モデルは以下を使用
https://huggingface.co/rinna/japanese-gpt-1b

使用する際は、上記で配布されているファイル群をmodelフォルダに入れてください。
他のモデルでも可能です。

install require:
torch,transformer,sentencepiece

/参考文献

https://www.ogis-ri.co.jp/otc/hiroba/technical/similar-document-search/part14.html
https://zenn.dev/tyaahan/articles/a8d99900000002

# テスト内容
1.質問BOT

・質問例

入力：『五等分の花嫁』の中野四葉とは、

出力：『五等分の花嫁』の中野四葉とは、腐れ縁の幼馴染みの関係であり、お互いに「よっちゃん」と呼び合っている。恋愛面でのプライドが高く思い込みの激しい毒舌家で、実乃梨とは喧嘩で何度も別れそうになっている。恋愛至上主義の彼女は、一見するとツンデレのようにも見える。容姿端麗で金遣いが荒く、「彼氏に貢ぐ」が信条。また、お金があるに越したことはないと考えている。料理も得意だが、腐りかけの肉などは絶対に食べようとはしない。作中では数少ない彼女の所有物も、中身がヨダレだと知りながら食べてしまったり、ヤフオクで手に入れたりしている。また、テレビゲームに関しては、かなり病的で、購入したゲームソフトを3回も続けて破壊してしまったり、使い終わったまま使わずに放置しているコントローラーを、再利用できないものかとオークションに出品してしまったりもしている。アニメ版の登場人物の六夏とは犬猿の仲。




2.GPTで出力するAIの独り言

![スクリーンショット 2022-07-25 21 01 16](https://user-images.githubusercontent.com/35251392/180779253-fc3fd9bf-03b3-4124-8fe2-f2dcd86e7e3b.png)

![スクリーンショット 2022-07-25 21 04 56](https://user-images.githubusercontent.com/35251392/180779283-4d99debb-32a1-452b-a213-ac674d76275c.png)

import torch
from transformers import T5Tokenizer, AutoModelForCausalLM

tokenizer = T5Tokenizer.from_pretrained("./model/japanese-gpt-1b")
model = AutoModelForCausalLM.from_pretrained("./model/japanese-gpt-1b")

print(torch.cuda.is_available())

if torch.cuda.is_available():
    model = model.to("cuda")

print("Successfully Loading!")

#@markdown ## 独り言回数
round_trip = 20 #@param {type:"slider", min:0, max:100, step:1}
#@markdown ## 独り言回数
round_trip = 20 #@param {type:"slider", min:0, max:100, step:1}
 
#@markdown ## 独り言のトピック/
topic = "面白いこと" #@param {type:"string"}
text = "ララちゃん:「いぇいっ！おはようございますなの！私」ララちゃん:「今日は" + topic + "について話すなの！」ララちゃん:「"
 
#@markdown ### parameter変更(Option)
#@markdown 次のトークン確率をモジュール化するために使用される値
temperature = 1 #@param {type:"slider", min:0.0, max:1.0, step:0.1}
#@markdown 繰り返しペナルティのパラメータ。1.0はペナルティなし
repetition_penalty = 1 #@param {type:"slider", min:0.0, max:1.0, step:0.1}
#@markdown 長さに対する指数関数的なペナルティ。1.0はペナルティなし
length_penalty = 1 #@param {type:"slider", min:0.0, max:1.0, step:0.1}

print("ララちゃんの独り言。\n話題:", topic)
 
pos = 3 # 括弧の取得位置
for round_num in range(round_trip):
  token_ids = tokenizer.encode(text, add_special_tokens=False, return_tensors="pt")
  max_length = 100
  if max_length < len(text):
    max_length = len(text) + 30
 
  # ララちゃんのテキスト生成
  with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        max_length=max_length,
        max_time=20,
        min_length=30,
        do_sample=True,
        top_k=320,
        top_p=0.95,
        pad_token_id=tokenizer.pad_token_id,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        bad_word_ids=[[tokenizer.unk_token_id]],
        temperature = temperature,
        repetition_penalty = repetition_penalty,
        length_penalty = length_penalty,
        no_repeat_ngram_size=1,
        use_cache=True
        )
  output = tokenizer.decode(output_ids.tolist()[0])
  # 半角を全角に正規化
  output = output.translate(str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))
 
  # ララちゃんの先頭の独り言のみ取得
  prefix = "ララちゃん:「"
  suffix = "」"
  pre = output.split(prefix)
  post = pre[pos].split(suffix)
 
  # 」で閉じずにララちゃんが次の独り言を続けた場合に対処
  if "ララちゃん:" in post[0]:
    post[0] = post[0].split("ララちゃん:")[0]
  # 」で閉じずに終了した場合
  if "</s>" in post[0]:
    post[0] = post[0].replace("</s>", "")
 
  print("ララちゃん「", post[0], "」")
  
  # textに付加
  text += post[0] + "ララちゃん:「"
 
  # 次回取得位置更新
  pos += 1
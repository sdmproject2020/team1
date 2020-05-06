## 提供している関数
### データ読み込み系（戻り値はpd.DataFrame）
#### read_recipe(n)
レシピデータを読み込む関数
columns = ['recipeID','UserID','recipe_name','details','servings','advice','upbringing','date']

#### read_report(n)
つくレポを読み込む関数
columns = ['recipeID','UserID','message','reply','date']

#### read_step(n)
作業工程を読み込む関数
columns = ['recipeID','step_number','note']

#### read_ingredient(n)
材料を読み込む関数
columns = ['recipeID','ingredient','size']

### データ整形（主にingredient関係で）

#### clean_ingredient(df)
大さじ、小さじをそれぞれ15g,5g、少々を0.5gとしてgに変換し、その後gの文字を取っ払ってgで表されている材料の行を返す
このときsizeの列が文字列ではなく数値になっているので注意

なお、ここから下の関数は全てclean_ingredient内でのみ用いられてるので、説明が雑になるので注意

#### z2h(df)
DataFrame内の全ての全角数字を半角数字に変換。

#### size2g(df)
大さじ、小さじの部分を15*,5*にして、半角と全角のg,ｇ、グラムを取っ払い"02"のようなものを整形

#### g2float(df)
DataFrameの中から"0.~~"、"200"のような物のみをとりだし、
15*1とかを計算して数値として返す

### 想定しているディレクトリ状態
sys.pathとかで絶対パスとか相対パスとかうんたらやるのはめんどくさかったので、作業しているノートブックと同じディレクトリに以下のようにおいてください

(ディレクトリ)<br>
|--<span style="color: red; ">example.ipynb</span>(作業してるノートブック) <br>
|--team1_module.py <br>
|--data(データを保管してるディレクトリ) <br>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--recipe(recipe1998.csvからrecipe2014.csvが入っている。他も同じ) <br>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--report <br>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--step <br>
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--ingredient <br>

### jupyternotebookでの使い方
```python
import team1_module as t1 
df = t1.read_ingredient(2014)
```
こんな感じで使ってください

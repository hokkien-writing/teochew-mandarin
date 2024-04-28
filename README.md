# 普通話切換到潮州話
## 目標

本倉庫旨在幫助在異鄉習慣於呾普通話而忘記掉怎呾潮州話其儂，重新切換到潮州話來，認識到母語表達其親切佮趣味。

## 運作

倉庫中有一個文件，名 `mandarin-teochow.txt`，其內容按下底格式追加：

```
{普通話} // {潮州話漢字} // {潮州話白話字} // {分類} // {分級} // {引用簡寫}
```

比如：

```
書蟲 // 册魚 // Chheh-hṳ̂ // 眾生 // L2 // 汕頭話讀本
```

隨後，運行 `generate_md.py` 程序，伊會照分類及字典順序輸出文檔，以供閱讀。

## 分級

爲便利閱讀佮學習，本倉庫按照詞語其常用程度，將詞語分爲三個等級：

* L0：非常常用；
* L1：一般常用；
* L2：毋常用。

應當注意，此三個等級其分別目前是相當粗糙佮主觀其，只能作爲學習參考。

## 分類

|        |      |      |      |      |      |      |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- |
| 代詞   | 關係 | 天地 | 飲食 | 建築 | 法律 | 熟語 |
| 動詞   | 交際 | 時日 | 眾生 | 物件 | 商業 |      |
| 形容詞 | 活動 | 人體 | 水產 | 交通 | 宗教 |      |
| 副詞   |      | 打扮 | 蔬菓 |      |      |      |
| 數字   |      | 醫療 | 植物 |      |      |      |

## 引用

| 引用                                                         | 簡寫           |
| ------------------------------------------------------------ | -------------- |
| 明朝嘉靖丙寅年（四十五年、1566）刊本《重刊五色潮泉插科增入詩詞北曲勾欄荔鏡記戲文全集》 | 荔鏡記         |
| 明末,《重補摘錦潮調金花女一卷明末刊本-卷一》                 | 蘇六娘         |
| 1841, William Dean([美]璘为仁, 憐為仁).《First Lessons in the Tie-chiw Dialect(潮州話初級教程)》 | 潮州話初級教程 |
| 1883, Adele Marion Fielde([美]A.M.菲爾德, 斐姑娘).《A pronouncing and defining dictionary of the Swatow dialect, arranged according to syllables and tones(汕頭方言音義字典)》 | 斐姑娘字典     |
| 1883, Josiah Goddard([美]高德, 哥達德).《A Chinese and English vocabulary, in the Tie-chiu dialect(漢英潮州方言字典) | 高德字典       |
| 1883, Rudolf Lechler([德]黎力基), Samuel Wells Williams([美]衛三畏), William Duffus([英]卓威廉).《English-Chinese Vocabulary of the Vernacular Or Spoken Language of Swatow(英漢汕頭方言口語詞典)》 | 卓威廉詞典     |
| 1886, Lim Hiong Seng([新加坡]林雄成).《Handbook of the Swatow Vernacular(汕頭話讀本)》 | 汕頭話讀本     |
| 1992, 李新魁, 林伦伦.《潮汕方言词考释》                      | 考释           |
| 1993, 林伦伦.《潮汕方言熟语辞典》                            | 熟语辞典       |


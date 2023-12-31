# 猜數字遊戲🎮說明書
歡迎來到猜數字遊戲！這份說明將幫助你了解遊戲玩法以及程式如何運作。這個遊戲由以下步驟組成：

## 遊戲流程
* 隨機數字
  * 遊戲開始時，系統會隨機生成一個目標數字。
* 玩家猜測
  * 玩家將猜測一個數字並提交它。
* 系統反饋
  * 系統將提供反饋，告訴玩家猜測是太高、太低或正確。
* 持續猜測🤔
  * 玩家可以持續猜測直到猜對目標數字或達到猜測次數上限。
## 遊戲設定
* 遊戲的一些設定可以透過 XML 文件來調整。在 game_settings.xml 中，你可以找到以下設定：
```
<gameSettings>
    <x1>1</x1> <!-- 最小數字 -->
    <x2>100</x2> <!-- 最大數字 -->
    <n>10</n> <!-- 最大猜測次數 -->
</gameSettings>
```
* 以下是使用 Python 撰寫的程式碼：
```
import random
import xml.etree.ElementTree as ET

# 函數：從 XML 文件讀取遊戲設定
# ...

# 函數：開始遊戲
# ...

# 主函數
# ...

# 程式入口點
# ...
```
## 如何遊玩
* 確保已設定適當的遊戲設定在 game_settings.xml 中。
* 執行 Python 程式。
* 根據系統提示，輸入你的猜測。
* 根據系統反饋，調整猜測。
* 繼續猜測直到猜對或達到最大猜測次數。

## 簡易步驟
* 開啟程式。
* 輸入你的猜測。
* 根據系統提示進行下一步。
* 持續猜測直到猜中或猜測次數達上限。
  
## 總結
* 這便是猜數字遊戲的核心！享受遊戲並看看你能在多少次內猜中目標數字吧😝！
* 這份說明書將提供對遊戲和程式的概述，同時提供了遊戲玩法的簡易指南。希望這能幫助初學者更容易地了解和開始玩這個有趣的遊戲！



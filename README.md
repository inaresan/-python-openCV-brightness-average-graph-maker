# [python&openCV]brightness-average-graph-maker
##プログラムの概略：
openCVで映像を取り込み、フレームの総数を得る。各フレームの総数分画像をグレースケール化し
輝度の平均値（各画素の輝度の総和÷画像のサイズ）
を出力しながら行列に格納。最後に行列を用いてグラフを得る。

###使い方:
パスとファイル名を測定したいファイルに合わせ実行する。
１フレーム毎にかなり時間がかかるので、長いファイルについての実行は相応の時間待つ必要あり。
各フレームの平均輝度値が計算されるたびに出力され、最後にグラフが出力される。（キャプチャ参考）

####バージョン：
python:3.7.3
opencv-python:4.1.0.25
numpy:1.16.2
matplotlib:3.0.3

#####参考リンク:

[1]Toru Tamaki『2019imageprocessing』(最終閲覧日7/22)https://notebooks.azure.com/tamaki/projects/2019imageprocessing
pythonの使用方法、輝度の平均値の取り方について参考にしました。
[2] 電気情報CH 『【Python/OpenCV】動画ファイルの読み込み・再生』アルゴリズム雑記（最終閲覧日7/22）https://algorithm.joho.info/programming/python/opencv-videocapture-mp4-movie-py/#Python3OpenCV3
映像読み込み部分で参考にしました。
[3]ばこら～『【Python】初心者がよく出すエラーメッセージ』バコラー日記(最終閲覧日7/22)http://blog.bakorer.com/archives/50555189.html
途中でエラーが出たので参考にしました。

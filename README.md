# Easy OCR for Korean Language

### Sample Run (Eng)

```shell
# run with images/R-540832-1331752044.jpeg.jpg
python detect.py
```

```
Using CPU. Note: This module is much faster with a GPU.
[([[54, 40], [534, 40], [534, 72], [54, 72]], 'WHO WANTS TO LIVE FOREVER', 0.10928599536418915), ([[210, 332], [384, 332], [384, 382], [210, 382]], 'QUEEN', 0.5790598392486572), ([[86, 460], [498, 460], [498, 492], [86, 492]], 'FRIENDS WILL BE FRIENDS', 0.31486403942108154)]
```



### Sample Run (Kor)

```shell
# run with images/YBIGTA.jpg
python detect.py
```

```
Using CPU. Note: This module is much faster with a GPU.
[([[55, 47], [479, 47], [479, 83], [55, 83]], '사이언스팀에서는어떤공부를 하나요?', 0.25651898980140686), ([[237, 135], [302, 135], [302, 160], [237, 160]], 'Science', 0.9743586778640747), ([[372, 135], [433, 135], [433, 163], [372, 163]], 'Design', 0.7959674596786499), ([[84, 136], [180, 136], [180, 162], [84, 162]], 'Engineering', 0.4326842427253723), ([[443, 263], [469, 263], [469, 283], [443, 283]], '될용', 0.5922150611877441), ([[159, 265], [189, 265], [189, 283], [159, 283]], '저잠', 0.814736545085907), ([[347, 265], [387, 265], [387, 283], [347, 283]], '시각화', 0.9782570004463196), ([[78, 329], [466, 329], [466, 362], [78, 362]], '사이언스팀은(통계적 머신러닝)과 (딥러닝)을', 0.23461131751537323), ([[156, 356], [380, 356], [380, 382], [156, 382]], '위주로 공부하고 있습니다.', 0.5316558480262756), ([[86, 380], [452, 380], [452, 406], [86, 406]], '단순히 코드를 실행하는 것에 머무르지 않고', 0.23412665724754333), ([[82, 404], [454, 404], [454, 432], [82, 432]], '이론적배경을 이해하는 것을 목표로 합니다.', 0.4896583557128906), ([[118, 428], [418, 428], [418, 456], [118, 456]], '사이언스팀은 프로젝트를 진행할 때', 0.44189533591270447), ([[74, 452], [464, 452], [464, 480], [74, 480]], '해당 데이터에 가장 적합하고 효율적인 방법을', 0.4386041462421417), ([[142, 474], [394, 474], [394, 502], [142, 502]], '찾기 위해 공부하고 있습니다.', 0.6089983582496643)]
```



### Source
* [Github](https://github.com/JaidedAI/EasyOCR)
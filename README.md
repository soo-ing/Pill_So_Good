# 프로젝트 설명

시각장애인들을 위한 약 구별 시스템

# 기술 스택

# 상세 기술

- Raspberry Pi의 PIR 센서를 통해 알약의 존재를 인식하고 카메라센서를 통해 알약의 사진을 촬영하여 가져옵니다.
- 다음, 서버로 알약의 사진을 가져와 Tesseract OCR을 이용하여 전처리 과정을 진행하여 알약의 텍스트, 색깔 데이터를 구분합니다.
- 이 데이터를 Pill.csv 파일에 저장한 후 pill_list.csv 파일에 있는 알약들과 데이터를 비교하여 알약의 정보를 가져옵니다.
- 가져온 알약의 정보를 이용하여 스피커로 음성을 출력합니다.

# 작품 사진

![image](https://user-images.githubusercontent.com/84956281/141678757-c130ee77-a5aa-441c-ad45-e83d16103a4b.png)

# 알약 전처리

![image](https://user-images.githubusercontent.com/84956281/141678771-ac38a3dc-ea3c-44f2-a308-9ad3b880e33f.png)

# 시스템 구성도

![image](https://user-images.githubusercontent.com/84956281/141678778-9e5ec9d7-1166-4d6f-aa55-f4dd2bc25df5.png)

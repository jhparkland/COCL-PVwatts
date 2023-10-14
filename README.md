# COCL-PVwatts
- 본 프로젝트는 Custom pvwattas API based on NREL PVwatts 기반으로 캠퍼스 내 건물별 옥상에서 생산되는 전력량과 탄소감축량을 측정해서 캠퍼스 Net-Zero화에 필요한 정밀하게 측정하고 분석합니다.
<br><br>

## 프로젝트 목표
1. NREL PVwatts API의 데이터 명세를 분석 (https://developer.nrel.gov/docs/solar/pvwatts/v6/), https://www.haezoom.io/api/를 이용한 시간당 분석도 가능 (다만 베타테스팅)
2. 동아대학교 건물별 옥상에 태양광 설치시 생산되는 전력량을 1년, 월별, 24시간 기준으로 나누어 캠퍼스 내에서 생산할 수 있는 전력 생산량과 탄소 감축량 측정.
   
![지도](https://github.com/Prcnsi/COCL-PVwatts/assets/86015194/78313268-fa57-4da1-8010-72e1eed8204f)
<br><br><br>

## NREL PVWatts
- National Renewable Energy Laboratory(NREL) 미국 국립 재생에너지 연구소는 대표적인 재생에너지 연구소 중 하나로 NREL은 청정 에너지 전환을 선도하기 위해 인류가 직면한 세 가지 주요 위협 기후 변화, 오염, 생물 다양성 손실을 해결하기 위해 연구하고 있는 연구소이다. 
- NREL PVWatts®R 계산기는 NREL에서 개발한 서비스로 태양광에서 생산되는 전력을 예측하는 모델이다. 이는 위도, 경도, 면적, 방위각을 입력으로 받아서 해당 위치의 태양광 발전 시스템에서 태양광 발전량(일사량, 전력량)을 추정해주는 도구이다. 이는 일반적인 날씨에서 1년 동안 작동하는 유사한 실제 시스템에 대한 추정치이다.
- NREL PVWatt는 월별 태양광발전을 제시하기 때문에, 30일 기준, 24시간으로 나누어서 시간단위로 균등하게 접근하는 가정을 필요함. 여기에 시간별(밤/낮), 계절별 가중치(여름/가을)의 가중치 설계를 통해서 일단위의 태양광 발전량 일반화시킬 수 있음.
![NREL_homepage](https://github.com/Prcnsi/COCL-PVwatts/assets/86015194/ede9a42f-8d13-4434-9b42-ef00c343dd2c)
<br><br><br>

## NREL PVWatts API 

- NREL PVWatts 계산기는 실제 성능과 일치하도록 예측 알고리즘을 업데이트해서 일반적인 태양광 예측 시스템보다 정확하게 예측하도록 에너지 예측 알고리즘을 업데이트해 일반적인 시스템보다 정확하게 모델링되도록 설계됨.
- NREL PVWatts API에서 제공하는 기능은 크게 태양일사량 예측과, 전력 생산 예측 기능을 제공한다.
- 태양일사량 예측에서는 고정 1축 또는 2축에 대한 입사각(AOI) 계산을 수행한다. 그리고 주어진 입사각에 대한 표준 기하학적 계산을 통해 실시간 시간별 태양열을 추적해서 계산한다.
- 전력 생산 예측에서 PVWatts 모듈은 지정된 명판 DC가 있는 DC 전력을 계산하여 시스템 사양 및 시간당 복사조도를 기반으로 시간당 전력 출력량을 계산한다.<br>
![NREL_PVWawtts](https://github.com/Prcnsi/COCL-PVwatts/assets/86015194/1360c104-6424-4fcb-9b7e-da7bc5938ce6)

<br><br>

## 참여 신청 방법
1. issues 탭 클릭
2. new issues 클릭 후 가입신청 템플릿 선택
3. 양식에 맞춰 작성

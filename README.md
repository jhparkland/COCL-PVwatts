# COCL-PVwatts
Custom pvwattas API based on NREL PVwatts

## NREL PVWatts
- National Renewable Energy Laboratory(NREL) 미국 국립 재생에너지 연구소는 대표적인 재생에너지 연구소 중 하나로 해당 연구소는 청정 에너지 연구, 개발 및 배포 분야에서 수십 년 동안 집중적으로 연구하는 기관으로 NREL은 청적 에너지 전환을 선도하기 위해 인류가 직면한 세 가지 주요 위협 기후 변화, 오염, 생물 다양성 손실을 해결하기 위해 연구하고 있는 연구소이다. 
- NREL PVWawtts Calculator는 

![NREL_홈페이지](https://github.com/Prcnsi/COCL-PVwatts/assets/86015194/ede9a42f-8d13-4434-9b42-ef00c343dd2c)

## 추가설명
NREL PVWatt는 월별 태양광발전을 제시하기 때문에, 30일 기준, 24시간으로 나누어서 시간단위로 균등하게 접근하는 가정을 필요함. 여기에 시간별(밤/낮), 계절별 가중치(여름/가을)의 가중치 설계를 통해서 일단위의 태양광 발전량 일반화시킬 수 있음.


## 프로젝트 목표
1. NREL PVwatts API의 데이터 명세를 분석 (https://developer.nrel.gov/docs/solar/pvwatts/v6/), https://www.haezoom.io/api/를 이용한 시간당 분석도 가능 (다만 베타테스팅)
2. 동아대학교 건물별 옥상에 태양광 설치시 생산되는 전력량을 1년, 월별, 24시간 기준으로 나누어 캠퍼스 내에서 생산할 수 있는 전력 생산량과 탄소 감축량 측정.
   
![지도](https://github.com/Prcnsi/COCL-PVwatts/assets/86015194/78313268-fa57-4da1-8010-72e1eed8204f)

## 참여 신청 방법

1. issues 탭 클릭
2. new issues 클릭 후 가입신청 템플릿 선택
3. 양식에 맞춰 작성

# COCL-PVwatts
Custom pvwattas API based on NREL PVwatts

## 프로젝트 목표
1. NREL PVwatts API의 데이터 명세를 분석 (https://developer.nrel.gov/docs/solar/pvwatts/v6/), https://www.haezoom.io/api/를 이용한 시간당 분석도 가능 (다만 베타테스팅)
2. 동아대학교 중심으로 태양광 발전량 측정

## 추가설명
NREL PVWatt는 월별 태양광발전을 제시하기 때문에, 30일 기준, 24시간으로 나누어서 시간단위로 균등하게 접근하는 가정을 필요함. 여기에 시간별(밤/낮), 계절별 가중치(여름/가을)의 가중치 설계를 통해서 일단위의 태양광 발전량 일반화시킬 수 있음.


## 참여 신청 방법

1. issues 탭 클릭
2. new issues 클릭 후 가입신청 템플릿 선택
3. 양식에 맞춰 작성

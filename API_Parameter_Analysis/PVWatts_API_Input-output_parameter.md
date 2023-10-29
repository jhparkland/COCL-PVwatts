# NREL API Input-output Parameter
- NREL은 미국 국립 재생 에너지 연구소로 NREL API는 이 연구소에서 태양광 일사량 분석 API이다. 이 API에서 요청하고 응답하는 파라미터 정보는 아래와 같다.
- NREL API의 주요 입출력 파라미터는 다음과 같다. 더 자세한 정보가 궁금하다면 아래 링크를 참고 바란다.
[Link] https://developer.nrel.gov/docs/solar/pvwatts/v6/
<br/>

## Input Parameter
| 파라미터명        | 뜻                 |
| ----------------- | ------------------ |
| array_type       | 태양광 패널 배열 종류 |
| tilt             | 기울어진 정도        |
| azimuth          | 방위각              |
| address          | 주소                |
| latitude         | 위도                |
| longitude        | 경도                |
| radius           | 반지름              |

<br/>

## Output Parameter
| 파라미터(Parameter)| 의미               | 단위                     |
| ----------------- | ------------------- | ------------------------- |
| poa_monthly     | 1-12월까지(월간) 조도값 |kWh/m2 |
| dc_monthly     | 1-12월까지(월간) DC량  | kWhdc|
| ac_monthly      | 1-12월까지(월간) AC량 | kWhac |
| ac_annual       | 년도별 AC 값        | kWhac   |
| solrad_monthly  | 1-12월별 일사량 값    |kWh/m2/day   |
| solrad_annual   | 연간 태양 복사값     | kWh/m2/day      |
| capacity_factor     | 시스템이 운영 첫해에 예상되는 전기 출력 대 명판 출력의 비율  | AC-to-DC   |

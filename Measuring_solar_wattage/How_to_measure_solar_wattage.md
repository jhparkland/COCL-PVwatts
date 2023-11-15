# 태양광 전력량 측정 방법 
- 태양광에서 생산되는 전력량을 측정하기 위해 NREL PVWatts에서 제공하는 PVWatts® Calculator를 이용합니다.
- PVWatts® Calculator는 NREL PVWatts API를 바탕으로 태양광에서 생산되는 전력을 예측하는 모델입니다. (https://pvwatts.nrel.gov/index.php)


##
1. 태양광 전력량을 측정하고 싶은 장소의 주소를 입력합니다.
![주소입력](https://github.com/jhparkland/COCL-PVwatts/assets/88486391/8814b41f-f7fa-4b96-9b97-4053aac304eb)

3. 입력한 주소를 기반으로 현재 위치(위도, 경도)와 함께 그리드 셀을 통해 지역이 지정됩니다. 만약 잘못된 위치에 지정된 경우 수정할 수 있습니다.
![위치지정](https://github.com/jhparkland/COCL-PVwatts/assets/88486391/94a22111-3d07-43ee-81a3-5d8f9a29420c)

4. 파라미터(DC System Size, Module Type, System Loss, etc.)를 조정합니다.
![파라미터 조정](https://github.com/jhparkland/COCL-PVwatts/assets/88486391/20d4b4a9-f6b7-4d14-bf24-813d83ecb83c)

- Rooptop Size Estimator 기능을 통해 그리드 셀을 지붕 면적 크기만큼 지정할 수 있습니다.
![그리드 셀 지정](https://github.com/jhparkland/COCL-PVwatts/assets/88486391/cd7060e4-391c-428c-bca5-4e0973aa771e)

4. 모든 작업이 끝나면 결과값(예측된 태양광 전력량)이 출력됩니다.
![결과](https://github.com/jhparkland/COCL-PVwatts/assets/88486391/607a0e71-194c-46f2-9afd-70e98ff73493)

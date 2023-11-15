class CallbackManager:
  # 위치 및 위도, 경도 데이터
  def location(self):
        data = db.child("information").get().val()
        if data:
            entry = data[0]  # Assuming there is only one entry in the "information" array
            return {
                "Requested Location": entry.get("Requested Location"),
                "Latitude (DD)": entry.get("Latitude (DD)"),
                "Longitude (DD)": entry.get("Longitude (DD)")
            }
          
  # 태양광 전력량 데이터 (1시간 단위)
  def get_dc_output_data(self, target_month, target_day):
      data = db.child("pvwatts").get().val()
      if data:
          dc_output_data = []
          for entry in data:
              if entry.get("Month") == target_month and entry.get("Day") == target_day:
                  dc_output_data.append(entry.get("DC Array Output (W)", 0))
          return dc_output_data
      else:
          return None

import pandas as pd
import matplotlib.pyplot as plt

# 1. 读取死亡谷（Death Valley）数据
death_valley_file = 'death_valley_2021_simple.csv'  # 死亡谷文件路径
death_valley_df = pd.read_csv(death_valley_file)

# 将 'DATE' 列转换为 datetime 格式
death_valley_df['DATE'] = pd.to_datetime(death_valley_df['DATE'])

# 2. 绘制死亡谷的温度折线图
plt.figure(figsize=(12, 6))

# 绘制最高温度 (TMAX)
plt.plot(death_valley_df['DATE'], death_valley_df['TMAX'], label='Max Temperature (TMAX)', color='r', marker='o', linestyle='-', linewidth=2)

# 绘制最低温度 (TMIN)
plt.plot(death_valley_df['DATE'], death_valley_df['TMIN'], label='Min Temperature (TMIN)', color='b', marker='x', linestyle='--', linewidth=2)

# 绘制观测温度 (TOBS)
plt.plot(death_valley_df['DATE'], death_valley_df['TOBS'], label='Observed Temperature (TOBS)', color='g', marker='s', linestyle=':', linewidth=2)

# 设置图表标题和标签
plt.title('Temperature Trends in Death Valley (2021)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)

# 设置日期格式和旋转角度
plt.xticks(rotation=45, ha='right')

# 显示图例
plt.legend()

# 显示网格线
plt.grid(True)

# 调整布局，使日期标签不重叠
plt.tight_layout()

# 显示图表
plt.show()


# 3. 读取Sitka天气数据
sitka_file = 'sitka_weather_2021_simple.csv'  # Sitka文件路径
sitka_df = pd.read_csv(sitka_file)

# 将 'DATE' 列转换为 datetime 格式
sitka_df['DATE'] = pd.to_datetime(sitka_df['DATE'])

# 4. 绘制Sitka的温度折线图
plt.figure(figsize=(12, 6))

# 绘制最高温度 (TMAX) 的折线图
plt.plot(sitka_df['DATE'], sitka_df['TMAX'], label='Max Temperature (TMAX)', color='orange', marker='o', linestyle='-', linewidth=2)

# 绘制最低温度 (TMIN) 的折线图
plt.plot(sitka_df['DATE'], sitka_df['TMIN'], label='Min Temperature (TMIN)', color='blue', marker='x', linestyle='--', linewidth=2)

# 设置图表标题和标签
plt.title('Temperature Trends in Sitka (2021)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)

# 设置日期格式和旋转角度
plt.xticks(rotation=45, ha='right')

# 显示图例
plt.legend()

# 显示网格线
plt.grid(True)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()

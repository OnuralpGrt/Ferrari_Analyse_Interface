import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Türkçe karakter desteği için
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# Veri setlerini yükle
print("Veri setleri yükleniyor...")
constructors = pd.read_csv('constructors.csv')
drivers = pd.read_csv('drivers.csv')
races = pd.read_csv('races.csv')
results = pd.read_csv('results.csv')
constructor_standings = pd.read_csv('constructor_standings.csv')
driver_standings = pd.read_csv('driver_standings.csv')
qualifying = pd.read_csv('qualifying.csv')
pit_stops = pd.read_csv('pit_stops.csv')
lap_times = pd.read_csv('lap_times.csv')
circuits = pd.read_csv('circuits.csv')

# Ferrari constructor ID'si
FERRARI_ID = 6

print("Ferrari analizi başlıyor...")

# Ferrari sonuçlarını yıl ve pist bilgisiyle birleştir
ferrari_results = results[results['constructorId'] == FERRARI_ID].copy()
ferrari_results = ferrari_results.merge(races[['raceId', 'year', 'name', 'date', 'circuitId']], on='raceId')
ferrari_results = ferrari_results.merge(drivers[['driverId', 'forename', 'surname']], on='driverId')
ferrari_results['driver_name'] = ferrari_results['forename'] + ' ' + ferrari_results['surname']
ferrari_results = ferrari_results.merge(circuits[['circuitId', 'name', 'country']], on='circuitId', suffixes=('', '_circuit'))
ferrari_results['position_numeric'] = pd.to_numeric(ferrari_results['position'], errors='coerce')

# 1. Yıllara Göre Ferrari Başarıları
print("\n1. Yıllara Göre Ferrari Başarıları")
yearly = ferrari_results.groupby('year').agg({
    'raceId': 'nunique',
    'points': 'sum',
    'position': lambda x: (x == '1').sum(),
    'position_numeric': lambda x: (x <= 3).sum()
}).rename(columns={'raceId': 'Yarış', 'points': 'Puan', 'position': 'Galibiyet'})
yearly['Podyum'] = yearly['position_numeric']
yearly['Ortalama_Pozisyon'] = ferrari_results.groupby('year')['position_numeric'].mean()
yearly = yearly.drop('position_numeric', axis=1)
yearly.to_csv('ferrari_yillik_ozet.csv')
plt.figure(figsize=(10,6))
yearly['Galibiyet'].plot(kind='bar', color='red', alpha=0.7)
plt.title('Ferrari: Yıllara Göre Kazanılan Yarış Sayısı')
plt.xlabel('Yıl')
plt.ylabel('Galibiyet')
plt.tight_layout()
plt.savefig('ferrari_yillik_galibiyet.png')
plt.close()

plt.figure(figsize=(10,6))
yearly['Puan'].plot(kind='line', color='darkred', marker='o')
plt.title('Ferrari: Yıllara Göre Toplam Puan')
plt.xlabel('Yıl')
plt.ylabel('Puan')
plt.tight_layout()
plt.savefig('ferrari_yillik_puan.png')
plt.close()

# 2. Pistlere Göre Ferrari Başarıları
print("\n2. Pistlere Göre Ferrari Başarıları")
circuit_stats = ferrari_results.groupby('name_circuit').agg({
    'raceId': 'nunique',
    'position': lambda x: (x == '1').sum(),
    'position_numeric': lambda x: (x <= 3).sum(),
    'points': 'sum'
}).rename(columns={'raceId': 'Yarış', 'position': 'Galibiyet', 'position_numeric': 'Podyum', 'points': 'Puan'})
circuit_stats['Ortalama_Pozisyon'] = ferrari_results.groupby('name_circuit')['position_numeric'].mean()
circuit_stats = circuit_stats.sort_values('Galibiyet', ascending=False)
circuit_stats.to_csv('ferrari_pist_ozet.csv')
plt.figure(figsize=(12,6))
circuit_stats['Galibiyet'].head(10).plot(kind='bar', color='crimson')
plt.title('Ferrari: En Çok Kazanılan 10 Pist')
plt.xlabel('Pist')
plt.ylabel('Galibiyet')
plt.tight_layout()
plt.savefig('ferrari_en_cok_kazanilan_pistler.png')
plt.close()

plt.figure(figsize=(12,6))
circuit_stats['Podyum'].head(10).plot(kind='bar', color='orange')
plt.title('Ferrari: En Çok Podyum Yapılan 10 Pist')
plt.xlabel('Pist')
plt.ylabel('Podyum')
plt.tight_layout()
plt.savefig('ferrari_en_cok_podyum_pistler.png')
plt.close()

# 3. Pilotlara Göre Ferrari Başarıları
print("\n3. Pilotlara Göre Ferrari Başarıları")
driver_stats = ferrari_results.groupby('driver_name').agg({
    'raceId': 'nunique',
    'position': lambda x: (x == '1').sum(),
    'position_numeric': lambda x: (x <= 3).sum(),
    'points': 'sum'
}).rename(columns={'raceId': 'Yarış', 'position': 'Galibiyet', 'position_numeric': 'Podyum', 'points': 'Puan'})
driver_stats['Ortalama_Pozisyon'] = ferrari_results.groupby('driver_name')['position_numeric'].mean()
driver_stats = driver_stats.sort_values('Puan', ascending=False)
driver_stats.to_csv('ferrari_pilot_ozet.csv')
plt.figure(figsize=(12,6))
driver_stats['Galibiyet'].head(10).plot(kind='bar', color='gold')
plt.title('Ferrari: En Çok Kazanan 10 Pilot')
plt.xlabel('Pilot')
plt.ylabel('Galibiyet')
plt.tight_layout()
plt.savefig('ferrari_en_cok_kazanan_pilotlar.png')
plt.close()

plt.figure(figsize=(12,6))
driver_stats['Podyum'].head(10).plot(kind='bar', color='red')
plt.title('Ferrari: En Çok Podyum Yapan 10 Pilot')
plt.xlabel('Pilot')
plt.ylabel('Podyum')
plt.tight_layout()
plt.savefig('ferrari_en_cok_podyum_pilotlar.png')
plt.close()

# 4. Sezon Bazında Ferrari Özet Tablosu
print("\n4. Sezon Bazında Ferrari Özet Tablosu")
season_summary = ferrari_results.groupby(['year', 'driver_name']).agg({
    'raceId': 'nunique',
    'points': 'sum',
    'position': lambda x: (x == '1').sum(),
    'position_numeric': lambda x: (x <= 3).sum()
}).rename(columns={'raceId': 'Yarış', 'points': 'Puan', 'position': 'Galibiyet', 'position_numeric': 'Podyum'})
season_summary.to_csv('ferrari_sezon_pilot_ozet.csv')

# 5. Ferrari'nin En Başarılı Sezonları Tablosu
print("\n5. Ferrari'nin En Başarılı Sezonları")
best_seasons = yearly.sort_values('Galibiyet', ascending=False).head(10)
best_seasons.to_csv('ferrari_en_basarili_sezonlar.csv')

# 6. Ferrari'nin En Başarılı Pilotları Tablosu
print("\n6. Ferrari'nin En Başarılı Pilotları")
best_drivers = driver_stats.head(10)
best_drivers.to_csv('ferrari_en_basarili_pilotlar.csv')

# 7. Ferrari'nin En Başarılı Pistleri Tablosu
print("\n7. Ferrari'nin En Başarılı Pistleri")
best_circuits = circuit_stats.head(10)
best_circuits.to_csv('ferrari_en_basarili_pistler.csv')

# 8. Ferrari'nin En Çok Puan Topladığı Sezonlar
print("\n8. Ferrari'nin En Çok Puan Topladığı Sezonlar")
highest_points_seasons = yearly.sort_values('Puan', ascending=False).head(10)
highest_points_seasons.to_csv('ferrari_en_cok_puan_sezonlar.csv')

# 9. Ferrari'nin En Çok Puan Topladığı Pilotlar
print("\n9. Ferrari'nin En Çok Puan Topladığı Pilotlar")
highest_points_drivers = driver_stats.sort_values('Puan', ascending=False).head(10)
highest_points_drivers.to_csv('ferrari_en_cok_puan_pilotlar.csv')

# 10. Ferrari'nin En Çok Puan Topladığı Pistler
print("\n10. Ferrari'nin En Çok Puan Topladığı Pistler")
highest_points_circuits = circuit_stats.sort_values('Puan', ascending=False).head(10)
highest_points_circuits.to_csv('ferrari_en_cok_puan_pistler.csv')

# 11. Ferrari'nin En İyi Ortalama Pozisyonu Olan Sezonlar
print("\n11. Ferrari'nin En İyi Ortalama Pozisyonu Olan Sezonlar")
best_avg_position_seasons = yearly.sort_values('Ortalama_Pozisyon').head(10)
best_avg_position_seasons.to_csv('ferrari_en_iyi_ortalama_pozisyon_sezonlar.csv')

# 12. Ferrari'nin En İyi Ortalama Pozisyonu Olan Pilotlar
print("\n12. Ferrari'nin En İyi Ortalama Pozisyonu Olan Pilotlar")
best_avg_position_drivers = driver_stats.sort_values('Ortalama_Pozisyon').head(10)
best_avg_position_drivers.to_csv('ferrari_en_iyi_ortalama_pozisyon_pilotlar.csv')

# 13. Ferrari'nin En İyi Ortalama Pozisyonu Olan Pistler
print("\n13. Ferrari'nin En İyi Ortalama Pozisyonu Olan Pistler")
best_avg_position_circuits = circuit_stats.sort_values('Ortalama_Pozisyon').head(10)
best_avg_position_circuits.to_csv('ferrari_en_iyi_ortalama_pozisyon_pistler.csv')

# 14. Ferrari'nin En Çok Podyum Yaptığı Sezonlar
print("\n14. Ferrari'nin En Çok Podyum Yaptığı Sezonlar")
most_podiums_seasons = yearly.sort_values('Podyum', ascending=False).head(10)
most_podiums_seasons.to_csv('ferrari_en_cok_podyum_sezonlar.csv')

# 15. Ferrari'nin En Çok Podyum Yaptığı Pilotlar
print("\n15. Ferrari'nin En Çok Podyum Yaptığı Pilotlar")
most_podiums_drivers = driver_stats.sort_values('Podyum', ascending=False).head(10)
most_podiums_drivers.to_csv('ferrari_en_cok_podyum_pilotlar.csv')

print("\nAnaliz tamamlandı! 15 farklı tablo ve grafikler ayrı dosyalara kaydedildi.")
print("\nOluşturulan Tablolar:")
print("1. ferrari_yillik_ozet.csv")
print("2. ferrari_pist_ozet.csv")
print("3. ferrari_pilot_ozet.csv")
print("4. ferrari_sezon_pilot_ozet.csv")
print("5. ferrari_en_basarili_sezonlar.csv")
print("6. ferrari_en_basarili_pilotlar.csv")
print("7. ferrari_en_basarili_pistler.csv")
print("8. ferrari_en_cok_puan_sezonlar.csv")
print("9. ferrari_en_cok_puan_pilotlar.csv")
print("10. ferrari_en_cok_puan_pistler.csv")
print("11. ferrari_en_iyi_ortalama_pozisyon_sezonlar.csv")
print("12. ferrari_en_iyi_ortalama_pozisyon_pilotlar.csv")
print("13. ferrari_en_iyi_ortalama_pozisyon_pistler.csv")
print("14. ferrari_en_cok_podyum_sezonlar.csv")
print("15. ferrari_en_cok_podyum_pilotlar.csv") 
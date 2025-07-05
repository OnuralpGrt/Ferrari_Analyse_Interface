import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Türkçe karakter desteği ve görsel ayarlar
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("Ferrari analiz tablolarını görselleştiriyorum...")

# 1. Yıllık Performans Analizi
print("\n1. Yıllık Performans Analizi")
yearly = pd.read_csv('ferrari_yillik_ozet.csv', index_col=0)

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Ferrari: Yıllık Performans Analizi', fontsize=16, fontweight='bold')

# Galibiyet sayısı
axes[0,0].bar(yearly.index, yearly['Galibiyet'], color='red', alpha=0.7)
axes[0,0].set_title('Yıllara Göre Galibiyet Sayısı')
axes[0,0].set_xlabel('Yıl')
axes[0,0].set_ylabel('Galibiyet')
axes[0,0].tick_params(axis='x', rotation=45)

# Toplam puan
axes[0,1].plot(yearly.index, yearly['Puan'], color='darkred', linewidth=2, marker='o')
axes[0,1].set_title('Yıllara Göre Toplam Puan')
axes[0,1].set_xlabel('Yıl')
axes[0,1].set_ylabel('Puan')
axes[0,1].tick_params(axis='x', rotation=45)

# Podyum sayısı
axes[1,0].bar(yearly.index, yearly['Podyum'], color='orange', alpha=0.7)
axes[1,0].set_title('Yıllara Göre Podyum Sayısı')
axes[1,0].set_xlabel('Yıl')
axes[1,0].set_ylabel('Podyum')
axes[1,0].tick_params(axis='x', rotation=45)

# Ortalama pozisyon
axes[1,1].plot(yearly.index, yearly['Ortalama_Pozisyon'], color='blue', linewidth=2, marker='s')
axes[1,1].set_title('Yıllara Göre Ortalama Pozisyon')
axes[1,1].set_xlabel('Yıl')
axes[1,1].set_ylabel('Ortalama Pozisyon')
axes[1,1].tick_params(axis='x', rotation=45)
axes[1,1].invert_yaxis()

plt.tight_layout()
plt.savefig('ferrari_yillik_performans_analizi.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Pistlere Göre Performans
print("\n2. Pistlere Göre Performans Analizi")
circuit_stats = pd.read_csv('ferrari_pist_ozet.csv', index_col=0)

fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Ferrari: Pistlere Göre Performans Analizi', fontsize=16, fontweight='bold')

# En çok galibiyet alınan pistler
top_circuits_wins = circuit_stats.nlargest(10, 'Galibiyet')
axes[0,0].barh(top_circuits_wins.index, top_circuits_wins['Galibiyet'], color='crimson')
axes[0,0].set_title('En Çok Galibiyet Alınan 10 Pist')
axes[0,0].set_xlabel('Galibiyet Sayısı')

# En çok puan toplanan pistler
top_circuits_points = circuit_stats.nlargest(10, 'Puan')
axes[0,1].barh(top_circuits_points.index, top_circuits_points['Puan'], color='gold')
axes[0,1].set_title('En Çok Puan Toplanan 10 Pist')
axes[0,1].set_xlabel('Toplam Puan')

# En çok podyum yapılan pistler
top_circuits_podiums = circuit_stats.nlargest(10, 'Podyum')
axes[1,0].barh(top_circuits_podiums.index, top_circuits_podiums['Podyum'], color='orange')
axes[1,0].set_title('En Çok Podyum Yapılan 10 Pist')
axes[1,0].set_xlabel('Podyum Sayısı')

# En iyi ortalama pozisyonu olan pistler
best_avg_circuits = circuit_stats.nsmallest(10, 'Ortalama_Pozisyon')
axes[1,1].barh(best_avg_circuits.index, best_avg_circuits['Ortalama_Pozisyon'], color='green')
axes[1,1].set_title('En İyi Ortalama Pozisyonu Olan 10 Pist')
axes[1,1].set_xlabel('Ortalama Pozisyon')

plt.tight_layout()
plt.savefig('ferrari_pist_performans_analizi.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Pilotlara Göre Performans
print("\n3. Pilotlara Göre Performans Analizi")
driver_stats = pd.read_csv('ferrari_pilot_ozet.csv', index_col=0)

fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Ferrari: Pilotlara Göre Performans Analizi', fontsize=16, fontweight='bold')

# En çok galibiyet alan pilotlar
top_drivers_wins = driver_stats.nlargest(10, 'Galibiyet')
axes[0,0].barh(top_drivers_wins.index, top_drivers_wins['Galibiyet'], color='gold')
axes[0,0].set_title('En Çok Galibiyet Alan 10 Pilot')
axes[0,0].set_xlabel('Galibiyet Sayısı')

# En çok puan toplayan pilotlar
top_drivers_points = driver_stats.nlargest(10, 'Puan')
axes[0,1].barh(top_drivers_points.index, top_drivers_points['Puan'], color='red')
axes[0,1].set_title('En Çok Puan Toplayan 10 Pilot')
axes[0,1].set_xlabel('Toplam Puan')

# En çok podyum yapan pilotlar
top_drivers_podiums = driver_stats.nlargest(10, 'Podyum')
axes[1,0].barh(top_drivers_podiums.index, top_drivers_podiums['Podyum'], color='orange')
axes[1,0].set_title('En Çok Podyum Yapan 10 Pilot')
axes[1,0].set_xlabel('Podyum Sayısı')

# En iyi ortalama pozisyonu olan pilotlar
best_avg_drivers = driver_stats.nsmallest(10, 'Ortalama_Pozisyon')
axes[1,1].barh(best_avg_drivers.index, best_avg_drivers['Ortalama_Pozisyon'], color='blue')
axes[1,1].set_title('En İyi Ortalama Pozisyonu Olan 10 Pilot')
axes[1,1].set_xlabel('Ortalama Pozisyon')

plt.tight_layout()
plt.savefig('ferrari_pilot_performans_analizi.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. En Başarılı Sezonlar
print("\n4. En Başarılı Sezonlar Analizi")
best_seasons = pd.read_csv('ferrari_en_basarili_sezonlar.csv', index_col=0)

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Ferrari: En Başarılı Sezonlar Analizi', fontsize=16, fontweight='bold')

# En çok galibiyet alan sezonlar
axes[0,0].bar(range(len(best_seasons)), best_seasons['Galibiyet'], color='red', alpha=0.7)
axes[0,0].set_title('En Çok Galibiyet Alan Sezonlar')
axes[0,0].set_xlabel('Sezon Sıralaması')
axes[0,0].set_ylabel('Galibiyet Sayısı')
axes[0,0].set_xticks(range(len(best_seasons)))
axes[0,0].set_xticklabels(best_seasons.index, rotation=45)

# En çok puan toplayan sezonlar
axes[0,1].bar(range(len(best_seasons)), best_seasons['Puan'], color='gold', alpha=0.7)
axes[0,1].set_title('En Çok Puan Toplayan Sezonlar')
axes[0,1].set_xlabel('Sezon Sıralaması')
axes[0,1].set_ylabel('Toplam Puan')
axes[0,1].set_xticks(range(len(best_seasons)))
axes[0,1].set_xticklabels(best_seasons.index, rotation=45)

# En çok podyum yapan sezonlar
axes[1,0].bar(range(len(best_seasons)), best_seasons['Podyum'], color='orange', alpha=0.7)
axes[1,0].set_title('En Çok Podyum Yapan Sezonlar')
axes[1,0].set_xlabel('Sezon Sıralaması')
axes[1,0].set_ylabel('Podyum Sayısı')
axes[1,0].set_xticks(range(len(best_seasons)))
axes[1,0].set_xticklabels(best_seasons.index, rotation=45)

# En iyi ortalama pozisyonu olan sezonlar
axes[1,1].bar(range(len(best_seasons)), best_seasons['Ortalama_Pozisyon'], color='blue', alpha=0.7)
axes[1,1].set_title('En İyi Ortalama Pozisyonu Olan Sezonlar')
axes[1,1].set_xlabel('Sezon Sıralaması')
axes[1,1].set_ylabel('Ortalama Pozisyon')
axes[1,1].set_xticks(range(len(best_seasons)))
axes[1,1].set_xticklabels(best_seasons.index, rotation=45)
axes[1,1].invert_yaxis()

plt.tight_layout()
plt.savefig('ferrari_en_basarili_sezonlar_analizi.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Karşılaştırmalı Analiz
print("\n5. Karşılaştırmalı Analiz")
fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Ferrari: Karşılaştırmalı Performans Analizi', fontsize=16, fontweight='bold')

# Galibiyet vs Puan (Sezonlar)
axes[0,0].scatter(yearly['Galibiyet'], yearly['Puan'], s=100, alpha=0.7, color='red')
axes[0,0].set_xlabel('Galibiyet Sayısı')
axes[0,0].set_ylabel('Toplam Puan')
axes[0,0].set_title('Galibiyet vs Puan (Sezonlar)')

# Podyum vs Galibiyet (Pilotlar)
axes[0,1].scatter(driver_stats['Podyum'], driver_stats['Galibiyet'], s=100, alpha=0.7, color='gold')
axes[0,1].set_xlabel('Podyum Sayısı')
axes[0,1].set_ylabel('Galibiyet Sayısı')
axes[0,1].set_title('Podyum vs Galibiyet (Pilotlar)')

# Ortalama Pozisyon vs Puan (Pistler)
axes[1,0].scatter(circuit_stats['Ortalama_Pozisyon'], circuit_stats['Puan'], s=100, alpha=0.7, color='blue')
axes[1,0].set_xlabel('Ortalama Pozisyon')
axes[1,0].set_ylabel('Toplam Puan')
axes[1,0].set_title('Ortalama Pozisyon vs Puan (Pistler)')
axes[1,0].invert_xaxis()

# Yarış Sayısı vs Galibiyet (Pilotlar)
axes[1,1].scatter(driver_stats['Yarış'], driver_stats['Galibiyet'], s=100, alpha=0.7, color='green')
axes[1,1].set_xlabel('Yarış Sayısı')
axes[1,1].set_ylabel('Galibiyet Sayısı')
axes[1,1].set_title('Yarış Sayısı vs Galibiyet (Pilotlar)')

plt.tight_layout()
plt.savefig('ferrari_karsilastirmali_analiz.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. Heatmap Analizi
print("\n6. Heatmap Analizi")
# Sezon bazında pilot performansı
season_driver = pd.read_csv('ferrari_sezon_pilot_ozet.csv', index_col=[0,1])

# Puan heatmap'i için pivot table oluştur
pivot_points = season_driver['Puan'].unstack(fill_value=0)

plt.figure(figsize=(15, 10))
sns.heatmap(pivot_points, annot=True, fmt='.0f', cmap='Reds', cbar_kws={'label': 'Puan'})
plt.title('Ferrari: Sezon-Pilot Puan Heatmap', fontsize=16, fontweight='bold')
plt.xlabel('Pilot')
plt.ylabel('Sezon')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('ferrari_sezon_pilot_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 7. Özet Dashboard
print("\n7. Özet Dashboard")
fig = plt.figure(figsize=(20, 15))
fig.suptitle('FERRARI PERFORMANS DASHBOARD', fontsize=20, fontweight='bold', color='red')

# Toplam istatistikler
total_stats = {
    'Toplam Yarış': yearly['Yarış'].sum(),
    'Toplam Galibiyet': yearly['Galibiyet'].sum(),
    'Toplam Podyum': yearly['Podyum'].sum(),
    'Toplam Puan': yearly['Puan'].sum()
}

# Dashboard layout
gs = fig.add_gridspec(3, 4, hspace=0.3, wspace=0.3)

# 1. Toplam istatistikler
ax1 = fig.add_subplot(gs[0, :2])
bars = ax1.bar(total_stats.keys(), total_stats.values(), color=['red', 'gold', 'orange', 'blue'], alpha=0.8)
ax1.set_title('Ferrari Genel İstatistikler', fontsize=14, fontweight='bold')
ax1.set_ylabel('Sayı')
for bar, value in zip(bars, total_stats.values()):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(total_stats.values())*0.01, 
             f'{value:,.0f}', ha='center', va='bottom', fontweight='bold')

# 2. En başarılı pilot
ax2 = fig.add_subplot(gs[0, 2:])
top_pilot = driver_stats.iloc[0]
ax2.pie([top_pilot['Galibiyet'], top_pilot['Podyum'] - top_pilot['Galibiyet']], 
        labels=['Galibiyet', 'Diğer Podyumlar'], autopct='%1.1f%%', colors=['gold', 'orange'])
ax2.set_title(f'En Başarılı Pilot: {driver_stats.index[0]}', fontsize=14, fontweight='bold')

# 3. En başarılı sezon
ax3 = fig.add_subplot(gs[1, :2])
best_season = yearly.loc[yearly['Galibiyet'].idxmax()]
ax3.bar(['Galibiyet', 'Podyum', 'Puan'], 
        [best_season['Galibiyet'], best_season['Podyum'], best_season['Puan']/100], 
        color=['red', 'orange', 'blue'], alpha=0.8)
ax3.set_title(f'En Başarılı Sezon: {yearly["Galibiyet"].idxmax()}', fontsize=14, fontweight='bold')
ax3.set_ylabel('Sayı')

# 4. En başarılı pist
ax4 = fig.add_subplot(gs[1, 2:])
best_circuit = circuit_stats.iloc[0]
ax4.bar(['Galibiyet', 'Podyum', 'Puan'], 
        [best_circuit['Galibiyet'], best_circuit['Podyum'], best_circuit['Puan']/100], 
        color=['crimson', 'orange', 'gold'], alpha=0.8)
ax4.set_title(f'En Başarılı Pist: {circuit_stats.index[0]}', fontsize=14, fontweight='bold')
ax4.set_ylabel('Sayı')

# 5. Yıllık trend
ax5 = fig.add_subplot(gs[2, :])
ax5.plot(yearly.index, yearly['Galibiyet'], 'ro-', linewidth=2, label='Galibiyet', markersize=8)
ax5.plot(yearly.index, yearly['Podyum'], 'go-', linewidth=2, label='Podyum', markersize=8)
ax5.set_title('Ferrari Yıllık Trend', fontsize=14, fontweight='bold')
ax5.set_xlabel('Yıl')
ax5.set_ylabel('Sayı')
ax5.legend()
ax5.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ferrari_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nTüm görselleştirmeler tamamlandı!")
print("\nOluşturulan Grafikler:")
print("1. ferrari_yillik_performans_analizi.png")
print("2. ferrari_pist_performans_analizi.png")
print("3. ferrari_pilot_performans_analizi.png")
print("4. ferrari_en_basarili_sezonlar_analizi.png")
print("5. ferrari_karsilastirmali_analiz.png")
print("6. ferrari_sezon_pilot_heatmap.png")
print("7. ferrari_dashboard.png") 
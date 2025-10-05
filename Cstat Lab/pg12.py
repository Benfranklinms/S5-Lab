import matplotlib.pyplot as plt

continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'Soviet Union']
areas = [11.7, 10.4, 1.9, 9.4, 3.3, 6.9, 7.9]

plt.figure(figsize=(10, 6))
plt.bar(continents, areas, color='purple', edgecolor='black')

plt.title('Areas of Continents (in Millions of Square Miles)')
plt.xlabel('Continent')
plt.ylabel('Area (Million sq. miles)')

for i, area in enumerate(areas):
    plt.text(i, area + 0.2, str(area), ha='center', fontsize=10)

plt.tight_layout()
plt.show()

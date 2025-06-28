import pandas as pd

df= pd.read_excel('deprem.xlsx')

df['TarihSaat'] = pd.to_datetime(df['Tarih'].astype(str)+ ' ' + df['Saat'], format='%Y.%m.%d %H:%M:%S')#Bu satır sayesinde sütunlar birleştirilir.

df.drop(['Tarih', 'Saat'], axis=1, inplace=True)

# print("\n Güncellenmiş Veri Tipleri: ")
# print(df.dtypes)

df['ML'] = pd.to_numeric(df['ML'], errors='coerce')
# print("\n 'ML' sütunundaki eksik değerler: ")
# print(df['ML'].isnull().sum())
df_clean = df.dropna(subset=['ML'])
# print('Temizlenmiş veri seti boyutu : ', df_clean.shape)

import matplotlib.pyplot as plt
import seaborn as sns

#TARİHE GÖRE DEPREM SAYISI
# plt.figure(figsize=(12,6))
# plt.countplot(data=df_clean, x=df_clean['TarihSaat'].dt.data, palette='viridis')
# plt.xticks(rotation=45)
# plt.title("Günlere göre deprem sayısı")
# plt.xlabel('Tarih')
# plt.ylabel('Deprem Sayısı')
# plt.tight_layout()
# plt.show()

#DEPREMİN BÜYÜKLÜK DAĞILIMI
# plt.figure(figsize=(8,6))
# sns.histplot(df_clean['ML'], bins=50, kde=True, color='skyblue')
# plt.title('Depremin büyüklük dağılımı')
# plt.xlabel('Büyüklük(ML)')
# plt.ylabel('Frekans')
# plt.show()



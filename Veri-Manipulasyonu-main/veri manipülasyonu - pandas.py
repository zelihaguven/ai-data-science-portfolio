# Veri Manipülasyonu - Pandas

import pandas as pd
import numpy as np

# Pandas Serisi Oluşturma
seri = pd.Series([1, 2, 3, 4, 5])

# Serinin Temel Özellikleri
print(type(seri))  # pandas.core.series.Series
print(seri.axes)  # RangeIndex(start=0, stop=5, step=1)
print(seri.dtype)  # dtype
print(seri.size)  # Eleman sayısı
print(seri.ndim)  # Boyut
print(seri.values)  # Sadece değerlere erişir
print(seri.head(3))  # İlk üç elemanı getirir
print(seri.tail(3))  # Son üç elemanı getirir

# Index İsimlendirmesi
seri_indexed = pd.Series([9, 2, 3, 94, 5], index=['a', 'b', 'c', 'd', 'e'])
print(seri_indexed['a'])  # 9
print(seri_indexed['a':'c'])  # 'a' ve 'c' arasındaki değerler

# Sözlük üzerinden liste oluşturmak
sozluk = {'reg': 10, 'log': 11, 'cart': 12}
seri_from_dict = pd.Series(sozluk)

# İki Seriyi Birleştirmek
seri1 = pd.Series([1, 2, 3])
seri2 = pd.Series([4, 5, 6])
print(pd.concat([seri1, seri2]))

# Pandas DataFrame Oluşturma
l = [1, 2, 39, 67, 90]
df = pd.DataFrame(l, columns=["degisken_ismi"])

m = np.arange(1, 10).reshape((3, 3))
df2 = pd.DataFrame(m, columns=["var1", "var2", "var3"])

# DataFrame İsimlendirme
df2.columns = ["deg1", "deg2", "deg3"]
print(df2.head())
print(df2.columns)

# DataFrame Özellikleri
print(df2.axes)  # Satır ve sütun bilgileri
print(df2.shape)  # (3, 3)
print(df2.ndim)  # 2
print(df2.size)  # 9
print(df2.values)  # Numpy array'e çevirir

# Numpy Array üzerinden DataFrame
a = np.array([1, 2, 3, 4, 5])
df_from_array = pd.DataFrame(a, columns=["deg1"])

# Rastgele Değerler ile DataFrame Oluşturma
s1 = np.random.randint(10, size=5)
s2 = np.random.randint(10, size=5)
s3 = np.random.randint(10, size=5)
sozluk = {"var1": s1, "var2": s2, "var3": s3}
df3 = pd.DataFrame(sozluk)

# DataFrame İndeks Ayarlama
df3.index = ["a", "b", "c", "d", "e"]

# Satır Silme
df3.drop("a", axis=0, inplace=True)  # Kalıcı silme

# Fancy Indexing
l = ["c", "e"]
print(df3.drop(l, axis=0))  # 'c' ve 'e' satırlarını sil

# Kolon Kontrolü
print("var1" in df3)  # True
l = ["var1", "var4", "var2"]
for i in l:
    print(i in df3)  # True veya False döner

# Yeni Değişken Oluşturma
df3["var4"] = df3["var1"] / df3["var2"]

# Birleştirme - Join İşlemleri (Kısaca açıklama)
# DataFrame'leri birleştirmek için 'merge' veya 'join' fonksiyonları kullanılır.

# Örnek Birleşim
df4 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']})
df5 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'C': ['C0', 'C1', 'C2' ]})
result = pd.merge(df4, df5, on='A')  # 'A' kolonuna göre birleştirir
print(result)

# Gruplama ve Toplulaştırma
# aggregate - 'groupby' ile toplulaştırma
df_crop = df3.groupby('var1').agg({'var2': 'mean'}) # var1' göre var2'nin ortalamasını alır.
print(df_crop)

# apply - Fonksiyon Uygulama
df3['var1'].apply(lambda x: x + 1)  # var1'e 1 ekler

# Sonuç
print(df3)
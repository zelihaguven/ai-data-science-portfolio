# Veri Manipülasyonu - NumPy Kütüphanesi
import numpy as np

# Array oluşturma
a = np.array([1, 2, 3, 4, 5])
print(type(a))  # numpy.ndarray
print(np.array([3.14, 13, 4, 2]))  # hepsini ondalık yaptı
print(np.array([3.14, 13, 4, 2], dtype="int"))  # hepsini int yaptı

# Sıfırdan array oluşturma
print(np.zeros(10, dtype=int))  # array([0,0,0,0,0,0,0,0,0,0])
print(np.ones((3, 5)))  # 3 satır 5 sütunlu tamamen 1’den oluşan bir array oluşturur.
print(np.full((2, 4), 3))  # sadece 3’lerden oluşan 2 satır 4 sütunlu bir array

print(np.arange(0, 31, 3)) 
# 0’dan başlar 30’a kadar gider, üçer üçer artar.

print(np.linspace(0, 1, 10)) 
# 0 ile 1 arasında 10 eşit parçaya bölünmüş array oluşturur.

print(np.random.normal(10, 4, (3, 4))) 
# Dağılımını kendimiz belirttiğimiz ama rastgele seçilen sayılardan oluşan bir dizi

print(np.random.randint(0, 10, (3, 3))) 
# 0 ile 10 arasında rastgele 3x3 matris

# ndim : boyut sayısı
# shape : boyut bilgisi
# size : toplam eleman sayısı
# dtype : array veri tipi

a = np.random.randint(10, size=10)
print(a.ndim)  # 1
print(a.shape)  # (10,)
print(a.size)  # 10
print(a.dtype)  # dtype('int64')

b = np.random.randint(10, size=(3, 5))
print(b.ndim)  # 2
print(b.shape)  # (3,5)
print(b.size)  # 15
print(b.dtype)  # dtype('int64')

# Yeniden şekillendirme - reshaping
a = np.arange(1, 10) 
# array([1,2,3,4,5,6,7,8,9]) 

print(a.reshape((3, 3))) 
# array([[1,2,3], [4,5,6], [7,8,9]])

b = a.reshape((1, 9))
print(b.ndim)  # 2

# Birleştirme - concatenation
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.array([7, 8, 9])

print(np.concatenate([x, y, z])) 
# array([1,2,3,4,5,6,7,8,9])

# İki boyutta birleştirme
a = np.array([[1, 2, 3], [4, 5, 6]])

print(np.concatenate([a, a])) 
# array([[1,2,3], [4,5,6], [1,2,3], [4,5,6]])

print(np.concatenate([a, a], axis=1)) 
# array([[1,2,3,1,2,3], [4,5,6,4,5,6]]) 

# Array ayırma - splitting
a = np.array([1, 2, 3, 99, 99, 3, 2, 1])
d, b, c = np.split(a, [3, 5])
# [1,2,3], [99,99], [3,2,1]

# İki boyutlu ayırma
m = np.arange(16).reshape(4, 4) 

print(np.vsplit(m, [2])) 
# array([[0,1,2,3], [4,5,6,7]]), array([[8,9,10,11], [12,13,14,15]])

print(np.hsplit(m, [2])) 
# array([[0,1], [4,5], [8,9], [12,13]]), array([[2,3], [6,7], [10,11], [14,15]]) 

# Sıralama - sorting
v = np.array([2, 1, 4, 3, 5])
v.sort()
print(v)  # array([1,2,3,4,5])

# Index ile elemanlara erişmek
print(a[0])  # ilk elemana erişilir
print(a[-1])  # son elemana erişilir
a[0] = 100  # eleman değiştirme yapılabilir

m[1, 4] = 2.2  # eğer array tipi int ise, eklenen float sayı int’e dönüşür

# Slicing
a = np.arange(20, 30) 
# array([20,21,22,23,24,25,26,27,28,29])

print(a[0:3])  # array([20,21,22])
print(a[:3])  # array([20,21,22])

print(m[:, 0])  # ilk sütunu alır
print(m[:, 1])  # ikinci sütunu alır
print(m[1, :])  # ikinci satırı alır
print(m[1:3, 0:2])  # array([[0,4], [8,2]])

# Fancy indexleme
v = np.arange(0, 30, 3)
al_getir = [1, 3, 5] 
print(v[al_getir]) 
# array([3,9,15])

# **Koşul ifadeleri (Conditions)**
a = np.random.randint(0, 10, 10)
print(a > 5)  # Boolean dizi döndürür
print(a[a > 5])  # 5'ten büyük değerleri getirir

# Koşul kullanımı ile değiştirme
a[a % 2 == 0] = -1  # Çift sayıları -1 yap

# if-else ile koşul ifadeleri
for i in a:
    if i > 5:
        print(f"{i} büyük")
    else:
        print(f"{i} küçük veya eşit")

# **Matematiksel İşlemler**
b = np.arange(1, 6)

print(b + 10)  # array([11,12,13,14,15])
print(b * 2)  # array([2,4,6,8,10])
print(b ** 2)  # array([1,4,9,16,25])
print(np.sqrt(b))  # karekök hesaplama
print(np.log(b))  # logaritma hesaplama
print(np.exp(b))  # üstel hesaplama (e^x)
print(np.sum(b))  # toplam
print(np.mean(b))  # ortalama
print(np.median(b))  # medyan
print(np.std(b))  # standart sapma

# **Matris işlemleri**
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print(np.dot(A, B))  # Matris çarpımı
print(np.linalg.inv(A))  # A matrisinin tersini bulma
print(np.linalg.det(A))  # A matrisinin determinantı
print(np.linalg.eig(A))  # Eigen değerleri ve vektörleri
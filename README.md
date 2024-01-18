Projeyi çekildikten sonra çalıştırma seçenekleri :

1-

Feature klasörüne girilir ve "addProductsCart.feature" ile kullanılan IDE(pyCharm)'ye göre değişmekle beraber  içinde bulundugumuz "addProductsCart.feature" run edilerek çalıştırılabilir


2-
Terminalde  proje çalıştırılabilir öncesinde aşağıda ki kodlar çalıştırılmalıdır. Aşağıdakilerin haricinde kurulan bilgisayar gereksinimlerine göre hata veren işlevler update edilmedilidir.

Projekten bir terminal veya komut istemcisini açın.
Aşağıdaki komutu kullanarak bir sanal ortam oluşturun:
  python -m venv venv

Windows için:
  venv\Scripts\activate
Unix veya MacOS için:
  source venv/bin/activate
Daha sonra terminalde
pip install selenium
pip install allure-behave

behave addProductsCart.feature " komutunu ile testi çalıştırın

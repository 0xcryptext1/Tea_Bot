# TEA Bot

Bu proje, TEA ağında tx kasmanızı sağlayan bir bot içerir. Aşağıdaki adımları izleyerek projeyi kurabilir ve çalıştırabilirsiniz.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki yazılımların yüklü olması gerekmektedir:

- Python 3.x
- pip (Python paket yöneticisi)

## Kurulum

1. **Depoyu Klonlayın**

   Terminal veya komut istemcisinde aşağıdaki komutu kullanarak projeyi klonlayın:

   ```bash
   git clone https://github.com/0xcryptext1/Tea_Bot.git
   cd Tea_Bot
   ```

2. **Gerekli Kütüphaneleri Yükleyin**

   Aşağıdaki komutu kullanarak gerekli kütüphaneleri yükleyin:

   ```bash
   pip install web3
   ```

3. **Cüzdan Bilgilerini Ayarlayın**

   `wallet.txt` dosyasını oluşturun ve aşağıdaki formatta cüzdan adresinizi ve özel anahtarınızı ekleyin:

   ```
   <cüzdan_adresi>,<özel_anahtar>
   ```

## Çalıştırma

Projenin ana fonksiyonlarını çalıştırmak için aşağıdaki komutu kullanın:
```bash
python main.py
```

## Kullanım

Bot, rastgele olarak belirlenen işlemleri gerçekleştirecektir. Her işlem için konsolda bilgi mesajları görüntülenecektir.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.
